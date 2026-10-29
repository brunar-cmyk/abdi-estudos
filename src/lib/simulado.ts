import { COTAS_SIMULADO, type Bloco } from './scoring'
import type { Categoria } from './types'

export interface ItemBanco {
  id: string
  categoria: Categoria
  bloco: Bloco
}

export interface Montagem {
  ids: string[]
  /** Quanto faltou em cada categoria em relação ao edital. */
  faltas: Array<{ categoria: string; rotulo: string; faltam: number }>
}

function embaralhar<T>(lista: T[], aleatorio: () => number): T[] {
  const a = [...lista]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(aleatorio() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

/**
 * Sorteia as questões na proporção da prova (8/6/6, 4/4/8/4 e 20).
 * Se uma categoria tiver menos questões do que a cota, usa todas e informa a falta.
 * A ordem final agrupa por bloco: Gerais, Institucionais, Específicos.
 */
export function montarSimulado(banco: ItemBanco[], aleatorio: () => number = Math.random): Montagem {
  const ids: string[] = []
  const faltas: Montagem['faltas'] = []
  for (const [categoria, cota] of Object.entries(COTAS_SIMULADO)) {
    const doBloco = banco.filter((q) => q.categoria === categoria)
    const sorteadas = embaralhar(doBloco, aleatorio).slice(0, cota.quantidade)
    ids.push(...sorteadas.map((q) => q.id))
    if (sorteadas.length < cota.quantidade) {
      faltas.push({ categoria, rotulo: cota.rotulo, faltam: cota.quantidade - sorteadas.length })
    }
  }
  return { ids, faltas }
}
