// Confere todo o conteúdo em content/. Uso: npm run validate  (ou validate:strict)
// Erros (exit 1): estrutura quebrada, questão sem 5 alternativas / sem 1 correta / sem explicação / sem fonte.
// Cobertura de tópicos do syllabus: aviso, e erro com --strict.
import { readFileSync, readdirSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const raiz = join(dirname(fileURLToPath(import.meta.url)), '..')
const strict = process.argv.includes('--strict')
const erros = []
const avisos = []
const err = (m) => erros.push(m)
const warn = (m) => avisos.push(m)

function ler(caminho) {
  try {
    return JSON.parse(readFileSync(join(raiz, caminho), 'utf8'))
  } catch (e) {
    err(`${caminho}: não consegui ler (${e.message})`)
    return null
  }
}

const BLOCOS = ['Gerais', 'Institucionais', 'Específicos']
const CATEGORIAS = { port: 'Gerais', rl: 'Gerais', info: 'Gerais', sss: 'Institucionais', lei: 'Institucionais', lic: 'Institucionais', etica: 'Institucionais', esp: 'Específicos' }
// Regra da usuária para qualquer texto dela: sem emoji, sem travessão, sem setas decorativas.
const PROIBIDO = /[—–]|[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]|[↗→←↑↓]/u

const texto = (v) => typeof v === 'string' && v.trim().length > 0

function checarEstilo(onde, t) {
  if (typeof t === 'string' && PROIBIDO.test(t)) err(`${onde}: contém travessão, emoji ou seta (${JSON.stringify(t.match(PROIBIDO)[0])})`)
}

const syllabus = ler('content/syllabus.json')
const topicos = new Map((syllabus?.topicos ?? []).map((t) => [t.id, t]))
if (topicos.size === 0) err('content/syllabus.json: sem tópicos')
for (const t of topicos.values()) {
  if (!BLOCOS.includes(t.bloco) || !texto(t.texto_edital) || typeof t.valor_questao !== 'number') err(`syllabus ${t.id}: campos inválidos`)
}
ler('content/dates.json')
ler('content/sources.json')

const arquivos = readdirSync(join(raiz, 'content/units')).filter((f) => f.endsWith('.json')).sort()
const idsUnidade = new Set()
const idsLicao = new Set()
const idsQuestao = new Set()
const cobertos = new Set()
const posicoes = [0, 0, 0, 0, 0]
let nQuestoes = 0
let nLicoes = 0
const porCategoria = {}

for (const arq of arquivos) {
  const u = ler(`content/units/${arq}`)
  if (!u) continue
  const o = `unidade ${u.id ?? arq}`
  if (!texto(u.id) || `${u.id}.json` !== arq) err(`${arq}: id deve ser igual ao nome do arquivo`)
  if (idsUnidade.has(u.id)) err(`${o}: id repetido`)
  idsUnidade.add(u.id)
  if (!texto(u.titulo)) err(`${o}: sem título`)
  if (!(u.categoria in CATEGORIAS)) err(`${o}: categoria inválida`)
  else if (CATEGORIAS[u.categoria] !== u.bloco) err(`${o}: categoria ${u.categoria} não pertence ao bloco ${u.bloco}`)
  if (!Array.isArray(u.topicos) || u.topicos.length === 0) err(`${o}: sem tópicos do syllabus`)
  for (const t of u.topicos ?? []) {
    if (!topicos.has(t)) err(`${o}: tópico ${t} não existe em syllabus.json`)
    else cobertos.add(t)
  }
  for (const n of u.pacoteNumeros ?? []) {
    if (!texto(n.rotulo) || !texto(n.valor) || !texto(n.fonte)) err(`${o}: item do pacote de números incompleto`)
    for (const k of ['rotulo', 'valor', 'fonte']) checarEstilo(`${o} pacote`, n[k])
  }
  if (!Array.isArray(u.licoes) || u.licoes.length === 0) err(`${o}: sem lições`)

  for (const l of u.licoes ?? []) {
    nLicoes++
    const lo = `lição ${l.id}`
    if (!texto(l.id) || idsLicao.has(l.id)) err(`${o}: id de lição vazio ou repetido (${l.id})`)
    idsLicao.add(l.id)
    if (!texto(l.titulo)) err(`${lo}: sem título`)
    if (!(l.minutos >= 5 && l.minutos <= 10)) err(`${lo}: minutos deve ficar entre 5 e 10`)
    if (!Array.isArray(l.resumo) || l.resumo.length < 3 || l.resumo.length > 6 || !l.resumo.every(texto)) err(`${lo}: resumo precisa de 3 a 6 tópicos`)
    if (!Array.isArray(l.flashcards) || l.flashcards.length < 2 || l.flashcards.length > 4) err(`${lo}: precisa de 2 a 4 flashcards`)
    for (const f of l.flashcards ?? []) if (!texto(f.frente) || !texto(f.verso)) err(`${lo}: flashcard incompleto`)
    if (!Array.isArray(l.questoes) || l.questoes.length < 4 || l.questoes.length > 8) err(`${lo}: precisa de 4 a 8 questões`)
    for (const t of [...(l.resumo ?? []), l.titulo]) checarEstilo(lo, t)
    for (const f of l.flashcards ?? []) { checarEstilo(lo, f.frente); checarEstilo(lo, f.verso) }

    for (const q of l.questoes ?? []) {
      nQuestoes++
      porCategoria[u.categoria] = (porCategoria[u.categoria] ?? 0) + 1
      const qo = `questão ${q.id}`
      if (!texto(q.id) || idsQuestao.has(q.id)) err(`${lo}: id de questão vazio ou repetido (${q.id})`)
      idsQuestao.add(q.id)
      if (!String(q.id).startsWith(`${l.id}-`)) err(`${qo}: id deve começar com "${l.id}-"`)
      if (!texto(q.enunciado)) err(`${qo}: sem enunciado`)
      if (!Array.isArray(q.alternativas) || q.alternativas.length !== 5 || !q.alternativas.every(texto)) err(`${qo}: precisa de exatamente 5 alternativas preenchidas`)
      else if (new Set(q.alternativas.map((a) => a.trim().toLowerCase())).size !== 5) err(`${qo}: alternativas repetidas`)
      if (!Number.isInteger(q.correta) || q.correta < 0 || q.correta > 4) err(`${qo}: "correta" deve ser um índice de 0 a 4 (exatamente uma correta)`)
      else posicoes[q.correta]++
      if (!texto(q.explicacao)) err(`${qo}: sem explicação`)
      if (!texto(q.fonte)) err(`${qo}: sem fonte`)
      if (q.topico && !topicos.has(q.topico)) err(`${qo}: tópico ${q.topico} não existe`)
      checarEstilo(qo, q.enunciado); checarEstilo(qo, q.explicacao); checarEstilo(qo, q.fonte)
      for (const a of q.alternativas ?? []) checarEstilo(qo, a)
      if (/\b(alternativa|letra|item)\s+[A-E]\b/i.test(q.explicacao ?? '')) warn(`${qo}: a explicação cita letra de alternativa (o app não fixa a ordem)`)
    }
  }
}

// Equilíbrio do gabarito
if (nQuestoes >= 20) {
  const max = Math.max(...posicoes)
  if (max / nQuestoes > 0.35) warn(`gabarito desequilibrado: posições A..E = ${posicoes.join(', ')}`)
}

// Calendário
const cal = ler('content/schedule.json')
for (const s of cal?.semanas ?? []) {
  for (const id of [...(s.unidades ?? []), ...(s.gerais ?? [])]) {
    if (!idsUnidade.has(id)) warn(`semana ${s.n}: unidade "${id}" ainda sem arquivo em content/units`)
  }
}

// Cobertura do syllabus
const semLicao = [...topicos.keys()].filter((t) => !cobertos.has(t))
const msgCobertura = `${semLicao.length} de ${topicos.size} tópicos do syllabus ainda sem lição: ${semLicao.join(', ')}`
if (semLicao.length) (strict ? err : warn)(msgCobertura)

console.log(`Unidades: ${idsUnidade.size} | lições: ${nLicoes} | questões: ${nQuestoes} ${JSON.stringify(porCategoria)}`)
for (const a of avisos) console.log(`AVISO  ${a}`)
for (const e of erros) console.log(`ERRO   ${e}`)
if (erros.length) {
  console.log(`\n${erros.length} erro(s).`)
  process.exit(1)
}
console.log(`\nConteúdo válido${avisos.length ? ` (${avisos.length} aviso(s))` : ''}.`)
