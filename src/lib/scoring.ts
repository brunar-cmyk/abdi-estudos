export type Bloco = 'Gerais' | 'Institucionais' | 'Específicos'

export const BLOCOS: Bloco[] = ['Gerais', 'Institucionais', 'Específicos']

/** Valor de cada questão em centésimos de ponto (evita erro de ponto flutuante). Edital 9.1 e 9.2.1. */
export const VALOR_CENTESIMOS: Record<Bloco, number> = {
  Gerais: 30,
  Institucionais: 30,
  Específicos: 65,
}

export interface RespostaProva {
  bloco: Bloco
  /** Índice da alternativa marcada (0 a 4); null se deixou em branco. */
  marcada: number | null
  correta: number
}

export interface ResumoBloco {
  total: number
  acertos: number
  pontos: number
}

export interface ResultadoProva {
  porBloco: Record<Bloco, ResumoBloco>
  totalQuestoes: number
  acertos: number
  pontos: number
  minimoParaAprovar: number
  blocosZerados: Bloco[]
  aprovado: boolean
}

/**
 * Edital 9.5: aprovado quem acerta pelo menos 50% das questões e não zera nenhuma área.
 * Edital 9.2.2: questão em branco (ou com mais de uma marcação) vale zero.
 */
export function pontuar(respostas: RespostaProva[]): ResultadoProva {
  const porBloco = Object.fromEntries(
    BLOCOS.map((b) => [b, { total: 0, acertos: 0, pontos: 0 }]),
  ) as Record<Bloco, ResumoBloco>
  const centesimos: Record<Bloco, number> = { Gerais: 0, Institucionais: 0, Específicos: 0 }

  for (const r of respostas) {
    const resumo = porBloco[r.bloco]
    resumo.total += 1
    if (r.marcada !== null && r.marcada === r.correta) {
      resumo.acertos += 1
      centesimos[r.bloco] += VALOR_CENTESIMOS[r.bloco]
    }
  }
  for (const b of BLOCOS) porBloco[b].pontos = centesimos[b] / 100

  const totalQuestoes = respostas.length
  const acertos = BLOCOS.reduce((s, b) => s + porBloco[b].acertos, 0)
  const pontos = BLOCOS.reduce((s, b) => s + centesimos[b], 0) / 100
  const minimoParaAprovar = Math.ceil(totalQuestoes / 2)
  const blocosZerados = BLOCOS.filter((b) => porBloco[b].total > 0 && porBloco[b].acertos === 0)

  return {
    porBloco,
    totalQuestoes,
    acertos,
    pontos,
    minimoParaAprovar,
    blocosZerados,
    aprovado: totalQuestoes > 0 && acertos >= minimoParaAprovar && blocosZerados.length === 0,
  }
}

/** Distribuição de questões do simulado (edital 9.1): 60 no total. */
export const COTAS_SIMULADO: Record<string, { bloco: Bloco; quantidade: number; rotulo: string }> = {
  port: { bloco: 'Gerais', quantidade: 8, rotulo: 'Língua Portuguesa' },
  rl: { bloco: 'Gerais', quantidade: 6, rotulo: 'Raciocínio Lógico' },
  info: { bloco: 'Gerais', quantidade: 6, rotulo: 'Noções de Informática' },
  sss: { bloco: 'Institucionais', quantidade: 4, rotulo: 'Serviços sociais autônomos' },
  lei: { bloco: 'Institucionais', quantidade: 4, rotulo: 'Lei, decreto e Estatuto' },
  lic: { bloco: 'Institucionais', quantidade: 8, rotulo: 'Licitações e convênios' },
  etica: { bloco: 'Institucionais', quantidade: 4, rotulo: 'Ética e missão institucional' },
  esp: { bloco: 'Específicos', quantidade: 20, rotulo: 'Comunicação e Marketing' },
}

export const DURACAO_SIMULADO_MIN = 210 // 13h30 às 17h00
