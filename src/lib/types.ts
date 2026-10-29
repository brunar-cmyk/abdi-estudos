import type { Bloco } from './scoring'

export type Categoria = 'port' | 'rl' | 'info' | 'sss' | 'lei' | 'lic' | 'etica' | 'esp'

export interface Questao {
  id: string
  enunciado: string
  alternativas: string[] // sempre 5
  correta: number // 0 a 4
  explicacao: string
  fonte: string
  /** Opcional: tópico do syllabus; se faltar, vale o primeiro tópico da unidade. */
  topico?: string
}

export interface Flashcard {
  frente: string
  verso: string
}

export interface Licao {
  id: string
  titulo: string
  minutos: number
  resumo: string[]
  flashcards: Flashcard[]
  questoes: Questao[]
}

export interface NumeroChave {
  rotulo: string
  valor: string
  fonte: string
}

export interface Unidade {
  id: string
  titulo: string
  bloco: Bloco
  categoria: Categoria
  topicos: string[]
  pacoteNumeros?: NumeroChave[]
  licoes: Licao[]
}

export interface SemanaPlano {
  n: number
  inicio: string
  fim: string
  modo: 'estudo' | 'revisao'
  titulo: string
  unidades: string[]
  /** Conhecimentos Gerais, que seguem em paralelo. */
  gerais: string[]
}

export interface TopicoSyllabus {
  id: string
  bloco: Bloco
  disciplina: string
  item: number
  questoes_disciplina: number
  valor_questao: number
  texto_edital: string
}
