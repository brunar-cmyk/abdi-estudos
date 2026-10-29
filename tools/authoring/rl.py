import itertools
from lib import Q, L, escrever

LOG = "Referência conceitual: lógica proposicional clássica (tabelas-verdade e regras de inferência)"
CONJ = "Referência conceitual: teoria dos conjuntos e diagramas de Venn"
ARIT = "Referência conceitual: matemática básica (razão, proporção, porcentagem, média, MMC)"
GEOM = "Referência conceitual: geometria plana e espacial básica"
MATR = "Referência conceitual: álgebra de matrizes (operações e determinante de ordem 2)"

V, F = True, False
imp = lambda p, q: (not p) or q

# ---- verificações por força bruta das equivalências usadas nas questões -------------------------
for p, q in itertools.product([V, F], repeat=2):
    assert (not (p and q)) == ((not p) or (not q))             # De Morgan 1
    assert (not (p or q)) == ((not p) and (not q))             # De Morgan 2
    assert (not imp(p, q)) == (p and (not q))                  # negação do condicional
    assert imp(p, q) == imp(not q, not p)                      # contrapositiva
    assert imp(p, q) == ((not p) or q)                         # condicional como disjunção
assert imp(F, V) is True                                       # antecedente falso
assert (V != F) and not (V != V)                               # ou exclusivo
# veracidade: A diz "B mente", B diz "C mente", C diz "A e B mentem"
sols = [(a, b, c) for a, b, c in itertools.product([V, F], repeat=3)
        if a == (not b) and b == (not c) and c == ((not a) and (not b))]
assert sols == [(F, V, F)], sols                               # só B diz a verdade
# conjuntos
assert 40 - 5 == 25 + 18 - 8
assert 60 - (35 + 28 - 10) == 7 and 35 - 10 == 25
# aritmética
assert 6 * 10 / 15 == 4 and abs(250 * 1.2 * 0.8 - 240) < 1e-9 and (6 + 7 + 9 + 10) / 4 == 8
import math
assert math.lcm(12, 18) == 36
# geometria
assert 6 ** 2 + 8 ** 2 == 10 ** 2 and 12 * 5 == 60 and 2 * (12 + 5) == 34 and 2 * 3 * 1.5 == 9
# matrizes
A = [[1, 2], [3, 4]]; B = [[0, 1], [1, 0]]
det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
soma = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
prod = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert det == -2 and soma == [[1, 3], [4, 4]] and prod == [[2, 1], [4, 3]]
assert [list(c) for c in zip(*[[1, 2, 3], [4, 5, 6]])] == [[1, 4], [2, 5], [3, 6]]
# sequências
assert [5 + 6 * i for i in range(5)] == [5, 11, 17, 23, 29]
assert [2 * 3 ** i for i in range(5)] == [2, 6, 18, 54, 162]
assert [1, 1, 2, 3, 5, 8, 13][-1] == 5 + 8

# ------------------------------------------------------------------------------------------------
escrever("u-rl-proposicional", "Lógica proposicional: tabelas-verdade, negações e conjuntos", "Gerais", "rl",
         ["rl-01", "rl-03"], [
    L("rlp-l1", "Proposições, conectivos e tabelas-verdade", 8, [
        "Proposição é uma sentença declarativa que pode ser verdadeira ou falsa. Perguntas, ordens, exclamações e sentenças abertas (\"x + 3 = 7\") não são proposições.",
        "Conjunção (p e q): verdadeira só se as duas forem verdadeiras. Disjunção inclusiva (p ou q): falsa só se as duas forem falsas. Disjunção exclusiva (ou p ou q): verdadeira só se os valores forem diferentes.",
        "Condicional (se p, então q): falsa somente quando p é verdadeira e q é falsa. Bicondicional (p se e somente se q): verdadeira quando p e q têm o mesmo valor.",
        "Com n proposições simples, a tabela-verdade tem 2 elevado a n linhas. Tautologia é sempre verdadeira, contradição é sempre falsa."
    ], [
        ("Quando o condicional \"se p, então q\" é falso?", "Somente quando p é verdadeira e q é falsa."),
        ("Quando a disjunção exclusiva é verdadeira?", "Quando as duas proposições têm valores diferentes."),
        ("Linhas da tabela-verdade", "2 elevado ao número de proposições simples: com 3, são 8 linhas.")
    ], [
        Q("Assinale a alternativa que contém uma proposição lógica.",
          "O Brasil é um país da América do Sul.",
          ["Que horas são?", "Feche a porta ao sair.", "x + 3 = 7", "Quanta alegria!"],
          "Proposição é sentença declarativa com valor lógico definido. Pergunta, ordem e exclamação não têm valor lógico, e \"x + 3 = 7\" é sentença aberta.", LOG),
        Q("Considere as proposições: \"9 é primo\" (falsa) e \"7 é primo\" (verdadeira). A proposição \"Se 9 é primo, então 7 é primo\" é",
          "verdadeira, pois o antecedente é falso.",
          ["falsa, pois o antecedente é falso.", "falsa, pois o consequente é verdadeiro.", "verdadeira, pois ambos são verdadeiros.", "indeterminada, pois depende de uma terceira proposição."],
          "O condicional só é falso quando o antecedente é verdadeiro e o consequente é falso. Com antecedente falso, é verdadeiro.", LOG),
        Q("Sabe-se que \"Ana viaja\" é verdadeira e \"Bia viaja\" é verdadeira. A proposição \"Ou Ana viaja ou Bia viaja\" (disjunção exclusiva) é",
          "falsa, pois as duas têm o mesmo valor lógico.",
          ["verdadeira, pois pelo menos uma viaja.", "verdadeira, pois as duas viajam.", "falsa, pois Ana não viaja.", "indeterminada."],
          "A disjunção exclusiva só é verdadeira quando as proposições têm valores diferentes.", LOG),
        Q("Uma tabela-verdade construída com três proposições simples distintas possui quantas linhas?",
          "8",
          ["6", "9", "3", "16"],
          "O número de linhas é 2 elevado a 3, ou seja, 8.", LOG),
    ]),
    L("rlp-l2", "Negações e equivalências", 8, [
        "Negação de \"p e q\": \"não p ou não q\". Negação de \"p ou q\": \"não p e não q\" (leis de De Morgan).",
        "Negação de \"se p, então q\": \"p e não q\". É a única forma de o condicional ser falso.",
        "Equivalências do condicional: \"se p, então q\" equivale a \"se não q, então não p\" (contrapositiva) e a \"não p ou q\".",
        "Não são equivalentes ao condicional a recíproca (\"se q, então p\") e a inversa (\"se não p, então não q\")."
    ], [
        ("Negação de \"p e q\"", "Não p ou não q (De Morgan)."),
        ("Negação de \"se p, então q\"", "p e não q."),
        ("Contrapositiva", "\"Se p, então q\" equivale a \"se não q, então não p\".")
    ], [
        Q("A negação de \"Maria estuda e João trabalha\" é",
          "Maria não estuda ou João não trabalha.",
          ["Maria não estuda e João não trabalha.", "Maria estuda ou João trabalha.", "Se Maria estuda, João não trabalha.", "Maria não estuda, e João trabalha."],
          "Pela lei de De Morgan, a negação de uma conjunção é a disjunção das negações.", LOG),
        Q("A negação de \"Se chove, então o evento é cancelado\" é",
          "Chove e o evento não é cancelado.",
          ["Não chove e o evento é cancelado.", "Se não chove, então o evento não é cancelado.", "Se o evento não é cancelado, então não chove.", "Não chove ou o evento é cancelado."],
          "A negação do condicional é a conjunção do antecedente com a negação do consequente.", LOG),
        Q("Uma proposição equivalente a \"Se o relatório foi enviado, então a reunião ocorreu\" é",
          "Se a reunião não ocorreu, então o relatório não foi enviado.",
          ["Se a reunião ocorreu, então o relatório foi enviado.", "Se o relatório não foi enviado, então a reunião não ocorreu.", "O relatório foi enviado e a reunião não ocorreu.", "O relatório não foi enviado e a reunião ocorreu."],
          "A contrapositiva é equivalente ao condicional. A recíproca e a inversa não são.", LOG),
        Q("A negação de \"O servidor é pontual ou assíduo\" é",
          "O servidor não é pontual e não é assíduo.",
          ["O servidor não é pontual ou não é assíduo.", "O servidor é impontual ou assíduo.", "O servidor é pontual e assíduo.", "Se o servidor é pontual, então é assíduo."],
          "Pela lei de De Morgan, a negação de uma disjunção é a conjunção das negações.", LOG),
    ]),
    L("rlp-l3", "Conjuntos e diagramas lógicos", 8, [
        "Quantidade de elementos da união: n(A ou B) = n(A) + n(B) menos n(A e B). Subtrai-se a interseção para não contar duas vezes.",
        "Elementos que pertencem apenas a A: n(A) menos n(A e B).",
        "Em problemas com um total, o que está fora dos dois conjuntos é o total menos a união.",
        "Comece sempre pela interseção quando ela é dada, depois preencha as demais regiões do diagrama."
    ], [
        ("n(A ou B)", "n(A) + n(B) menos n(A e B)."),
        ("Apenas A", "n(A) menos a interseção n(A e B)."),
        ("Tautologia", "Proposição sempre verdadeira, como \"p ou não p\".")
    ], [
        Q("Em um grupo de 40 empregados, 25 falam inglês, 18 falam espanhol e 5 não falam nenhuma das duas línguas. Quantos falam as duas?",
          "8",
          ["5", "7", "10", "13"],
          "35 falam pelo menos uma língua (40 menos 5). Como 25 + 18 = 43 e 43 menos 35 é 8, 8 falam as duas.", CONJ),
        Q("Em uma pesquisa com 60 pessoas, 35 leem jornal, 28 leem revistas e 10 leem ambos. Quantas não leem nenhum dos dois?",
          "7",
          ["5", "10", "12", "15"],
          "A união tem 35 + 28 menos 10 = 53. Fora dela ficam 60 menos 53 = 7.", CONJ),
        Q("Na pesquisa anterior (60 pessoas, 35 leem jornal, 28 leem revistas, 10 leem ambos), quantas leem apenas jornal?",
          "25",
          ["10", "18", "35", "45"],
          "Apenas jornal é 35 menos a interseção de 10, ou seja, 25.", CONJ),
        Q("Das alternativas, a única que é uma tautologia é",
          "\"Chove ou não chove.\"",
          ["\"Chove e não chove.\"", "\"Chove.\"", "\"Se chove, então não chove.\"", "\"Não chove.\""],
          "\"p ou não p\" é verdadeira em qualquer caso. \"p e não p\" é contradição, e as demais dependem do valor de p.", LOG),
    ]),
], semente=0)

escrever("u-rl-argumentacao", "Argumentação lógica, sequências e analogias", "Gerais", "rl", ["rl-02"], [
    L("rla-l1", "Argumentos e validade", 8, [
        "Argumento é um conjunto de premissas e uma conclusão. É válido quando a conclusão é necessariamente verdadeira se as premissas forem verdadeiras. Validade não é o mesmo que verdade.",
        "Formas válidas: modus ponens (se p, então q; p; logo q), modus tollens (se p, então q; não q; logo não p), silogismo hipotético (se p, então q; se q, então r; logo se p, então r) e silogismo disjuntivo (p ou q; não p; logo q).",
        "Falácias comuns: afirmação do consequente (se p, então q; q; logo p) e negação do antecedente (se p, então q; não p; logo não q)."
    ], [
        ("Modus tollens", "Se p, então q; não q; logo não p."),
        ("Afirmação do consequente", "Falácia: \"se p, então q; q; logo p\" não é válido."),
        ("Silogismo hipotético", "Se p, então q; se q, então r; logo se p, então r.")
    ], [
        Q("Premissas: \"Se o sistema está atualizado, o relatório é gerado\" e \"O relatório não foi gerado\". A conclusão que decorre necessariamente é:",
          "O sistema não está atualizado.",
          ["O sistema está atualizado.", "O relatório será gerado amanhã.", "O sistema está com falha.", "Nenhuma conclusão é possível."],
          "É um modus tollens: negando o consequente, nega-se o antecedente.", LOG),
        Q("O argumento \"Se chove, a rua molha. A rua está molhada. Logo, choveu\" é",
          "inválido, por afirmação do consequente.",
          ["válido, por modus ponens.", "válido, por modus tollens.", "válido, por silogismo hipotético.", "inválido, por negação do antecedente."],
          "A rua pode estar molhada por outra causa. Afirmar o consequente não permite concluir o antecedente.", LOG),
        Q("Premissas: \"Se estudo, aprendo\" e \"Se aprendo, passo\". A conclusão válida é:",
          "Se estudo, passo.",
          ["Se passo, estudo.", "Se não estudo, não passo.", "Estudo e passo.", "Aprendo, logo estudo."],
          "É um silogismo hipotético: encadeiam-se os condicionais.", LOG),
        Q("Premissas: \"Ou o prazo é prorrogado ou as inscrições encerram hoje\" e \"O prazo não foi prorrogado\". A conclusão válida é:",
          "As inscrições encerram hoje.",
          ["O prazo será prorrogado.", "As inscrições não encerram hoje.", "O prazo foi prorrogado e as inscrições encerram.", "Nada se pode concluir."],
          "É um silogismo disjuntivo: negada uma das alternativas, vale a outra.", LOG),
    ]),
    L("rla-l2", "Sequências, analogias e veracidade", 9, [
        "Progressão aritmética soma uma razão constante (5, 11, 17, 23: razão 6). Progressão geométrica multiplica por uma razão constante (2, 6, 18, 54: razão 3).",
        "Há sequências em que cada termo é a soma dos dois anteriores (1, 1, 2, 3, 5, 8, 13).",
        "Em problemas de veracidade (quem fala a verdade e quem mente), teste cada hipótese e descarte as que geram contradição.",
        "Analogias mantêm a mesma relação entre dois pares de elementos."
    ], [
        ("Progressão aritmética x geométrica", "Aritmética: soma-se sempre o mesmo valor. Geométrica: multiplica-se sempre pelo mesmo valor."),
        ("Soma dos dois termos anteriores", "Sequência de Fibonacci: 1, 1, 2, 3, 5, 8, 13."),
        ("Como resolver problemas de veracidade", "Assuma uma hipótese, verifique as consequências e descarte as que levam a contradição.")
    ], [
        Q("O próximo termo da sequência 5, 11, 17, 23, ... é",
          "29",
          ["27", "28", "30", "35"],
          "A razão é 6, e 23 + 6 = 29.", ARIT),
        Q("O próximo termo da sequência 2, 6, 18, 54, ... é",
          "162",
          ["108", "126", "144", "216"],
          "Cada termo é multiplicado por 3: 54 vezes 3 é 162.", ARIT),
        Q("Na sequência 1, 1, 2, 3, 5, 8, ..., o termo seguinte é",
          "13",
          ["11", "12", "14", "16"],
          "Cada termo é a soma dos dois anteriores: 5 + 8 = 13.", ARIT),
        Q("Três pessoas, A, B e C, sempre dizem a verdade ou sempre mentem. A diz: \"B mente\". B diz: \"C mente\". C diz: \"A e B mentem\". Quem diz a verdade?",
          "Apenas B.",
          ["Apenas A.", "Apenas C.", "A e C.", "Ninguém."],
          "Se A dissesse a verdade, B mentiria, C diria a verdade e então A e B mentiriam, o que contradiz. Testando B como verdadeiro: C mente, A mente, e a fala de C (\"A e B mentem\") é falsa, o que é coerente. Só B diz a verdade.", LOG),
    ]),
], semente=1)

escrever("u-rl-primeira-ordem", "Lógica de primeira ordem: quantificadores e silogismos", "Gerais", "rl", ["rl-04"], [
    L("rl1-l1", "Quantificadores e suas negações", 7, [
        "Quantificador universal: todo, qualquer. Existencial: algum, existe, pelo menos um. Universal negativo: nenhum.",
        "Negação de \"todo A é B\": \"algum A não é B\".",
        "Negação de \"algum A é B\": \"nenhum A é B\". Negação de \"nenhum A é B\": \"algum A é B\".",
        "Ao negar uma frase com \"e\" ou \"ou\" dentro, aplique De Morgan ao predicado."
    ], [
        ("Negação de \"todo A é B\"", "Algum A não é B."),
        ("Negação de \"algum A é B\"", "Nenhum A é B."),
        ("Negação de \"nenhum A é B\"", "Algum A é B.")
    ], [
        Q("A negação de \"Todos os servidores participaram do curso\" é",
          "Algum servidor não participou do curso.",
          ["Nenhum servidor participou do curso.", "Todos os servidores não participaram do curso.", "Algum servidor participou do curso.", "Poucos servidores participaram do curso."],
          "A negação de um universal afirmativo é um particular negativo. \"Nenhum\" é mais forte do que a negação lógica.", LOG),
        Q("A negação de \"Algum candidato foi aprovado\" é",
          "Nenhum candidato foi aprovado.",
          ["Algum candidato não foi aprovado.", "Todos os candidatos foram aprovados.", "Todos os candidatos não foram aprovados e alguns foram.", "Vários candidatos foram reprovados."],
          "Negar \"existe\" é afirmar que nenhum satisfaz a propriedade.", LOG),
        Q("A negação de \"Nenhum documento está pendente\" é",
          "Algum documento está pendente.",
          ["Todos os documentos estão pendentes.", "Algum documento não está pendente.", "Todos os documentos foram entregues.", "Nenhum documento foi entregue."],
          "A negação de \"nenhum\" é \"pelo menos um\".", LOG),
        Q("A negação de \"Todo analista é pontual ou assíduo\" é",
          "Algum analista não é pontual e não é assíduo.",
          ["Nenhum analista é pontual ou assíduo.", "Algum analista não é pontual ou não é assíduo.", "Todo analista é impontual e inassíduo.", "Algum analista é pontual e assíduo."],
          "Nega-se o quantificador (todo vira algum não) e aplica-se De Morgan ao predicado (ou vira e, com negação).", LOG),
    ]),
    L("rl1-l2", "Silogismos categóricos e diagramas", 8, [
        "\"Todo A é B\": o círculo de A fica dentro do de B. \"Nenhum A é B\": círculos separados. \"Algum A é B\": os círculos se cruzam.",
        "Conclusões válidas: se todo A é B e todo B é C, então todo A é C. Se todo A é B e algum C é A, então algum C é B. Se nenhum A é B e todo C é A, então nenhum C é B.",
        "Cuidado com a falácia: de \"todo A é B\" e \"todo C é B\" não se conclui que todo A é C."
    ], [
        ("Silogismo clássico", "Todo A é B; todo B é C; logo todo A é C."),
        ("Falácia do termo médio", "Todo A é B e todo C é B não permite concluir nenhuma relação entre A e C."),
        ("\"Algum A é B\" no diagrama", "Os círculos de A e B têm interseção não vazia.")
    ], [
        Q("Premissas: \"Todo analista é graduado\" e \"Todo graduado é elegível\". Conclui-se necessariamente que",
          "todo analista é elegível.",
          ["todo elegível é analista.", "algum elegível não é graduado.", "nenhum analista é elegível.", "todo graduado é analista."],
          "Encadeando os dois universais, todo analista é elegível.", LOG),
        Q("Premissas: \"Nenhum estagiário tem acesso total\" e \"Todo bolsista é estagiário\". Conclui-se necessariamente que",
          "nenhum bolsista tem acesso total.",
          ["todo bolsista tem acesso total.", "algum bolsista tem acesso total.", "nenhum estagiário é bolsista.", "todo estagiário é bolsista."],
          "Como todo bolsista está no conjunto dos estagiários, e nenhum deles tem acesso total, nenhum bolsista tem.", LOG),
        Q("Premissas: \"Todo gestor é líder\" e \"Algum analista é gestor\". Conclui-se necessariamente que",
          "algum analista é líder.",
          ["todo analista é líder.", "nenhum analista é líder.", "todo líder é gestor.", "algum líder não é gestor."],
          "Os analistas que são gestores são líderes. Nada se pode afirmar sobre todos os analistas.", LOG),
        Q("A partir das premissas \"Todo redator é comunicador\" e \"Todo jornalista é comunicador\", é correto afirmar que",
          "não se pode concluir necessariamente que todo redator seja jornalista.",
          ["todo redator é jornalista.", "todo jornalista é redator.", "nenhum redator é jornalista.", "algum comunicador não é redator."],
          "Os dois conjuntos estão dentro de \"comunicador\", mas podem ou não se sobrepor. A conclusão não é necessária.", LOG),
    ]),
], semente=2)

escrever("u-rl-problemas", "Problemas aritméticos, geométricos e matriciais", "Gerais", "rl", ["rl-05"], [
    L("rlpb-l1", "Problemas aritméticos", 8, [
        "Regra de três: com grandezas inversamente proporcionais (mais pessoas, menos dias), multiplica-se. Com diretamente proporcionais, divide-se em cruz.",
        "Porcentagem: aumento de 20% multiplica por 1,2 e desconto de 20% multiplica por 0,8. Aumento e desconto de mesmo percentual não se anulam.",
        "Média aritmética: soma dos valores dividida pela quantidade. MMC dá o primeiro momento em que eventos periódicos coincidem."
    ], [
        ("Aumento e desconto sucessivos", "Multiplicam-se os fatores: 1,2 vezes 0,8 é 0,96, ou seja, queda de 4%."),
        ("Grandezas inversamente proporcionais", "Quando uma aumenta, a outra diminui na mesma razão: o produto se mantém."),
        ("Para que serve o MMC em problemas de eventos periódicos?", "Para saber quando eventos com períodos diferentes voltam a coincidir.")
    ], [
        Q("Uma tarefa é concluída por 6 analistas em 10 dias. Mantido o ritmo, em quantos dias 15 analistas a concluiriam?",
          "4 dias",
          ["2 dias", "6 dias", "15 dias", "25 dias"],
          "As grandezas são inversamente proporcionais: 6 vezes 10 = 60 e 60 dividido por 15 é 4.", ARIT),
        Q("Um produto custava R$ 250,00, sofreu aumento de 20% e, em seguida, desconto de 20% sobre o novo preço. O preço final é",
          "R$ 240,00",
          ["R$ 250,00", "R$ 260,00", "R$ 230,00", "R$ 300,00"],
          "250 vezes 1,2 = 300, e 300 vezes 0,8 = 240. Os percentuais incidem sobre bases diferentes.", ARIT),
        Q("As notas de um candidato foram 6, 7, 9 e 10. A média aritmética é",
          "8",
          ["7,5", "8,5", "9", "32"],
          "A soma é 32 e 32 dividido por 4 é 8.", ARIT),
        Q("Dois eventos ocorrem a cada 12 e a cada 18 dias. Se coincidiram hoje, voltarão a coincidir daqui a",
          "36 dias",
          ["6 dias", "30 dias", "54 dias", "216 dias"],
          "O MMC de 12 e 18 é 36.", ARIT),
    ]),
    L("rlpb-l2", "Problemas geométricos", 8, [
        "Retângulo: área é base vezes altura e perímetro é duas vezes (base mais altura). Círculo: área é pi vezes raio ao quadrado.",
        "Teorema de Pitágoras: no triângulo retângulo, a hipotenusa ao quadrado é a soma dos quadrados dos catetos.",
        "Volume do paralelepípedo: comprimento vezes largura vezes altura. Um metro cúbico equivale a 1.000 litros."
    ], [
        ("Teorema de Pitágoras", "Hipotenusa ao quadrado é igual à soma dos quadrados dos catetos."),
        ("Área do círculo", "Pi vezes o raio ao quadrado."),
        ("1 metro cúbico em litros", "1.000 litros.")
    ], [
        Q("Um triângulo retângulo tem catetos de 6 cm e 8 cm. A hipotenusa mede",
          "10 cm",
          ["7 cm", "12 cm", "14 cm", "48 cm"],
          "36 mais 64 é 100, cuja raiz quadrada é 10.", GEOM),
        Q("Um terreno retangular mede 12 m por 5 m. Sua área e seu perímetro são, respectivamente,",
          "60 metros quadrados e 34 metros",
          ["34 metros quadrados e 60 metros", "60 metros quadrados e 17 metros", "17 metros quadrados e 60 metros", "30 metros quadrados e 34 metros"],
          "Área: 12 vezes 5 = 60. Perímetro: 2 vezes (12 + 5) = 34.", GEOM),
        Q("Um reservatório em forma de paralelepípedo mede 2 m de comprimento, 3 m de largura e 1,5 m de altura. Sua capacidade é de",
          "9.000 litros",
          ["6.500 litros", "7.500 litros", "9 litros", "90.000 litros"],
          "O volume é 2 vezes 3 vezes 1,5 = 9 metros cúbicos, e 1 metro cúbico equivale a 1.000 litros.", GEOM),
        Q("A área de um círculo de raio 3 cm é",
          "9 pi centímetros quadrados",
          ["6 pi centímetros quadrados", "3 pi centímetros quadrados", "18 pi centímetros quadrados", "27 pi centímetros quadrados"],
          "A área é pi vezes o raio ao quadrado: pi vezes 9.", GEOM),
    ]),
    L("rlpb-l3", "Matrizes", 8, [
        "Matriz é uma tabela de números organizada em linhas e colunas. Soma: termo a termo, entre matrizes de mesma ordem.",
        "Produto: o elemento da linha i e coluna j é a soma dos produtos dos elementos da linha i da primeira pelos da coluna j da segunda.",
        "Determinante de ordem 2: diagonal principal menos diagonal secundária (a d menos b c). Transposta: troca linhas por colunas."
    ], [
        ("Determinante de ordem 2", "Produto da diagonal principal menos o produto da diagonal secundária."),
        ("Matriz transposta", "Linhas viram colunas, e colunas viram linhas."),
        ("Condição para somar matrizes", "Ter a mesma ordem (mesmo número de linhas e de colunas).")
    ], [
        Q("O determinante da matriz de linhas (1, 2) e (3, 4) é",
          "-2",
          ["2", "-10", "10", "0"],
          "1 vezes 4 menos 2 vezes 3 é 4 menos 6, ou seja, -2.", MATR),
        Q("Sejam A com linhas (1, 2) e (3, 4), e B com linhas (0, 1) e (1, 0). A soma A + B tem linhas",
          "(1, 3) e (4, 4)",
          ["(1, 3) e (3, 4)", "(2, 1) e (4, 3)", "(1, 2) e (3, 4)", "(0, 2) e (3, 0)"],
          "Soma-se termo a termo: 1+0, 2+1, 3+1, 4+0.", MATR),
        Q("Para as mesmas matrizes A (linhas (1, 2) e (3, 4)) e B (linhas (0, 1) e (1, 0)), o produto A vezes B tem linhas",
          "(2, 1) e (4, 3)",
          ["(0, 2) e (3, 0)", "(1, 3) e (4, 4)", "(1, 2) e (3, 4)", "(2, 4) e (1, 3)"],
          "Linha 1: 1x0+2x1 = 2 e 1x1+2x0 = 1. Linha 2: 3x0+4x1 = 4 e 3x1+4x0 = 3.", MATR),
        Q("A transposta da matriz de linhas (1, 2, 3) e (4, 5, 6) tem",
          "3 linhas: (1, 4), (2, 5) e (3, 6).",
          ["2 linhas: (1, 2, 3) e (4, 5, 6).", "3 linhas: (3, 6), (2, 5) e (1, 4).", "2 linhas: (6, 5, 4) e (3, 2, 1).", "3 linhas: (1, 2), (3, 4) e (5, 6)."],
          "A transposta troca linhas por colunas: a primeira coluna (1, 4) passa a ser a primeira linha.", MATR),
    ]),
], semente=3)
