import { useMemo, useState } from 'react'
import { avaliarCarta, cartasVencidas } from '../lib/acoes'
import { licaoPorId, questaoPorId } from '../lib/content'
import { NOTA_DIFICIL, NOTA_ERREI, NOTA_FACIL } from '../lib/srs'
import { useProgresso } from '../state'
import { QuestaoView } from './QuestaoView'

type Item =
  | { tipo: 'fc'; id: string; frente: string; verso: string }
  | { tipo: 'q'; id: string; questaoId: string }

function resolver(id: string): Item | null {
  if (id.startsWith('q:')) {
    const questaoId = id.slice(2)
    return questaoPorId(questaoId) ? { tipo: 'q', id, questaoId } : null
  }
  const [, licaoId, n] = id.split(':')
  const card = licaoPorId(licaoId)?.licao.flashcards[Number(n)]
  return card ? { tipo: 'fc', id, frente: card.frente, verso: card.verso } : null
}

export function Revisar() {
  const { p, hoje, atualizar } = useProgresso()
  const [aba, setAba] = useState<'fila' | 'caderno'>('fila')
  // A fila é congelada ao abrir a aba, para não mudar enquanto se avalia.
  const fila = useMemo(
    () => cartasVencidas(p, hoje).map(resolver).filter((x): x is Item => x !== null),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [],
  )
  const [i, setI] = useState(0)
  const [virado, setVirado] = useState(false)
  const [sel, setSel] = useState<number | null>(null)

  const atual = fila[i]

  function avaliar(nota: 1 | 3 | 5) {
    atualizar((x) => avaliarCarta(x, atual.id, nota, hoje))
    setI(i + 1)
    setVirado(false)
    setSel(null)
  }

  return (
    <section>
      <h2>Revisão</h2>
      <div className="abas-internas">
        <button type="button" className={aba === 'fila' ? 'ativa' : ''} onClick={() => setAba('fila')}>Para hoje ({fila.length})</button>
        <button type="button" className={aba === 'caderno' ? 'ativa' : ''} onClick={() => setAba('caderno')}>Caderno de erros ({p.caderno.length})</button>
      </div>

      {aba === 'fila' && (
        !atual ? (
          <p className="vazio">{fila.length === 0 ? 'Nada para revisar hoje. Faça uma lição para criar novos itens.' : 'Revisão de hoje concluída.'}</p>
        ) : atual.tipo === 'fc' ? (
          <>
            <p className="muted">Item {i + 1} de {fila.length}</p>
            <button type="button" className={`card ${virado ? 'virado' : ''}`} onClick={() => setVirado(true)}>
              {virado ? atual.verso : atual.frente}
              {!virado && <span className="dica">Toque para ver a resposta</span>}
            </button>
            {virado && (
              <div className="linha">
                <button type="button" className="erro" onClick={() => avaliar(NOTA_ERREI)}>Errei</button>
                <button type="button" onClick={() => avaliar(NOTA_DIFICIL)}>Difícil</button>
                <button type="button" className="primario" onClick={() => avaliar(NOTA_FACIL)}>Fácil</button>
              </div>
            )}
          </>
        ) : (
          <QuestaoRevisao
            key={atual.id}
            questaoId={atual.questaoId}
            sel={sel}
            setSel={setSel}
            posicao={`Item ${i + 1} de ${fila.length}`}
            onNota={avaliar}
          />
        )
      )}

      {aba === 'caderno' && (
        p.caderno.length === 0 ? <p className="vazio">Nenhum erro pendente.</p> : (
          <ul className="caderno">
            {p.caderno.map((id) => {
              const q = questaoPorId(id)
              if (!q) return null
              const est = p.questoes[id]
              return (
                <li key={id}>
                  <p className="muted">{q.unidade.titulo}, errada {est?.erradas ?? 1}x</p>
                  <p>{q.enunciado}</p>
                  <p><strong>Resposta:</strong> {q.alternativas[q.correta]}</p>
                  <p>{q.explicacao}</p>
                  <p className="fonte">Fonte: {q.fonte}</p>
                </li>
              )
            })}
          </ul>
        )
      )}
    </section>
  )
}

function QuestaoRevisao(props: {
  questaoId: string
  sel: number | null
  setSel: (n: number | null) => void
  posicao: string
  onNota: (n: 1 | 3 | 5) => void
}) {
  const q = questaoPorId(props.questaoId)!
  const [revelar, setRevelar] = useState(false)
  return (
    <>
      <p className="muted">{props.posicao}. Questão do caderno de erros</p>
      <QuestaoView questao={q} selecionada={props.sel} revelar={revelar} onEscolher={props.setSel} />
      {!revelar ? (
        <button type="button" className="primario" disabled={props.sel === null} onClick={() => setRevelar(true)}>Responder</button>
      ) : (
        <button type="button" className="primario" onClick={() => props.onNota(props.sel === q.correta ? NOTA_FACIL : NOTA_ERREI)}>Próximo</button>
      )}
    </>
  )
}
