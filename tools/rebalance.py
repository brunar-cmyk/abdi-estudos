"""Redistribui a posição da alternativa correta numa unidade, sem mudar o texto das alternativas.
Uso: python3 -I tools/rebalance.py content/units/<unidade>.json
Só use em unidades cujas explicações não citam letras (o validate avisa)."""
import json, sys, random

path = sys.argv[1]
d = json.load(open(path, encoding="utf-8"))
alvos = [2, 4, 0, 3, 1]
n = 0
rng = random.Random(path)
for lic in d["licoes"]:
    for q in lic["questoes"]:
        certa = q["alternativas"][q["correta"]]
        outras = [a for i, a in enumerate(q["alternativas"]) if i != q["correta"]]
        rng.shuffle(outras)
        alvo = alvos[n % 5]
        q["alternativas"] = outras[:alvo] + [certa] + outras[alvo:]
        q["correta"] = alvo
        n += 1
json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(n, "questões redistribuídas")
