"""Gera content/syllabus.json a partir do texto extraído do Edital 01/2026 (Anexo II)."""
import json, re, sys

src, out = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().split("\n")

def block(a, b):
    t = " ".join(l.strip() for l in lines[a - 1:b] if l.strip() and not l.startswith("=====") and not re.search(r"INDUSTRIAL . ABDI \d+\s*$", l))
    t = re.sub(r"\s+", " ", t)
    return t

# artefatos de extração do PDF (palavras partidas); só corrige o que foi conferido
FIX = {
    "Legisla ção": "Legislação", "reput ação": "reputação", "tex to": "texto",
    "aplica das": "aplicadas", "Reescrit a": "Reescrita", "prime ira": "primeira",
    "tra balho": "trabalho", "armazenamento, organização": "armazenamento, organização",
    "Lei nº 11.080/2004, art. 1º, § 1º": "Lei nº 11.080/2004, art. 1º, § 1º",
    "L ei": "Lei", "sust entabilidade": "sustentabilidade", "confo rme": "conforme",
    "For malização": "Formalização", "Diretoria -Executiva": "Diretoria-Executiva", "2024 –2029": "2024–2029", "habili tação": "habilitação",
}
def fix(t):
    for k, v in FIX.items():
        t = t.replace(k, v)
    return t

def split_items(text, n, header_re=None):
    """Divide em n itens numerados sequencialmente (1, 2, ... n)."""
    pos, starts = 0, []
    for i in range(1, n + 1):
        m = re.compile(r"(?:(?<=\s)|^)%d\.? (?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])" % i).search(text, pos)
        if not m:
            raise SystemExit(f"item {i} não encontrado")
        starts.append(m.start()); pos = m.end()
    starts.append(len(text))
    return [fix(text[starts[i]:starts[i + 1]].strip()) for i in range(n)]

topics = []
def add(bloco, disc, q, valor, prefix, items, extra=None):
    for i, t in enumerate(items, 1):
        d = dict(id=f"{prefix}-{i:02d}", bloco=bloco, disciplina=disc, item=i,
                 questoes_disciplina=q, valor_questao=valor, texto_edital=t)
        if extra and i in extra: d.update(extra[i])
        topics.append(d)

# Conhecimentos Gerais
add("Gerais", "Língua Portuguesa", 8, 0.3, "port", split_items(block(1960, 1970), 6))
add("Gerais", "Raciocínio Lógico", 6, 0.3, "rl", split_items(block(1973, 1976), 5))
add("Gerais", "Noções de Informática", 6, 0.3, "info", split_items(block(1979, 1996), 11))
# Institucionais (itens 1-4; subitens 1.1... ficam dentro do texto do item)
inst = block(2000, 2048)
inst = inst.replace("1. NATUREZA", "1 NATUREZA")
inst_items = split_items(inst, 4)
qs = {1: 4, 2: 4, 3: 8, 4: 4}
nomes = {1: "Natureza e finalidade dos serviços sociais autônomos",
         2: "Lei e decreto de criação da ABDI; Estatuto",
         3: "Regulamento de licitações e contratos; regulamento de convênios",
         4: "Ética e conduta; missão e atuação institucional da agência"}
for i, t in enumerate(inst_items, 1):
    topics.append(dict(id=f"inst-{i:02d}", bloco="Institucionais", disciplina=nomes[i], item=i,
                       questoes_disciplina=qs[i], valor_questao=0.3, texto_edital=t))
# Específicos: Comunicação e Marketing (26 itens)
add("Específicos", "API - Comunicação e Marketing", 20, 0.65, "esp", split_items(block(2083, 2098), 26))

json.dump(dict(fonte="Edital 01/2026 ABDI/FGV, Anexo II, págs. 38-40 (publicado em 20/10/2026)",
               perfil="API - Comunicação e Marketing",
               aviso="Texto transcrito do PDF; espaços e palavras partidas pela extração foram corrigidos.",
               topicos=topics), open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(len(topics), "tópicos")
