import { avaliar, estaVencida, novaCarta, type Nota } from './srs'
import type { Progresso, ResultadoSalvo } from './storage'

export const XP_LICAO_BASE = 10
export const XP_POR_ACERTO = 5

export function darXp(p: Progresso, xp: number, hoje: string): Progresso {
  return { ...p, xp: p.xp + xp, xpPorDia: { ...p.xpPorDia, [hoje]: (p.xpPorDia[hoje] ?? 0) + xp } }
}

/** Primeira conclusão paga XP cheio; repetir a lição paga menos, para não virar caminho fácil. */
export function concluirLicao(p: Progresso, id: string, acertos: number, total: number, hoje: string): Progresso {
  const repetida = id in p.licoes
  const xp = repetida ? 5 + 2 * acertos : XP_LICAO_BASE + XP_POR_ACERTO * acertos
  const anterior = p.licoes[id]
  const melhor = anterior && anterior.acertos > acertos ? anterior : { data: hoje, acertos, total }
  return darXp({ ...p, licoes: { ...p.licoes, [id]: melhor } }, xp, hoje)
}

/** Registra uma resposta. Errar leva a questão ao caderno e agenda revisão para amanhã. */
export function registrarResposta(p: Progresso, questaoId: string, certa: boolean, hoje: string): Progresso {
  const antes = p.questoes[questaoId] ?? { certas: 0, erradas: 0, ultimaCerta: false, data: hoje }
  const questoes = {
    ...p.questoes,
    [questaoId]: {
      certas: antes.certas + (certa ? 1 : 0),
      erradas: antes.erradas + (certa ? 0 : 1),
      ultimaCerta: certa,
      data: hoje,
    },
  }
  if (certa) return { ...p, questoes }
  const idCarta = `q:${questaoId}`
  const carta = avaliar(p.cartas[idCarta] ?? novaCarta(hoje), 1, hoje)
  return {
    ...p,
    questoes,
    cartas: { ...p.cartas, [idCarta]: carta },
    caderno: p.caderno.includes(questaoId) ? p.caderno : [...p.caderno, questaoId],
  }
}

/** Avalia uma carta (flashcard ou questão do caderno). Questão do caderno sai depois de 2 acertos seguidos. */
export function avaliarCarta(p: Progresso, id: string, nota: Nota, hoje: string): Progresso {
  const carta = avaliar(p.cartas[id] ?? novaCarta(hoje), nota, hoje)
  let caderno = p.caderno
  if (id.startsWith('q:') && nota >= 3 && carta.repeticoes >= 2) {
    caderno = caderno.filter((q) => q !== id.slice(2))
  }
  const comXp = nota >= 3 ? darXp(p, nota === 5 ? 2 : 1, hoje) : p
  return { ...comXp, cartas: { ...comXp.cartas, [id]: carta }, caderno }
}

export function cartasVencidas(p: Progresso, hoje: string): string[] {
  return Object.entries(p.cartas)
    .filter(([, c]) => estaVencida(c, hoje))
    .map(([id]) => id)
    .sort()
}

export function guardarSimulado(p: Progresso, r: ResultadoSalvo, hoje: string): Progresso {
  return darXp({ ...p, simulados: [...p.simulados, r], simuladoAtual: null }, r.total, hoje)
}
