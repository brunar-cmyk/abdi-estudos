import { useState } from 'react'
import { avaliarCarta, concluirLicao, registrarResposta } from '../lib/acoes'
import { licaoPorId } from '../lib/content'
import { NOTA_DIFICIL, NOTA_ERREI, NOTA_FACIL } from '../lib/srs'
import { useProgresso } from '../state'
import { QuestaoView } from './QuestaoView'

type Etapa = 'resumo' | 'cards' | 'questoes' | 'fim'

export function Licao({ licaoId, onSair }: { licaoId: string; onSair: () => void }) {
  const achada = licaoPorId(licaoId)
  const { atualizar, hoje } = useProgresso()
  const [etapa, setEtapa] = useState<Etapa>('resumo')
  const [i, setI] = useState(0)
  const [virado, setVirado] = useState(false)
  const [sel, setSel] = useState<number | null>(null)
  const [revelar, setRevelar] = useState(false)
  const [acertos, setAcertos] = useState(0)

  if (!achada) return <p>Lição não encontrada.</p>
  const { unidade, licao } = achada
  const cards = licao.flashcards
  const questoes = licao.questoes

  function avancarEtapa(proxima: Etapa) {
    setEtapa(proxima)
    setI(0)
    setVirado(false)
    setSel(null)
    setRevelar(false)
  }

  function avaliarFlash(nota: 1 | 3 | 5) {
    atualizar((p) => avaliarCarta(p, `fc:${licao.id}:${i}`, nota, hoje))
    if (i + 1 < cards.length) {
      setI(i + 1)
      setVirado(false)
    } else avancarEtapa('questoes')
  }

  function responder() {
    if (sel === null) return
    const q = questoes[i]
    const certa = sel === q.correta
    if (certa) setAcertos((a) => a + 1)
    atualizar((p) => registrarResposta(p, q.id, certa, hoje))
    setRevelar(true)
  }

  function proxima() {
    if (i + 1 < questoes.length) {
      setI(i + 1)
      setSel(null)
      setRevelar(false)
    } else {
      atualizar((p) => concluirLicao(p, licao.id, acertos, questoes.length, hoje))
      setEtapa('fim')
    }
  }

  const progresso =
    etapa === 'resumo' ? 0.05 : etapa === 'cards' ? 0.1 + 0.3 * (i / Math.max(cards.length, 1))
    : etapa === 'questoes' ? 0.4 + 0.6 * (i / Math.max(questoes.length, 1)) : 1

  return (
    <section className="licao">
      <header className="licao-topo">
        <button type="button" className="link" onClick={onSair}>Sair da lição</button>
        <div className="barra" aria-label="Progresso da lição"><div style={{ width: `${progresso * 100}%` }} /></div>
      </header>
      <p className="muted">{unidade.titulo}</p>
      <h2>{licao.titulo}</h2>

      {etapa === 'resumo' && (
        <>
          <h3>Resumo</h3>
          <ul className="resumo">{licao.resumo.map((t, k) => <li key={k}>{t}</li>)}</ul>
          <button type="button" className="primario" onClick={() => avancarEtapa(cards.length ? 'cards' : 'questoes')}>
            Continuar para os flashcards
          </button>
        </>
      )}

      {etapa === 'cards' && cards[i] && (
        <>
          <h3>Flashcard {i + 1} de {cards.length}</h3>
          <button type="button" className={`card ${virado ? 'virado' : ''}`} onClick={() => setVirado(true)}>
            {virado ? cards[i].verso : cards[i].frente}
            {!virado && <span className="dica">Toque para ver a resposta</span>}
          </button>
          {virado && (
            <div className="linha">
              <button type="button" className="erro" onClick={() => avaliarFlash(NOTA_ERREI)}>Errei</button>
              <button type="button" onClick={() => avaliarFlash(NOTA_DIFICIL)}>Difícil</button>
              <button type="button" className="primario" onClick={() => avaliarFlash(NOTA_FACIL)}>Fácil</button>
            </div>
          )}
        </>
      )}

      {etapa === 'questoes' && questoes[i] && (
        <>
          <h3>Questão {i + 1} de {questoes.length}</h3>
          <QuestaoView questao={questoes[i]} selecionada={sel} revelar={revelar} onEscolher={setSel} />
          {!revelar
            ? <button type="button" className="primario" disabled={sel === null} onClick={responder}>Responder</button>
            : <button type="button" className="primario" onClick={proxima}>{i + 1 < questoes.length ? 'Próxima' : 'Concluir lição'}</button>}
        </>
      )}

      {etapa === 'fim' && (
        <div className="fim">
          <h3>Lição concluída</h3>
          <p>Você acertou {acertos} de {questoes.length}. As questões erradas foram para o Caderno de erros e voltam na revisão de amanhã.</p>
          <button type="button" className="primario" onClick={onSair}>Voltar à trilha</button>
        </div>
      )}
    </section>
  )
}
