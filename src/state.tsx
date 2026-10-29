import { createContext, useCallback, useContext, useEffect, useRef, useState, type ReactNode } from 'react'
import { hojeISO } from './lib/dates'
import { carregar, progressoVazio, salvar, type OrigemArmazenamento, type Progresso } from './lib/storage'

interface Contexto {
  p: Progresso
  hoje: string
  pronto: boolean
  origem: OrigemArmazenamento
  aviso?: string
  atualizar: (fn: (p: Progresso) => Progresso) => void
  substituir: (p: Progresso) => void
}

const Ctx = createContext<Contexto | null>(null)

export function ProgressoProvider({ children }: { children: ReactNode }) {
  const [p, setP] = useState<Progresso>(() => progressoVazio(hojeISO()))
  const [pronto, setPronto] = useState(false)
  const [origem, setOrigem] = useState<OrigemArmazenamento>('indexeddb')
  const [aviso, setAviso] = useState<string | undefined>()
  const carregou = useRef(false)

  useEffect(() => {
    carregar().then((r) => {
      if (r.progresso) setP(r.progresso)
      setOrigem(r.origem)
      setAviso(r.aviso)
      carregou.current = true
      setPronto(true)
    })
  }, [])

  useEffect(() => {
    if (!carregou.current) return
    const t = setTimeout(() => {
      salvar(p).then((r) => {
        setOrigem(r.origem)
        setAviso(r.erro)
      })
    }, 300)
    return () => clearTimeout(t)
  }, [p])

  const atualizar = useCallback((fn: (p: Progresso) => Progresso) => setP(fn), [])
  const substituir = useCallback((novo: Progresso) => setP(novo), [])

  return (
    <Ctx.Provider value={{ p, hoje: hojeISO(), pronto, origem, aviso, atualizar, substituir }}>
      {children}
    </Ctx.Provider>
  )
}

export function useProgresso(): Contexto {
  const c = useContext(Ctx)
  if (!c) throw new Error('useProgresso fora do ProgressoProvider')
  return c
}
