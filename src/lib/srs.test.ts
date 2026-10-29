import { describe, expect, it } from 'vitest'
import { avaliar, estaVencida, FACILIDADE_MINIMA, novaCarta } from './srs'

const HOJE = '2026-10-28'

describe('avaliar (SM-2)', () => {
  it('acertos seguidos espaçam 1, 6 e depois intervalo x facilidade', () => {
    let c = novaCarta(HOJE)
    c = avaliar(c, 5, HOJE)
    expect(c.intervalo).toBe(1)
    expect(c.vence).toBe('2026-10-29')
    c = avaliar(c, 5, '2026-10-29')
    expect(c.intervalo).toBe(6)
    expect(c.vence).toBe('2026-11-04')
    const antes = c
    c = avaliar(c, 5, '2026-11-04')
    expect(c.intervalo).toBe(Math.round(antes.intervalo * c.facilidade))
    expect(c.repeticoes).toBe(3)
  })

  it('nota 5 sobe a facilidade e nota 3 desce', () => {
    const base = novaCarta(HOJE)
    expect(avaliar(base, 5, HOJE).facilidade).toBeCloseTo(2.6, 5)
    expect(avaliar(base, 3, HOJE).facilidade).toBeCloseTo(2.36, 5)
  })

  it('erro reinicia as repetições e volta amanhã', () => {
    let c = novaCarta(HOJE)
    c = avaliar(c, 5, HOJE)
    c = avaliar(c, 5, '2026-10-29')
    c = avaliar(c, 1, '2026-11-04')
    expect(c.repeticoes).toBe(0)
    expect(c.intervalo).toBe(1)
    expect(c.vence).toBe('2026-11-05')
  })

  it('a facilidade nunca passa do mínimo de 1,3', () => {
    let c = novaCarta(HOJE)
    for (let i = 0; i < 20; i++) c = avaliar(c, 0, HOJE)
    expect(c.facilidade).toBe(FACILIDADE_MINIMA)
  })
})

describe('estaVencida', () => {
  it('vence no dia marcado e depois', () => {
    const c = { ...novaCarta(HOJE), vence: '2026-10-30' }
    expect(estaVencida(c, '2026-10-29')).toBe(false)
    expect(estaVencida(c, '2026-10-30')).toBe(true)
    expect(estaVencida(c, '2026-11-02')).toBe(true)
  })
})
