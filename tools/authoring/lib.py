"""Ajudantes para escrever unidades de conteúdo de forma compacta.
Cada questão é escrita com a alternativa CERTA em primeiro lugar; o script embaralha as
alternativas de forma equilibrada e grava o JSON em content/units/ (formato que o app lê).
Uso: python3 tools/authoring/port.py"""
import json, os, random

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
ALVOS = [2, 0, 4, 1, 3]


def Q(enunciado, certa, erradas, explicacao, fonte, topico=None):
    assert len(erradas) == 4, f"precisa de 4 erradas: {enunciado[:50]}"
    return dict(enunciado=enunciado, certa=certa, erradas=erradas, explicacao=explicacao, fonte=fonte, topico=topico)


def L(id, titulo, minutos, resumo, cards, questoes):
    return dict(id=id, titulo=titulo, minutos=minutos, resumo=resumo, cards=cards, questoes=questoes)


def escrever(id, titulo, bloco, categoria, topicos, licoes, numeros=None, semente=0):
    rng = random.Random(f"{id}{semente}")
    n = semente
    out_licoes = []
    for lic in licoes:
        qs = []
        for i, q in enumerate(lic["questoes"], 1):
            alvo = ALVOS[n % 5]
            n += 1
            outras = list(q["erradas"])
            rng.shuffle(outras)
            alts = outras[:alvo] + [q["certa"]] + outras[alvo:]
            item = dict(id=f"{lic['id']}-q{i}", enunciado=q["enunciado"], alternativas=alts, correta=alvo,
                        explicacao=q["explicacao"], fonte=q["fonte"])
            if q.get("topico"):
                item["topico"] = q["topico"]
            qs.append(item)
        out_licoes.append(dict(id=lic["id"], titulo=lic["titulo"], minutos=lic["minutos"], resumo=lic["resumo"],
                               flashcards=[dict(frente=f, verso=v) for f, v in lic["cards"]], questoes=qs))
    d = dict(id=id, titulo=titulo, bloco=bloco, categoria=categoria, topicos=topicos)
    if numeros:
        d["pacoteNumeros"] = [dict(rotulo=a, valor=b, fonte=c) for a, b, c in numeros]
    d["licoes"] = out_licoes
    caminho = os.path.join(RAIZ, "content", "units", f"{id}.json")
    json.dump(d, open(caminho, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{id}: {len(out_licoes)} lições, {sum(len(l['questoes']) for l in out_licoes)} questões")
