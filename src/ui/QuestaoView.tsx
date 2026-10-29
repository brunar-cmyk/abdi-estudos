import type { Questao } from '../lib/types'

const LETRAS = ['A', 'B', 'C', 'D', 'E']

interface Props {
  questao: Questao
  selecionada: number | null
  /** Quando verdadeiro, mostra gabarito e explicação e trava a escolha. */
  revelar: boolean
  onEscolher: (i: number) => void
}

export function QuestaoView({ questao, selecionada, revelar, onEscolher }: Props) {
  return (
    <div className="questao">
      <p className="enunciado">{questao.enunciado}</p>
      <ul className="alternativas" role="radiogroup">
        {questao.alternativas.map((alt, i) => {
          let classe = 'alt'
          if (selecionada === i) classe += ' marcada'
          if (revelar && i === questao.correta) classe += ' certa'
          if (revelar && selecionada === i && i !== questao.correta) classe += ' errada'
          return (
            <li key={i}>
              <button
                type="button"
                role="radio"
                aria-checked={selecionada === i}
                className={classe}
                disabled={revelar}
                onClick={() => onEscolher(i)}
              >
                <span className="letra">{LETRAS[i]}</span>
                <span>{alt}</span>
              </button>
            </li>
          )
        })}
      </ul>
      {revelar && (
        <div className="explicacao" role="status">
          <strong>{selecionada === questao.correta ? 'Correto.' : `Resposta certa: ${LETRAS[questao.correta]}.`}</strong>
          <p>{questao.explicacao}</p>
          <p className="fonte">Fonte: {questao.fonte}</p>
        </div>
      )}
    </div>
  )
}
