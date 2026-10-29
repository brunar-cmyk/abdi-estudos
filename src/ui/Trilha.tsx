import { PROVA_ISO, semanaDe, semanas, unidadePorId, eventos } from '../lib/content'
import { diffDias, formatarData } from '../lib/dates'
import { useProgresso } from '../state'

function textoPrazo(hoje: string, alvo: string): string {
  const d = diffDias(hoje, alvo)
  if (d < 0) return 'já passou'
  if (d === 0) return 'hoje'
  return d === 1 ? 'amanhã' : `em ${d} dias`
}

export function Trilha({ onAbrirLicao, onIrPara }: { onAbrirLicao: (id: string) => void; onIrPara: (aba: 'simulado' | 'revisar') => void }) {
  const { p, hoje } = useProgresso()
  const semanaAtual = semanaDe(hoje)
  const diasProva = Math.max(0, diffDias(hoje, PROVA_ISO.slice(0, 10)))

  const primeiraPendente = (ids: string[]) =>
    ids
      .map(unidadePorId)
      .flatMap((u) => (u ? u.licoes.map((l) => ({ u, l })) : []))
      .find(({ l }) => !(l.id in p.licoes))
  const proximaLicao = primeiraPendente(semanaAtual?.unidades ?? [])
  const proximaGeral = primeiraPendente(semanaAtual?.gerais ?? [])

  const proximosPrazos = eventos
    .map((e) => ({ ...e, alvo: e.fim?.slice(0, 10) ?? e.data ?? e.inicio?.slice(0, 10) ?? '' }))
    .filter((e) => e.alvo >= hoje && e.id !== 'publicacao')
    .slice(0, 3)

  return (
    <section>
      <div className="contagem">
        <strong>{diasProva}</strong> dias para a prova, 20/12/2026, 13h30 às 17h (horário de Brasília)
      </div>

      {semanaAtual && (
        <p className="muted">
          Semana {semanaAtual.n} ({formatarData(semanaAtual.inicio)} a {formatarData(semanaAtual.fim)}):{' '}
          {semanaAtual.modo === 'revisao' ? 'revisão. ' : ''}{semanaAtual.titulo}
        </p>
      )}

      <div className="destaque">
        <h2>Lição do dia</h2>
        {proximaLicao ? (
          <>
            <p className="muted">{proximaLicao.u.titulo}</p>
            <p><strong>{proximaLicao.l.titulo}</strong>, cerca de {proximaLicao.l.minutos} minutos</p>
            <button type="button" className="primario" onClick={() => onAbrirLicao(proximaLicao.l.id)}>Começar</button>
          </>
        ) : (
          <>
            <p>Você concluiu todas as lições desta semana que já estão no app.</p>
            <div className="linha">
              <button type="button" onClick={() => onIrPara('revisar')}>Fazer a revisão</button>
              <button type="button" onClick={() => onIrPara('simulado')}>Fazer um simulado</button>
            </div>
          </>
        )}
      </div>

      {proximaGeral && (
        <div className="destaque">
          <h2>Conhecimentos Gerais em paralelo</h2>
          <p className="muted">{proximaGeral.u.titulo}</p>
          <p><strong>{proximaGeral.l.titulo}</strong>, cerca de {proximaGeral.l.minutos} minutos</p>
          <button type="button" className="primario" onClick={() => onAbrirLicao(proximaGeral.l.id)}>Começar</button>
        </div>
      )}

      {proximosPrazos.length > 0 && (
        <div className="prazos">
          <h3>Prazos do edital</h3>
          <ul className="lista">
            {proximosPrazos.map((e) => (
              <li key={e.id}>{formatarData(e.alvo)} ({textoPrazo(hoje, e.alvo)}): {e.texto}</li>
            ))}
          </ul>
        </div>
      )}

      <h2>Trilha</h2>
      {semanas.map((s) => {
        const us = [...s.unidades, ...s.gerais].map((id) => ({ id, u: unidadePorId(id) }))
        const atual = semanaAtual?.n === s.n
        return (
          <details key={s.n} open={atual} className="semana">
            <summary>
              Semana {s.n}, {formatarData(s.inicio)} a {formatarData(s.fim)}{s.modo === 'revisao' ? ' (revisão)' : ''}
              {atual ? ' (atual)' : ''}
            </summary>
            <p className="muted">{s.titulo}</p>
            {us.length === 0 && <p className="muted">Simulados completos e revisão do caderno de erros.</p>}
            {us.some(({ id }) => s.gerais.includes(id)) && <p className="muted">As unidades de Conhecimentos Gerais seguem em paralelo.</p>}
            {us.map(({ id, u }) =>
              u ? (
                <div key={id} className="unidade">
                  <h4>{u.titulo}</h4>
                  <ul className="licoes">
                    {u.licoes.map((l) => {
                      const feita = p.licoes[l.id]
                      return (
                        <li key={l.id}>
                          <button type="button" className={feita ? 'feita' : ''} onClick={() => onAbrirLicao(l.id)}>
                            <span>{l.titulo}</span>
                            <span className="muted">{feita ? `${feita.acertos}/${feita.total}` : `${l.minutos} min`}</span>
                          </button>
                        </li>
                      )
                    })}
                  </ul>
                </div>
              ) : (
                <p key={id} className="muted em-preparo">Em preparo: {id}</p>
              ),
            )}
          </details>
        )
      })}
    </section>
  )
}
