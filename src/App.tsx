import { useState } from 'react'
import { calcularSequencia } from './lib/streak'
import { useProgresso } from './state'
import { Ajustes } from './ui/Ajustes'
import { Licao } from './ui/Licao'
import { Painel } from './ui/Painel'
import { Revisar } from './ui/Revisar'
import { Simulado } from './ui/Simulado'
import { Trilha } from './ui/Trilha'

type Aba = 'trilha' | 'revisar' | 'simulado' | 'progresso' | 'ajustes'

const ABAS: Array<{ id: Aba; rotulo: string }> = [
  { id: 'trilha', rotulo: 'Trilha' },
  { id: 'revisar', rotulo: 'Revisar' },
  { id: 'simulado', rotulo: 'Simulado' },
  { id: 'progresso', rotulo: 'Progresso' },
  { id: 'ajustes', rotulo: 'Ajustes' },
]

export default function App() {
  const { p, hoje, pronto } = useProgresso()
  const [aba, setAba] = useState<Aba>('trilha')
  const [licaoAberta, setLicaoAberta] = useState<string | null>(null)

  if (!pronto) return <p className="carregando">Carregando seu progresso...</p>

  const seq = calcularSequencia(p.xpPorDia, p.metaDiaria, hoje)
  const xpHoje = p.xpPorDia[hoje] ?? 0

  return (
    <div className="app">
      <header className="topo">
        <div className="marca">Estudos ABDI</div>
        <dl className="placar">
          <div><dt>Sequência</dt><dd>{seq.atual} {seq.atual === 1 ? 'dia' : 'dias'}</dd></div>
          <div><dt>Hoje</dt><dd>{xpHoje} de {p.metaDiaria} XP</dd></div>
          <div><dt>Escudo</dt><dd>{seq.escudoDisponivel ? 'disponível' : 'usado na semana'}</dd></div>
        </dl>
        <div className="barra meta" aria-label="Meta diária"><div style={{ width: `${Math.min(100, (100 * xpHoje) / p.metaDiaria)}%` }} /></div>
      </header>

      <main>
        {licaoAberta ? (
          <Licao licaoId={licaoAberta} onSair={() => setLicaoAberta(null)} />
        ) : (
          <>
            {aba === 'trilha' && <Trilha onAbrirLicao={setLicaoAberta} onIrPara={setAba} />}
            {aba === 'revisar' && <Revisar />}
            {aba === 'simulado' && <Simulado />}
            {aba === 'progresso' && <Painel />}
            {aba === 'ajustes' && <Ajustes />}
          </>
        )}
      </main>

      {!licaoAberta && (
        <nav className="abas" aria-label="Seções">
          {ABAS.map((a) => (
            <button
              key={a.id}
              type="button"
              className={aba === a.id ? 'ativa' : ''}
              aria-current={aba === a.id ? 'page' : undefined}
              onClick={() => setAba(a.id)}
            >
              {a.rotulo}
              {a.id === 'revisar' && p.caderno.length > 0 ? ` (${p.caderno.length})` : ''}
            </button>
          ))}
        </nav>
      )}
    </div>
  )
}
