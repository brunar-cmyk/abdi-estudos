import type { CartaSRS } from './srs'

/** Tudo que fica salvo no aparelho. Sem login, sem servidor. */
export interface Progresso {
  versao: 1
  criadoEm: string
  metaDiaria: number
  xp: number
  xpPorDia: Record<string, number>
  licoes: Record<string, { data: string; acertos: number; total: number }>
  cartas: Record<string, CartaSRS> // "fc:<licao>:<n>" ou "q:<questao>"
  /** Resultado da última tentativa de cada questão. */
  questoes: Record<string, { certas: number; erradas: number; ultimaCerta: boolean; data: string }>
  /** Questões erradas que ainda não foram acertadas de novo. */
  caderno: string[]
  simulados: ResultadoSalvo[]
  simuladoAtual: SimuladoEmAndamento | null
}

export interface ResultadoSalvo {
  data: string
  acertos: number
  total: number
  pontos: number
  aprovado: boolean
  porBloco: Record<string, { acertos: number; total: number; pontos: number }>
}

export interface SimuladoEmAndamento {
  iniciadoEm: number // epoch ms
  ids: string[]
  respostas: Record<string, number | null>
}

export function progressoVazio(hoje: string): Progresso {
  return {
    versao: 1,
    criadoEm: hoje,
    metaDiaria: 30,
    xp: 0,
    xpPorDia: {},
    licoes: {},
    cartas: {},
    questoes: {},
    caderno: [],
    simulados: [],
    simuladoAtual: null,
  }
}

const NOME_DB = 'abdi-estudos'
const LOJA = 'kv'
const CHAVE = 'progresso'
const CHAVE_LS = 'abdi-estudos:progresso'

export type OrigemArmazenamento = 'indexeddb' | 'localstorage' | 'memoria'

function abrirDB(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    if (typeof indexedDB === 'undefined') return reject(new Error('IndexedDB indisponível'))
    const req = indexedDB.open(NOME_DB, 1)
    req.onupgradeneeded = () => req.result.createObjectStore(LOJA)
    req.onsuccess = () => resolve(req.result)
    req.onerror = () => reject(req.error ?? new Error('Falha ao abrir o IndexedDB'))
    req.onblocked = () => reject(new Error('IndexedDB bloqueado'))
  })
}

async function lerDB(): Promise<unknown> {
  const db = await abrirDB()
  try {
    return await new Promise((resolve, reject) => {
      const r = db.transaction(LOJA, 'readonly').objectStore(LOJA).get(CHAVE)
      r.onsuccess = () => resolve(r.result)
      r.onerror = () => reject(r.error)
    })
  } finally {
    db.close()
  }
}

async function gravarDB(p: Progresso): Promise<void> {
  const db = await abrirDB()
  try {
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction(LOJA, 'readwrite')
      tx.objectStore(LOJA).put(p, CHAVE)
      tx.oncomplete = () => resolve()
      tx.onerror = () => reject(tx.error)
      tx.onabort = () => reject(tx.error ?? new Error('Transação cancelada'))
    })
  } finally {
    db.close()
  }
}

/** Confere o formato mínimo antes de aceitar dados vindos do disco ou de um arquivo importado. */
export function validarProgresso(x: unknown): Progresso {
  if (!x || typeof x !== 'object') throw new Error('Arquivo inválido: não é um objeto.')
  const o = x as Record<string, unknown>
  if (o.versao !== 1) throw new Error('Versão de progresso não suportada.')
  const objetos = ['xpPorDia', 'licoes', 'cartas', 'questoes']
  for (const k of objetos) {
    if (!o[k] || typeof o[k] !== 'object' || Array.isArray(o[k])) throw new Error(`Campo "${k}" inválido.`)
  }
  if (!Array.isArray(o.caderno) || !Array.isArray(o.simulados)) throw new Error('Campos de lista inválidos.')
  if (typeof o.xp !== 'number' || typeof o.metaDiaria !== 'number') throw new Error('XP ou meta inválidos.')
  const base = o as unknown as Progresso
  return { ...base, simuladoAtual: base.simuladoAtual ?? null }
}

export interface Carregado {
  progresso: Progresso | null
  origem: OrigemArmazenamento
  aviso?: string
}

export async function carregar(): Promise<Carregado> {
  const avisos: string[] = []
  try {
    const v = await lerDB()
    if (v) return { progresso: validarProgresso(v), origem: 'indexeddb' }
    // pode haver dados antigos só no localStorage (fallback anterior)
    const ls = lerLS(avisos)
    return { progresso: ls, origem: 'indexeddb', aviso: avisos[0] }
  } catch (e) {
    avisos.push(`IndexedDB falhou (${(e as Error).message}); usando localStorage.`)
  }
  const ls = lerLS(avisos)
  return { progresso: ls, origem: 'localstorage', aviso: avisos.join(' ') }
}

function lerLS(avisos: string[]): Progresso | null {
  try {
    const bruto = localStorage.getItem(CHAVE_LS)
    return bruto ? validarProgresso(JSON.parse(bruto)) : null
  } catch (e) {
    avisos.push(`Não foi possível ler o localStorage (${(e as Error).message}).`)
    return null
  }
}

/** Grava no IndexedDB; se falhar, tenta o localStorage; se também falhar, avisa. */
export async function salvar(p: Progresso): Promise<{ origem: OrigemArmazenamento; erro?: string }> {
  try {
    await gravarDB(p)
    return { origem: 'indexeddb' }
  } catch (e1) {
    try {
      localStorage.setItem(CHAVE_LS, JSON.stringify(p))
      return { origem: 'localstorage', erro: `IndexedDB falhou: ${(e1 as Error).message}` }
    } catch (e2) {
      return {
        origem: 'memoria',
        erro: `Não consegui salvar no aparelho (${(e2 as Error).message}). Exporte o progresso para não perder.`,
      }
    }
  }
}

export function exportarJSON(p: Progresso): string {
  return JSON.stringify(p, null, 2)
}

export function importarJSON(texto: string): Progresso {
  let bruto: unknown
  try {
    bruto = JSON.parse(texto)
  } catch {
    throw new Error('O arquivo não é um JSON válido.')
  }
  return validarProgresso(bruto)
}
