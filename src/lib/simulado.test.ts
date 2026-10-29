import { describe, expect, it } from 'vitest'
import { COTAS_SIMULADO } from './scoring'
import { montarSimulado, type ItemBanco } from './simulado'
import type { Categoria } from './types'

function banco(porCategoria: Partial<Record<Categoria, number>>): ItemBanco[] {
  return Object.entries(porCategoria).flatMap(([cat, n]) =>
    Array.from({ length: n as number }, (_, i) => ({
      id: `${cat}-${i}`,
      categoria: cat as Categoria,
      bloco: COTAS_SIMULADO[cat].bloco,
    })),
  )
}

describe('montarSimulado', () => {
  it('com banco cheio monta 60 questões sem faltas e sem repetir', () => {
    const b = banco({ port: 20, rl: 20, info: 20, sss: 20, lei: 20, lic: 20, etica: 20, esp: 40 })
    const m = montarSimulado(b)
    expect(m.ids).toHaveLength(60)
    expect(new Set(m.ids).size).toBe(60)
    expect(m.faltas).toEqual([])
    expect(m.ids.filter((id) => id.startsWith('lic-'))).toHaveLength(8)
    expect(m.ids.filter((id) => id.startsWith('esp-'))).toHaveLength(20)
  })

  it('com banco incompleto usa o que há e informa a falta', () => {
    const m = montarSimulado(banco({ esp: 12, lic: 3 }))
    expect(m.ids).toHaveLength(15)
    const lic = m.faltas.find((f) => f.categoria === 'lic')
    const esp = m.faltas.find((f) => f.categoria === 'esp')
    expect(lic?.faltam).toBe(5)
    expect(esp?.faltam).toBe(8)
    expect(m.faltas).toHaveLength(8)
  })
})
