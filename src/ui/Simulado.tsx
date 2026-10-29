import { useEffect, useMemo, useRef, useState } from 'react'
import { guardarSimulado, registrarResposta } from '../lib/acoes'
import { questaoPorId, todasQuestoes } from '../lib/content'
import { formatarData } from '../lib/dates'
import { BLOCOS, COTAS_SIMULADO, DURACAO_SIMULADO_MIN, pontuar, type ResultadoProva } from '../lib/scoring'
import { montarSimulado } from '../lib/simulado'
import type { ResultadoSalvo, SimuladoEmAndamento } from '../lib/storage'
import { useProgresso } from '../state'
import { QuestaoView } from './QuestaoView'

function formatarTempo(ms: number): string {
  const s = Math.max(0, Math.floor(ms / 1000))
  const h = Math.floor(s / 3600)
  const m = Math.floor((s % 3600) / 60)
  return `${h}:${String(m).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`
}

function calcular(sim: SimuladoEmAndamento): ResultadoProva {
  return pontuar(
    sim.ids.map((id) => {
      const q = questaoPorId(id)!
      return { bloco: q.unidade.bloco, correta: q.correta, marcada: sim.respostas[id] ?? null }
    }),
  )
}

export function Simulado() {
  const { p, hoje, atualizar } = useProgresso()
  const [resultado, setResultado] = useState<{ sim: SimuladoEmAndamento; res: ResultadoProva } | null>(null)
  const banco = useMemo(() => todasQuestoes(), [])

  if (resultado) return <Resultado {...resultado} onVoltar={() => setResultado(null)} />

  if (p.simuladoAtual) {
    return (
      <Prova
        sim={p.simuladoAtual}
        onFinalizar={(sim) => {
          const res = calcular(sim)
          const salvo: ResultadoSalvo = {
            data: hoje,
            acertos: res.acertos,
            total: res.totalQuestoes,
            pontos: res.pontos,
            aprovado: res.aprovado,
            porBloco: res.porBloco,
          }
          atualizar((x) => {
            let novo = x
            for (const id of sim.ids) {
              const q = questaoPorId(id)!
              novo = registrarResposta(novo, id, sim.respostas[id] === q.correta, hoje)
            }
            return guardarSimulado(novo, salvo, hoje)
          })
          setResultado({ sim, res })
        }}
      />
    )
  }

  const montagem = montarSimulado(banco.map((q) => ({ id: q.id, categoria: q.unidade.categoria, bloco: q.unidade.bloco })))
  return (
    <section>
      <h2>Simulado</h2>
      <p>60 questões na proporção da prova, 3h30 de cronômetro, nota real (0,3 e 0,65) e aviso se algum bloco zerar.</p>
      {montagem.faltas.length > 0 && (
        <div className="aviso">
          <strong>O banco de questões ainda está incompleto.</strong> Este simulado terá {montagem.ids.length} questões em vez de 60.
          Faltam: {montagem.faltas.map((f) => `${f.rotulo} (${f.faltam})`).join(', ')}.
        </div>
      )}
      <button
        type="button"
        className="primario"
        disabled={montagem.ids.length === 0}
        onClick={() => atualizar((x) => ({ ...x, simuladoAtual: { iniciadoEm: Date.now(), ids: montagem.ids, respostas: {} } }))}
      >
        Começar simulado
      </button>
      {p.simulados.length > 0 && (
        <>
          <h3>Simulados anteriores</h3>
          <ul className="lista">
            {[...p.simulados].reverse().map((s, k) => (
              <li key={k}>
                {formatarData(s.data)}: {s.acertos}/{s.total} acertos, {s.pontos.toFixed(2).replace('.', ',')} pontos, {s.aprovado ? 'aprovada' : 'reprovada'}
              </li>
            ))}
          </ul>
        </>
      )}
    </section>
  )
}

function Prova({ sim, onFinalizar }: { sim: SimuladoEmAndamento; onFinalizar: (s: SimuladoEmAndamento) => void }) {
  const { atualizar } = useProgresso()
  const [i, setI] = useState(0)
  const [agora, setAgora] = useState(Date.now())
  const restante = sim.iniciadoEm + DURACAO_SIMULADO_MIN * 60_000 - agora

  useEffect(() => {
    const t = setInterval(() => setAgora(Date.now()), 1000)
    return () => clearInterval(t)
  }, [])
  const encerrado = useRef(false)
  useEffect(() => {
    if (restante <= 0 && !encerrado.current) {
      encerrado.current = true
      onFinalizar(sim)
    }
  }, [restante, sim, onFinalizar])

  const q = questaoPorId(sim.ids[i])!
  const respondidas = sim.ids.filter((id) => sim.respostas[id] != null).length

  function marcar(alt: number) {
    atualizar((x) =>
      x.simuladoAtual ? { ...x, simuladoAtual: { ...x.simuladoAtual, respostas: { ...x.simuladoAtual.respostas, [q.id]: alt } } } : x,
    )
  }

  return (
    <section>
      <div className="cronometro" aria-live="off">
        <span>Tempo restante</span> <strong>{formatarTempo(restante)}</strong>
        <span className="muted"> {respondidas} de {sim.ids.length} respondidas</span>
      </div>
      <p className="muted">Questão {i + 1} de {sim.ids.length}, {q.unidade.bloco}</p>
      <QuestaoView questao={q} selecionada={sim.respostas[q.id] ?? null} revelar={false} onEscolher={marcar} />
      <div className="linha">
        <button type="button" disabled={i === 0} onClick={() => setI(i - 1)}>Anterior</button>
        <button type="button" disabled={i === sim.ids.length - 1} onClick={() => setI(i + 1)}>Próxima</button>
      </div>
      <div className="grade" role="navigation" aria-label="Ir para a questão">
        {sim.ids.map((id, k) => (
          <button key={id} type="button" className={`${sim.respostas[id] != null ? 'feita' : ''} ${k === i ? 'atual' : ''}`} onClick={() => setI(k)}>
            {k + 1}
          </button>
        ))}
      </div>
      <button
        type="button"
        className="primario"
        onClick={() => {
          const faltam = sim.ids.length - respondidas
          if (faltam === 0 || window.confirm(`Ainda há ${faltam} sem resposta. Finalizar mesmo assim? Em branco vale zero.`)) onFinalizar(sim)
        }}
      >
        Finalizar simulado
      </button>
    </section>
  )
}

function Resultado({ sim, res, onVoltar }: { sim: SimuladoEmAndamento; res: ResultadoProva; onVoltar: () => void }) {
  const nomeBloco = (b: string) => b
  return (
    <section>
      <h2>Resultado do simulado</h2>
      <p className={res.aprovado ? 'ok' : 'alerta'}>
        {res.aprovado ? 'Aprovada neste simulado.' : 'Reprovada neste simulado.'}
      </p>
      <p>
        {res.acertos} acertos de {res.totalQuestoes} (mínimo {res.minimoParaAprovar}). Nota: {res.pontos.toFixed(2).replace('.', ',')}
        {res.totalQuestoes === 60 ? ' de 25 pontos.' : ' pontos. Simulado parcial, então a nota máxima é menor que 25.'}
      </p>
      {res.blocosZerados.length > 0 && (
        <div className="aviso">
          <strong>Atenção:</strong> você zerou {res.blocosZerados.join(' e ')}. Pelo edital (item 9.5, b), zerar uma área elimina o candidato mesmo com acertos suficientes.
        </div>
      )}
      <table className="tabela">
        <thead><tr><th>Bloco</th><th>Acertos</th><th>Pontos</th></tr></thead>
        <tbody>
          {BLOCOS.map((b) => (
            <tr key={b}>
              <td>{nomeBloco(b)}</td>
              <td>{res.porBloco[b].acertos} de {res.porBloco[b].total}</td>
              <td>{res.porBloco[b].pontos.toFixed(2).replace('.', ',')}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <h3>Por disciplina</h3>
      <ul className="lista">
        {Object.entries(COTAS_SIMULADO).map(([cat, c]) => {
          const ids = sim.ids.filter((id) => questaoPorId(id)?.unidade.categoria === cat)
          if (ids.length === 0) return null
          const certas = ids.filter((id) => sim.respostas[id] === questaoPorId(id)!.correta).length
          return <li key={cat}>{c.rotulo}: {certas} de {ids.length}</li>
        })}
      </ul>
      <p className="muted">As questões erradas foram para o Caderno de erros.</p>
      <button type="button" className="primario" onClick={onVoltar}>Concluir</button>
    </section>
  )
}
