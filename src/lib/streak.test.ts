import { describe, expect, it } from 'vitest'
import { diffDias, inicioDaSemana, somarDias } from './dates'
import { calcularSequencia } from './streak'

const META = 30

describe('datas', () => {
  it('soma dias atravessando o mês e o ano', () => {
    expect(somarDias('2026-10-31', 1)).toBe('2026-11-01')
    expect(somarDias('2026-12-31', 1)).toBe('2027-01-01')
    expect(diffDias('2026-10-28', '2026-12-20')).toBe(53)
  })
  it('a semana começa na segunda', () => {
    expect(inicioDaSemana('2026-10-28')).toBe('2026-10-26') // quarta
    expect(inicioDaSemana('2026-11-01')).toBe('2026-10-26') // domingo
    expect(inicioDaSemana('2026-10-26')).toBe('2026-10-26')
  })
})

describe('calcularSequencia', () => {
  it('conta dias seguidos que atingiram a meta', () => {
    const xp = { '2026-10-26': 40, '2026-10-27': 30, '2026-10-28': 35 }
    expect(calcularSequencia(xp, META, '2026-10-28').atual).toBe(3)
  })

  it('hoje ainda aberto não quebra a sequência', () => {
    const xp = { '2026-10-26': 40, '2026-10-27': 30 }
    expect(calcularSequencia(xp, META, '2026-10-28').atual).toBe(2)
  })

  it('XP abaixo da meta não conta o dia', () => {
    const xp = { '2026-10-26': 40, '2026-10-27': 29 }
    const s = calcularSequencia(xp, META, '2026-10-28')
    expect(s.atual).toBe(1) // segunda cumprida; terça protegida pelo escudo
  })

  it('o escudo cobre um dia perdido por semana', () => {
    const xp = { '2026-10-26': 40, '2026-10-28': 40 } // terça perdida
    const s = calcularSequencia(xp, META, '2026-10-28')
    expect(s.atual).toBe(2)
    expect(s.diasProtegidos).toEqual(['2026-10-27'])
    expect(s.escudoDisponivel).toBe(false)
  })

  it('dois dias perdidos na mesma semana quebram a sequência', () => {
    const xp = { '2026-10-26': 40, '2026-10-29': 40 } // terça e quarta perdidas
    const s = calcularSequencia(xp, META, '2026-10-29')
    expect(s.atual).toBe(1)
    expect(s.melhor).toBe(1)
  })

  it('o escudo volta a ficar disponível na semana seguinte', () => {
    // sexta cumprida; sábado perdido (escudo), domingo perdido (sem escudo): zera; segunda recomeça
    const xp = { '2026-10-30': 40, '2026-11-02': 40 }
    const s = calcularSequencia(xp, META, '2026-11-02')
    expect(s.atual).toBe(1)
    expect(s.escudoDisponivel).toBe(true)
  })

  it('sem nenhum dia cumprido a sequência é zero', () => {
    expect(calcularSequencia({}, META, '2026-10-28').atual).toBe(0)
  })
})
