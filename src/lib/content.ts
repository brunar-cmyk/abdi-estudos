import syllabusJson from '../../content/syllabus.json'
import datesJson from '../../content/dates.json'
import scheduleJson from '../../content/schedule.json'
import type { Licao, Questao, SemanaPlano, TopicoSyllabus, Unidade } from './types'

const modulos = import.meta.glob('../../content/units/*.json', { eager: true, import: 'default' })

export const unidades: Unidade[] = (Object.values(modulos) as Unidade[]).sort((a, b) =>
  a.id.localeCompare(b.id),
)
export const syllabus = syllabusJson.topicos as TopicoSyllabus[]
export const semanas = scheduleJson.semanas as SemanaPlano[]
export const eventos = datesJson.eventos as Array<{
  id: string
  texto: string
  data?: string
  inicio?: string
  fim?: string
}>

export const PROVA_ISO = '2026-12-20T13:30:00-03:00'

export function unidadePorId(id: string): Unidade | undefined {
  return unidades.find((u) => u.id === id)
}

export interface QuestaoCompleta extends Questao {
  unidade: Unidade
  licao: Licao
  topicoId: string
}

export function todasQuestoes(): QuestaoCompleta[] {
  return unidades.flatMap((u) =>
    u.licoes.flatMap((l) =>
      l.questoes.map((q) => ({ ...q, unidade: u, licao: l, topicoId: q.topico ?? u.topicos[0] })),
    ),
  )
}

export function questaoPorId(id: string): QuestaoCompleta | undefined {
  return todasQuestoes().find((q) => q.id === id)
}

export function licaoPorId(id: string): { unidade: Unidade; licao: Licao } | undefined {
  for (const u of unidades) {
    const licao = u.licoes.find((l) => l.id === id)
    if (licao) return { unidade: u, licao }
  }
  return undefined
}

export function semanaDe(hoje: string): SemanaPlano | undefined {
  return (
    semanas.find((s) => hoje >= s.inicio && hoje <= s.fim) ??
    (hoje < semanas[0].inicio ? semanas[0] : undefined)
  )
}
