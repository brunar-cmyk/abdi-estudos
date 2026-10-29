import { describe, expect, it } from 'vitest'
import { COTAS_SIMULADO, pontuar, type Bloco, type RespostaProva } from './scoring'

function gerar(bloco: Bloco, n: number, acertos: number): RespostaProva[] {
  return Array.from({ length: n }, (_, i) => ({ bloco, correta: 2, marcada: i < acertos ? 2 : 0 }))
}

describe('pontuar', () => {
  it('a prova inteira certa vale 25 pontos (edital 9.2.1)', () => {
    const r = pontuar([...gerar('Gerais', 20, 20), ...gerar('Institucionais', 20, 20), ...gerar('Específicos', 20, 20)])
    expect(r.pontos).toBe(25)
    expect(r.acertos).toBe(60)
    expect(r.aprovado).toBe(true)
  })

  it('usa 0,3 para Gerais e Institucionais e 0,65 para Específicos', () => {
    const r = pontuar([...gerar('Gerais', 20, 10), ...gerar('Institucionais', 20, 5), ...gerar('Específicos', 20, 3)])
    expect(r.porBloco.Gerais.pontos).toBe(3)
    expect(r.porBloco.Institucionais.pontos).toBe(1.5)
    expect(r.porBloco.Específicos.pontos).toBe(1.95)
    expect(r.pontos).toBe(6.45)
  })

  it('não acumula erro de ponto flutuante', () => {
    // 7 acertos x 0,65 = 4,55 e 3 x 0,3 = 0,9
    const r = pontuar([...gerar('Específicos', 20, 7), ...gerar('Gerais', 20, 3)])
    expect(r.porBloco.Específicos.pontos).toBe(4.55)
    expect(r.porBloco.Gerais.pontos).toBe(0.9)
    expect(r.pontos).toBe(5.45)
  })

  it('exige no mínimo 30 acertos de 60', () => {
    const com29 = pontuar([...gerar('Gerais', 20, 10), ...gerar('Institucionais', 20, 10), ...gerar('Específicos', 20, 9)])
    const com30 = pontuar([...gerar('Gerais', 20, 10), ...gerar('Institucionais', 20, 10), ...gerar('Específicos', 20, 10)])
    expect(com29.minimoParaAprovar).toBe(30)
    expect(com29.aprovado).toBe(false)
    expect(com30.aprovado).toBe(true)
  })

  it('reprova quando zera um bloco, mesmo com mais de 30 acertos', () => {
    const r = pontuar([...gerar('Gerais', 20, 0), ...gerar('Institucionais', 20, 20), ...gerar('Específicos', 20, 20)])
    expect(r.acertos).toBe(40)
    expect(r.blocosZerados).toEqual(['Gerais'])
    expect(r.aprovado).toBe(false)
  })

  it('questão em branco vale zero', () => {
    const r = pontuar([{ bloco: 'Específicos', correta: 1, marcada: null }])
    expect(r.acertos).toBe(0)
    expect(r.pontos).toBe(0)
  })

  it('sem questões não aprova', () => {
    expect(pontuar([]).aprovado).toBe(false)
  })
})

describe('COTAS_SIMULADO', () => {
  it('soma 60 questões na proporção do edital', () => {
    const soma = (b: Bloco) =>
      Object.values(COTAS_SIMULADO).filter((c) => c.bloco === b).reduce((s, c) => s + c.quantidade, 0)
    expect(soma('Gerais')).toBe(20)
    expect(soma('Institucionais')).toBe(20)
    expect(soma('Específicos')).toBe(20)
    expect(COTAS_SIMULADO.lic.quantidade).toBe(8)
  })
})
