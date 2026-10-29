import { useMemo } from 'react'
import { questaoPorId, syllabus, unidades } from '../lib/content'
import { BLOCOS } from '../lib/scoring'
import { useProgresso } from '../state'

const MIN_TENTATIVAS = 3

function pct(c: number, t: number): string {
  return t === 0 ? 'sem dados' : `${Math.round((100 * c) / t)}%`
}

export function Painel() {
  const { p } = useProgresso()

  const { porBloco, porTopico } = useMemo(() => {
    const blocos: Record<string, { c: number; t: number }> = Object.fromEntries(BLOCOS.map((b) => [b, { c: 0, t: 0 }]))
    const topicos: Record<string, { c: number; t: number }> = {}
    for (const [id, est] of Object.entries(p.questoes)) {
      const q = questaoPorId(id)
      if (!q) continue
      const t = est.certas + est.erradas
      blocos[q.unidade.bloco].c += est.certas
      blocos[q.unidade.bloco].t += t
      const topico = (topicos[q.topicoId] ??= { c: 0, t: 0 })
      topico.c += est.certas
      topico.t += t
    }
    return { porBloco: blocos, porTopico: topicos }
  }, [p.questoes])

  const nomeTopico = (id: string) => {
    const t = syllabus.find((x) => x.id === id)
    return t ? `${t.disciplina}, item ${t.item}` : id
  }

  const fracos = Object.entries(porTopico)
    .filter(([, v]) => v.t >= MIN_TENTATIVAS)
    .sort(([, a], [, b]) => a.c / a.t - b.c / b.t)
    .slice(0, 5)

  const totalLicoes = unidades.reduce((s, u) => s + u.licoes.length, 0)

  return (
    <section>
      <h2>Progresso</h2>
      <p>{Object.keys(p.licoes).length} de {totalLicoes} lições concluídas. {p.xp} XP no total.</p>

      <h3>Acertos por bloco</h3>
      <ul className="barras">
        {BLOCOS.map((b) => {
          const v = porBloco[b]
          return (
            <li key={b}>
              <span>{b}</span>
              <div className="barra"><div style={{ width: v.t ? `${(100 * v.c) / v.t}%` : '0%' }} /></div>
              <span>{pct(v.c, v.t)} ({v.c} de {v.t})</span>
            </li>
          )
        })}
      </ul>

      <h3>Tópicos mais fracos</h3>
      {fracos.length === 0 ? (
        <p className="muted">Aparecem aqui depois de pelo menos {MIN_TENTATIVAS} respostas no mesmo tópico.</p>
      ) : (
        <ul className="lista">
          {fracos.map(([id, v]) => (
            <li key={id}><strong>{nomeTopico(id)}</strong>: {pct(v.c, v.t)} ({v.c} de {v.t})</li>
          ))}
        </ul>
      )}

      <h3>Todos os tópicos</h3>
      <table className="tabela">
        <thead><tr><th>Tópico</th><th>Acertos</th></tr></thead>
        <tbody>
          {Object.entries(porTopico).sort(([a], [b]) => a.localeCompare(b)).map(([id, v]) => (
            <tr key={id}><td>{nomeTopico(id)}</td><td>{pct(v.c, v.t)} ({v.t} respostas)</td></tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
