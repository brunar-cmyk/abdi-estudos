import { useRef, useState } from 'react'
import { exportarJSON, importarJSON, progressoVazio } from '../lib/storage'
import { unidades } from '../lib/content'
import { useProgresso } from '../state'

export function Ajustes() {
  const { p, hoje, origem, aviso, atualizar, substituir } = useProgresso()
  const [msg, setMsg] = useState<string | null>(null)
  const arquivo = useRef<HTMLInputElement>(null)

  function exportar() {
    const blob = new Blob([exportarJSON(p)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `progresso-abdi-${hoje}.json`
    a.click()
    URL.revokeObjectURL(url)
    setMsg('Arquivo gerado. Guarde-o em um lugar seguro.')
  }

  async function importar(f: File | undefined) {
    if (!f) return
    try {
      const novo = importarJSON(await f.text())
      if (!window.confirm('Importar vai substituir o progresso atual neste aparelho. Continuar?')) return
      substituir(novo)
      setMsg('Progresso importado.')
    } catch (e) {
      setMsg(`Não foi possível importar: ${(e as Error).message}`)
    } finally {
      if (arquivo.current) arquivo.current.value = ''
    }
  }

  const numeros = unidades.flatMap((u) => (u.pacoteNumeros ?? []).map((n) => ({ ...n, unidade: u.titulo })))

  return (
    <section>
      <h2>Ajustes</h2>

      <label className="campo">
        Meta diária de XP
        <input
          type="number"
          min={10}
          max={300}
          step={5}
          value={p.metaDiaria}
          onChange={(e) => atualizar((x) => ({ ...x, metaDiaria: Math.max(10, Math.min(300, Number(e.target.value) || 30)) }))}
        />
      </label>
      <p className="muted">Uma lição completa rende de 10 a 40 XP. Um dia conta para a sequência ao atingir a meta.</p>

      <h3>Progresso no aparelho</h3>
      <p className="muted">
        Salvo em: {origem === 'indexeddb' ? 'IndexedDB' : origem === 'localstorage' ? 'localStorage' : 'somente memória (não está sendo salvo)'}.
      </p>
      {aviso && <div className="aviso">{aviso}</div>}
      <div className="linha">
        <button type="button" onClick={exportar}>Exportar JSON</button>
        <button type="button" onClick={() => arquivo.current?.click()}>Importar JSON</button>
        <input ref={arquivo} type="file" accept="application/json,.json" hidden onChange={(e) => importar(e.target.files?.[0])} />
      </div>
      {msg && <p role="status">{msg}</p>}

      <button
        type="button"
        className="perigo"
        onClick={() => {
          if (window.confirm('Apagar todo o progresso deste aparelho? Exporte antes se quiser guardar.')) substituir(progressoVazio(hoje))
        }}
      >
        Apagar progresso
      </button>

      <h3>Pacote de números</h3>
      {numeros.length === 0 ? <p className="muted">Ainda não há números cadastrados.</p> : (
        <table className="tabela">
          <thead><tr><th>Item</th><th>Valor</th><th>Fonte</th></tr></thead>
          <tbody>
            {numeros.map((n, k) => (
              <tr key={k}><td>{n.rotulo}</td><td>{n.valor}</td><td>{n.fonte}</td></tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  )
}
