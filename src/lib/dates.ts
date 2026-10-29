// Datas como texto "AAAA-MM-DD" no horário local, para evitar problemas de fuso.

export function hojeISO(agora: Date = new Date()): string {
  const y = agora.getFullYear()
  const m = String(agora.getMonth() + 1).padStart(2, '0')
  const d = String(agora.getDate()).padStart(2, '0')
  return `${y}-${m}-${d}`
}

function paraUTC(iso: string): number {
  const [y, m, d] = iso.split('-').map(Number)
  return Date.UTC(y, m - 1, d)
}

export function somarDias(iso: string, dias: number): string {
  const dt = new Date(paraUTC(iso) + dias * 86_400_000)
  return `${dt.getUTCFullYear()}-${String(dt.getUTCMonth() + 1).padStart(2, '0')}-${String(dt.getUTCDate()).padStart(2, '0')}`
}

/** Diferença em dias (b - a). */
export function diffDias(a: string, b: string): number {
  return Math.round((paraUTC(b) - paraUTC(a)) / 86_400_000)
}

/** Segunda-feira da semana que contém a data. */
export function inicioDaSemana(iso: string): string {
  const dow = new Date(paraUTC(iso)).getUTCDay() // 0 = domingo
  return somarDias(iso, -((dow + 6) % 7))
}

export function formatarData(iso: string): string {
  const [y, m, d] = iso.split('-')
  return `${d}/${m}/${y}`
}
