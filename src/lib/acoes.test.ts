import { describe, expect, it } from 'vitest'
import { avaliarCarta, cartasVencidas, concluirLicao, registrarResposta } from './acoes'
import { progressoVazio } from './storage'

const HOJE = '2026-10-28'

describe('registrarResposta', () => {
  it('erro entra no caderno e agenda revisão para amanhã', () => {
    const p = registrarResposta(progressoVazio(HOJE), 'q1', false, HOJE)
    expect(p.caderno).toEqual(['q1'])
    expect(p.cartas['q:q1'].vence).toBe('2026-10-29')
    expect(cartasVencidas(p, HOJE)).toEqual([])
    expect(cartasVencidas(p, '2026-10-29')).toEqual(['q:q1'])
  })

  it('errar duas vezes não duplica no caderno', () => {
    let p = registrarResposta(progressoVazio(HOJE), 'q1', false, HOJE)
    p = registrarResposta(p, 'q1', false, HOJE)
    expect(p.caderno).toEqual(['q1'])
    expect(p.questoes.q1.erradas).toBe(2)
  })

  it('acerto fora do caderno só registra a estatística', () => {
    const p = registrarResposta(progressoVazio(HOJE), 'q2', true, HOJE)
    expect(p.caderno).toEqual([])
    expect(p.questoes.q2.certas).toBe(1)
  })
})

describe('avaliarCarta', () => {
  it('questão sai do caderno depois de dois acertos seguidos na revisão', () => {
    let p = registrarResposta(progressoVazio(HOJE), 'q1', false, HOJE) // repeticoes = 0
    p = avaliarCarta(p, 'q:q1', 4, '2026-10-29')
    expect(p.caderno).toEqual(['q1'])
    p = avaliarCarta(p, 'q:q1', 4, '2026-10-30')
    expect(p.caderno).toEqual([])
  })

  it('errar na revisão mantém no caderno', () => {
    let p = registrarResposta(progressoVazio(HOJE), 'q1', false, HOJE)
    p = avaliarCarta(p, 'q:q1', 4, '2026-10-29')
    p = avaliarCarta(p, 'q:q1', 1, '2026-10-30')
    p = avaliarCarta(p, 'q:q1', 4, '2026-10-31')
    expect(p.caderno).toEqual(['q1'])
  })
})

describe('concluirLicao', () => {
  it('paga XP cheio na primeira vez e menos nas repetições', () => {
    let p = concluirLicao(progressoVazio(HOJE), 'l1', 5, 6, HOJE)
    expect(p.xp).toBe(10 + 5 * 5)
    expect(p.xpPorDia[HOJE]).toBe(35)
    p = concluirLicao(p, 'l1', 6, 6, HOJE)
    expect(p.xp).toBe(35 + 5 + 12)
    expect(p.licoes.l1.acertos).toBe(6)
  })
})
