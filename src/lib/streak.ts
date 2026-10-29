import { diffDias, inicioDaSemana, somarDias } from './dates'

export interface Sequencia {
  atual: number
  melhor: number
  /** Dias em que o escudo foi usado automaticamente. */
  diasProtegidos: string[]
  escudoDisponivel: boolean
}

/**
 * Calcula a sequência de dias a partir do XP de cada dia.
 * Um dia conta quando o XP do dia atinge a meta. O escudo protege um dia perdido
 * por semana (segunda a domingo) e é aplicado sozinho, em ordem cronológica.
 * O dia de hoje ainda aberto não quebra a sequência.
 */
export function calcularSequencia(
  xpPorDia: Record<string, number>,
  meta: number,
  hoje: string,
): Sequencia {
  const dias = Object.keys(xpPorDia).filter((d) => xpPorDia[d] >= meta).sort()
  const protegidos: string[] = []
  if (dias.length === 0) return { atual: 0, melhor: 0, diasProtegidos: protegidos, escudoDisponivel: true }

  const escudoUsadoNaSemana = new Set<string>()
  let atual = 0
  let melhor = 0
  const cumpridos = new Set(dias)

  for (let d = dias[0]; diffDias(d, hoje) >= 0; d = somarDias(d, 1)) {
    if (cumpridos.has(d)) {
      atual += 1
      melhor = Math.max(melhor, atual)
    } else if (d === hoje) {
      // hoje ainda pode ser cumprido
    } else {
      const semana = inicioDaSemana(d)
      if (atual > 0 && !escudoUsadoNaSemana.has(semana)) {
        escudoUsadoNaSemana.add(semana)
        protegidos.push(d)
      } else {
        atual = 0
      }
    }
  }
  return {
    atual,
    melhor,
    diasProtegidos: protegidos,
    escudoDisponivel: !escudoUsadoNaSemana.has(inicioDaSemana(hoje)),
  }
}
