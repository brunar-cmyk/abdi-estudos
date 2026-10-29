import { somarDias } from './dates'

/** Revisão espaçada no estilo SM-2. Datas em "AAAA-MM-DD". */
export interface CartaSRS {
  facilidade: number
  intervalo: number // dias
  repeticoes: number
  vence: string
}

export type Nota = 0 | 1 | 2 | 3 | 4 | 5

export const FACILIDADE_INICIAL = 2.5
export const FACILIDADE_MINIMA = 1.3

export function novaCarta(hoje: string): CartaSRS {
  return { facilidade: FACILIDADE_INICIAL, intervalo: 0, repeticoes: 0, vence: hoje }
}

/** Nota abaixo de 3 reinicia a carta e ela volta amanhã. */
export function avaliar(carta: CartaSRS, nota: Nota, hoje: string): CartaSRS {
  const q = nota
  const facilidade = Math.max(
    FACILIDADE_MINIMA,
    carta.facilidade + 0.1 - (5 - q) * (0.08 + (5 - q) * 0.02),
  )
  if (q < 3) {
    return { facilidade, intervalo: 1, repeticoes: 0, vence: somarDias(hoje, 1) }
  }
  let intervalo: number
  if (carta.repeticoes === 0) intervalo = 1
  else if (carta.repeticoes === 1) intervalo = 6
  else intervalo = Math.round(carta.intervalo * facilidade)
  return {
    facilidade,
    intervalo,
    repeticoes: carta.repeticoes + 1,
    vence: somarDias(hoje, intervalo),
  }
}

export function estaVencida(carta: CartaSRS, hoje: string): boolean {
  return carta.vence <= hoje
}

/** Botões da tela: errei, difícil, fácil. */
export const NOTA_ERREI = 1 as const
export const NOTA_DIFICIL = 3 as const
export const NOTA_FACIL = 5 as const
