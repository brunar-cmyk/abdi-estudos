from lib import Q, L, escrever

GRAM = "Referência conceitual: gramática normativa (C. Cunha e L. Cintra, Nova Gramática do Português Contemporâneo)"
ORTO = "Acordo Ortográfico da Língua Portuguesa, promulgado pelo Decreto 6.583/2008 (planalto.gov.br), e Vocabulário Ortográfico (VOLP)"
TEXTO = "Referência conceitual: interpretação de texto (leitura de texto original escrito para esta lição)"
REDOF = "Referência conceitual: Manual de Redação da Presidência da República (3ª ed., 2018)"

# ---------------------------------------------------------------- interpretação, gêneros, ortografia
escrever("u-port-interpretacao", "Interpretação, gêneros textuais e ortografia", "Gerais", "port",
         ["port-01", "port-02", "port-03"], [
    L("pint-l1", "Compreensão e inferência", 7, [
        "Ideia central é o que o texto defende ou informa como um todo. As ideias secundárias a sustentam. Procure a tese e os argumentos.",
        "Informação explícita está dita no texto. Pressuposto decorre das palavras usadas: em \"A agência voltou a divulgar o relatório\", pressupõe-se que já o divulgava antes. Subentendido é inferência do leitor.",
        "Sentido denotativo é o literal; conotativo é figurado, como em \"o prazo foi um muro\". Ironia diz o contrário do que se quer comunicar.",
        "Armadilhas frequentes: extrapolação (ir além do texto), redução (dizer menos), contradição e generalização com palavras absolutas, como sempre, nunca e todos."
    ], [
        ("Pressuposto x subentendido", "Pressuposto vem marcado nas palavras do texto (voltou a, deixou de). Subentendido é a conclusão que o leitor tira do contexto."),
        ("O que é extrapolação em questão de interpretação?", "Afirmar algo que vai além do que o texto diz ou permite concluir."),
        ("Denotação x conotação", "Denotação: sentido literal. Conotação: sentido figurado, metafórico.")
    ], [
        Q("Em \"A agência voltou a divulgar o relatório anual em seu sítio\", há o pressuposto de que",
          "a agência já havia divulgado o relatório anual antes.",
          ["o relatório nunca foi divulgado.", "a divulgação do relatório foi proibida.", "o sítio da agência foi criado agora.", "apenas jornalistas podem acessar o relatório."],
          "O verbo \"voltar a\" pressupõe uma ação anterior. As demais alternativas contradizem o texto ou inventam informações.", TEXTO),
        Q("Leia: \"Cresce o número de órgãos públicos que publicam dados em formato aberto. A medida facilita o controle social e permite que pesquisadores e empresas reutilizem as informações. Ainda assim, muitos conjuntos de dados continuam sem atualização regular, o que limita seu uso.\" A ideia central do texto é que",
          "a abertura de dados avança e traz benefícios, mas a falta de atualização regular limita seu aproveitamento.",
          ["os dados abertos são inúteis para pesquisadores e empresas.", "os órgãos públicos estão proibidos de manter dados sem atualização.", "apenas as empresas se beneficiam da publicação de dados.", "o controle social independe da divulgação de dados."],
          "O texto apresenta o avanço da abertura de dados, seus benefícios e uma limitação (atualização irregular). As outras alternativas distorcem essas informações.", TEXTO),
        Q("Com base no texto sobre dados abertos (\"Cresce o número de órgãos públicos que publicam dados em formato aberto [...] muitos conjuntos de dados continuam sem atualização regular\"), é possível inferir que",
          "a falta de atualização pode reduzir a utilidade de dados já publicados.",
          ["todos os órgãos públicos já publicam dados abertos.", "as empresas deixaram de usar dados públicos.", "o controle social foi extinto.", "os pesquisadores rejeitam dados abertos."],
          "O próprio texto afirma que a falta de atualização limita o uso. Dizer que todos os órgãos publicam dados abertos é extrapolação: o texto diz apenas que o número cresce.", TEXTO),
        Q("Em \"O prazo foi um muro entre a equipe e o lançamento\", a palavra \"muro\" está empregada em sentido",
          "conotativo, pois apresenta o prazo como um obstáculo.",
          ["denotativo, pois indica uma construção de alvenaria.", "denotativo, pois descreve a estrutura do escritório.", "literal, pois o prazo é um objeto físico.", "técnico, pois pertence ao vocabulário da engenharia."],
          "A metáfora compara o prazo a um muro, o que caracteriza sentido figurado (conotativo).", TEXTO),
    ]),
    L("pint-l2", "Tipos e gêneros textuais", 7, [
        "Tipos textuais são as sequências básicas: narrativo, descritivo, expositivo, dissertativo-argumentativo e injuntivo (instrução). Gêneros textuais são as formas concretas dos textos: notícia, ata, ofício, e-mail, editorial.",
        "O gênero se define pela finalidade, pelo suporte e pela estrutura. Um mesmo gênero pode combinar vários tipos.",
        "Dissertativo-argumentativo: defende uma tese com argumentos. Expositivo: apresenta informações sem defender tese. Injuntivo: orienta ou ordena ações (\"preencha, anexe, envie\").",
        "Editorial expressa a posição do veículo, sem assinatura individual. Artigo de opinião é assinado. Ata registra as ocorrências de uma reunião. Ofício é correspondência oficial."
    ], [
        ("Tipo injuntivo", "Orienta ou instrui o leitor a agir, com verbos no imperativo ou no infinitivo (receitas, manuais, instruções)."),
        ("Editorial x artigo de opinião", "Editorial: posição do próprio veículo, sem assinatura individual. Artigo de opinião: assinado por um autor."),
        ("Para que serve uma ata?", "Registrar por escrito o que ocorreu e foi decidido em uma reunião.")
    ], [
        Q("O trecho \"Preencha o formulário, anexe os documentos e envie a inscrição até o prazo final\" é predominantemente do tipo",
          "injuntivo, pois orienta o leitor a executar ações.",
          ["narrativo, pois conta uma sequência de fatos passados.", "descritivo, pois caracteriza um objeto.", "dissertativo-argumentativo, pois defende uma tese.", "expositivo, pois apenas informa conceitos."],
          "Verbos no imperativo que orientam ações caracterizam o tipo injuntivo (instrucional).", GRAM),
        Q("O gênero jornalístico que expressa a posição do próprio veículo de comunicação sobre um tema, sem assinatura individual, é o",
          "editorial.",
          ["artigo de opinião assinado por colaborador.", "noticiário factual.", "reportagem de serviço.", "carta do leitor."],
          "O editorial traduz a opinião do veículo. O artigo de opinião é assinado, e a notícia busca relatar fatos.", GRAM),
        Q("O gênero textual cuja finalidade é registrar por escrito as ocorrências e as deliberações de uma reunião é a",
          "ata.",
          ["circular.", "procuração.", "resenha.", "crônica."],
          "A ata documenta o que foi discutido e decidido em reunião.", REDOF),
        Q("Um texto que apresenta um ponto de vista, o sustenta com argumentos e conclui reafirmando a tese pertence ao tipo",
          "dissertativo-argumentativo.",
          ["narrativo.", "descritivo.", "injuntivo.", "expositivo apenas, sem tese."],
          "A presença de tese, argumentos e conclusão é típica do dissertativo-argumentativo.", GRAM),
    ]),
    L("pint-l3", "Ortografia oficial", 8, [
        "O Acordo Ortográfico (Decreto 6.583/2008) eliminou o trema (exceto em nomes próprios estrangeiros) e o acento em ditongos abertos \"ei\" e \"oi\" de palavras paroxítonas: ideia, heroico, jiboia. Também saiu o acento de \"oo\" e \"ee\": voo, enjoo, leem, veem.",
        "Hífen: usa-se antes de \"h\" e quando a vogal final do prefixo é igual à inicial da palavra (anti-higiênico, micro-ondas). Com \"r\" ou \"s\" no início, dobra-se a consoante e une-se: antirrábico, ultrassom, contrassenso. Prefixos ex-, vice-, pós-, pré-, pró- e recém- levam hífen.",
        "Cuidado com pares: mal (contrário de bem) e mau (contrário de bom); mas (oposição) e mais (quantidade); por que (pergunta ou \"pelo qual\"), porque (explicação), por quê (fim de frase), porquê (substantivo: \"o porquê\").",
        "Também: a gente (pronome) e agente (pessoa); a fim de (finalidade) e afim (semelhante); onde (lugar em que) e aonde (a que lugar)."
    ], [
        ("Mal x mau", "Mal é o contrário de bem (\"saiu-se mal\"). Mau é o contrário de bom (\"mau humor\")."),
        ("Por que, porque, por quê, porquê", "Por que: pergunta. Porque: explicação. Por quê: fim de frase. Porquê: substantivo, com artigo (\"o porquê\")."),
        ("Hífen com r ou s", "Prefixo terminado em vogal + palavra com r ou s: dobra a letra e une (antirrábico, ultrassom).")
    ], [
        Q("Assinale a alternativa em que todas as palavras estão grafadas de acordo com a ortografia oficial vigente.",
          "ideia, heroico, enjoo, micro-ondas",
          ["idéia, heroico, enjoo, micro-ondas", "ideia, heróico, enjoo, micro-ondas", "ideia, heroico, enjôo, micro-ondas", "ideia, heroico, enjoo, microondas"],
          "Com o Acordo, perdem o acento \"ideia\" e \"heroico\" (ditongos abertos em paroxítonas) e \"enjoo\" (terminação oo). Em \"micro-ondas\", o hífen é obrigatório porque o prefixo termina em \"o\" e a palavra começa por \"o\".", ORTO),
        Q("Complete: \"___ você não enviou o relatório? Gostaria de saber o ___.\"",
          "Por que / porquê",
          ["Porque / por quê", "Por quê / porque", "Porque / porquê", "Por que / por que"],
          "Na pergunta direta usa-se \"por que\". \"O porquê\" é substantivo e vem precedido de artigo.", GRAM),
        Q("Complete: \"Ele se saiu ___ na prova porque estava de ___ humor.\"",
          "mal / mau",
          ["mau / mal", "mal / mal", "mau / mau", "mais / mau"],
          "\"Mal\" opõe-se a \"bem\" e modifica o verbo (saiu-se mal). \"Mau\" opõe-se a \"bom\" e acompanha o substantivo (mau humor).", GRAM),
        Q("Assinale a palavra grafada corretamente de acordo com o Acordo Ortográfico.",
          "antirrábico",
          ["anti-rábico", "antirábico", "antirrabico", "anti-rrábico"],
          "Prefixo terminado em vogal seguido de palavra iniciada por \"r\": dobra-se o \"r\" e une-se (antirrábico). A palavra é proparoxítona (an-ti-rrá-bi-co), por isso leva acento.", ORTO),
    ]),
], semente=0)

# ---------------------------------------------------------------- coesão e tempos verbais
escrever("u-port-coesao", "Coesão textual e tempos verbais", "Gerais", "port", ["port-04"], [
    L("pcoe-l1", "Coesão referencial e sequencial", 7, [
        "Coesão referencial retoma ou antecipa termos: pronomes (ele, esse, o qual), sinônimos, hiperônimos, elipse e expressões nominais (\"a agência\"). Anáfora retoma algo já dito; catáfora antecipa algo que será dito.",
        "Coesão sequencial usa conectores para organizar as relações entre ideias.",
        "Principais relações: adição (e, além disso), oposição (mas, porém, contudo, no entanto), conclusão (logo, portanto, por isso), explicação (pois, porque), causa (já que, visto que), consequência (de modo que), concessão (embora, ainda que), condição (se, caso, desde que), finalidade (para que, a fim de), tempo (quando, assim que), conformidade (conforme, segundo).",
        "Trocar um conector por outro de relação diferente muda o sentido do texto."
    ], [
        ("Anáfora x catáfora", "Anáfora retoma um termo já mencionado. Catáfora antecipa um termo que será mencionado."),
        ("Conectores de concessão", "Embora, ainda que, apesar de, mesmo que: indicam uma ideia contrária que não impede o fato principal."),
        ("Conectores de conclusão", "Logo, portanto, por isso, assim, então.")
    ], [
        Q("Em \"Embora o orçamento tenha sido ampliado, as metas não foram atingidas\", a oração iniciada por \"embora\" expressa ideia de",
          "concessão.",
          ["causa.", "condição.", "finalidade.", "conclusão."],
          "\"Embora\" introduz um fato que seria um obstáculo, mas não impediu o que se afirma na oração principal. É a ideia de concessão.", GRAM),
        Q("Em \"A agência ampliou o atendimento; no entanto, o número de reclamações cresceu\", a expressão \"no entanto\" pode ser substituída, sem alteração de sentido, por",
          "contudo.",
          ["portanto.", "porque.", "logo.", "além disso."],
          "\"No entanto\" e \"contudo\" expressam oposição. \"Portanto\" e \"logo\" indicam conclusão, \"porque\" indica causa e \"além disso\" indica adição.", GRAM),
        Q("Em \"O diretor apresentou o relatório. Ele destacou os resultados\", o pronome \"ele\" estabelece coesão",
          "referencial anafórica, pois retoma \"o diretor\".",
          ["referencial catafórica, pois antecipa um termo seguinte.", "sequencial por oposição, pois contrasta duas ideias.", "por elipse, pois omite o sujeito.", "por substituição lexical, pois usa um sinônimo."],
          "O pronome retoma um termo já mencionado (\"o diretor\"), o que caracteriza anáfora.", GRAM),
        Q("Em \"Choveu muito, de modo que o evento foi cancelado\", a locução \"de modo que\" introduz uma oração que expressa",
          "consequência.",
          ["causa.", "concessão.", "condição.", "finalidade."],
          "\"De modo que\" liga uma consequência ao fato anterior (a chuva forte teve como resultado o cancelamento).", GRAM),
    ]),
    L("pcoe-l2", "Tempos e modos verbais", 7, [
        "Indicativo expressa fatos e certezas. Subjuntivo expressa dúvida, hipótese, desejo e condição. Imperativo expressa ordem, pedido ou conselho.",
        "Correlações clássicas: \"Se eu tivesse tempo, revisaria o texto\" (pretérito imperfeito do subjuntivo + futuro do pretérito). \"Se a equipe cumprir os prazos, o projeto será concluído\" (futuro do subjuntivo + futuro do presente).",
        "Futuro do subjuntivo de verbos irregulares: vir: quando eu vier; ver: se eu vir; fazer: se ele fizer; trazer: se ele trouxer; pôr: se ele puser; querer: se quiser; haver: se houver; dizer: se disser.",
        "Cuidado com a confusão entre \"vir\" (futuro do subjuntivo de ver) e \"vier\" (futuro do subjuntivo de vir)."
    ], [
        ("Se + futuro do subjuntivo", "Pede verbo no futuro do presente: \"Se você fizer, receberá\"."),
        ("Se + pretérito imperfeito do subjuntivo", "Pede futuro do pretérito: \"Se eu tivesse tempo, faria\"."),
        ("Futuro do subjuntivo de \"ver\" e de \"vir\"", "Ver: quando eu vir. Vir: quando eu vier.")
    ], [
        Q("Complete: \"Se a equipe ___ os prazos, o projeto será concluído a tempo.\"",
          "cumprir",
          ["cumprisse", "cumpriria", "cumpre", "cumprirá"],
          "Oração condicional com \"se\" e verbo principal no futuro do presente pede futuro do subjuntivo: cumprir.", GRAM),
        Q("Complete: \"Quando você ___ ao escritório, procure o setor de pessoal.\"",
          "vier",
          ["vir", "vem", "viesse", "venha"],
          "\"Quando\" com ideia de futuro pede futuro do subjuntivo. O de \"vir\" é \"vier\"; \"vir\" é o futuro do subjuntivo de \"ver\".", GRAM),
        Q("Complete: \"Se eu ___ mais tempo, revisaria o texto com calma.\"",
          "tivesse",
          ["tiver", "tenho", "terei", "tinha tido"],
          "A hipótese irreal no passado pede pretérito imperfeito do subjuntivo (tivesse) em correlação com o futuro do pretérito (revisaria).", GRAM),
        Q("Complete: \"Se você ___ o relatório pronto, avise-me.\"",
          "vir",
          ["ver", "veja", "visse", "viu"],
          "Futuro do subjuntivo do verbo \"ver\": quando eu vir, se você vir.", GRAM),
    ]),
], semente=2)

# ---------------------------------------------------------------- sintaxe, concordância, regência
escrever("u-port-sintaxe", "Classes de palavras, período, concordância e regência", "Gerais", "port", ["port-05"], [
    L("psin-l1", "Classes de palavras, coordenação e subordinação", 8, [
        "Classes: substantivo, adjetivo, artigo, numeral, pronome, verbo, advérbio, preposição, conjunção e interjeição.",
        "Coordenação liga orações independentes. Sindéticas: aditiva (e, nem), adversativa (mas, porém, contudo), alternativa (ou), conclusiva (logo, portanto) e explicativa (pois, porque).",
        "Subordinação liga orações dependentes: substantivas (funcionam como sujeito, objeto, predicativo etc., com \"que\" ou \"se\"), adjetivas (introduzidas por pronome relativo) e adverbiais (causa, concessão, condição, finalidade, tempo).",
        "Adjetiva restritiva restringe o termo e não tem vírgula. Adjetiva explicativa acrescenta uma informação e vem entre vírgulas."
    ], [
        ("Oração coordenada adversativa", "Expressa oposição: mas, porém, contudo, todavia, no entanto."),
        ("Oração substantiva subjetiva", "Funciona como sujeito de outra oração: \"É necessário que todos participem\"."),
        ("Adjetiva restritiva x explicativa", "Restritiva: sem vírgulas, limita o termo. Explicativa: entre vírgulas, só acrescenta informação.")
    ], [
        Q("Em \"Estudei bastante, mas não passei\", a segunda oração é coordenada",
          "sindética adversativa.",
          ["sindética aditiva.", "sindética conclusiva.", "assindética.", "sindética explicativa."],
          "\"Mas\" liga orações com ideia de oposição.", GRAM),
        Q("Em \"É necessário que todos participem\", a oração \"que todos participem\" é subordinada substantiva",
          "subjetiva, pois funciona como sujeito de \"é necessário\".",
          ["objetiva direta, pois completa um verbo transitivo.", "adjetiva restritiva, pois qualifica um substantivo.", "adverbial de finalidade.", "coordenada aditiva."],
          "Pode-se reescrever: \"A participação de todos é necessária\". A oração substitui o sujeito.", GRAM),
        Q("Em \"O relatório que você enviou está completo\", o \"que\" é",
          "pronome relativo, pois retoma \"o relatório\" e introduz oração adjetiva.",
          ["conjunção integrante, pois introduz oração substantiva.", "conjunção causal, pois indica a causa.", "advérbio de intensidade.", "pronome interrogativo."],
          "O \"que\" pode ser substituído por \"o qual\" e exerce função sintática de objeto direto de \"enviou\".", GRAM),
        Q("Em \"Chegou tarde porque perdeu o ônibus\", a oração \"porque perdeu o ônibus\" é subordinada adverbial",
          "causal.",
          ["concessiva.", "condicional.", "final.", "temporal."],
          "A oração expressa a causa do atraso.", GRAM),
    ]),
    L("psin-l2", "Concordância verbal e nominal", 8, [
        "O verbo concorda com o sujeito. \"Mais de um\" leva o verbo ao singular. Coletivos no singular levam o verbo ao singular.",
        "Haver no sentido de existir é impessoal, sempre no singular: \"Há muitos candidatos\", \"Houve problemas\". Fazer indicando tempo também fica no singular: \"Faz dois anos\".",
        "Na voz passiva sintética, o verbo concorda com o sujeito: \"Vendem-se casas\", \"Alugam-se salas\". Com verbo transitivo indireto, fica no singular: \"Precisa-se de técnicos\".",
        "Concordância nominal: anexo, incluso e obrigado concordam com o substantivo a que se referem (\"seguem anexos os documentos\"). \"Meio\" advérbio é invariável (\"meio cansada\"). \"É proibida a entrada\" concorda; \"é proibido entrada\" (sem artigo) fica invariável."
    ], [
        ("Verbo haver no sentido de existir", "Impessoal, sempre no singular: \"Há muitos candidatos\", \"Houve problemas\"."),
        ("Voz passiva sintética x transitivo indireto", "\"Vendem-se casas\" (concorda). \"Precisa-se de técnicos\" (singular, com preposição)."),
        ("Anexo, incluso, obrigado", "Concordam com o substantivo: \"seguem anexos os documentos\", \"obrigada\" dita por mulher.")
    ], [
        Q("Assinale a frase em que a concordância verbal está de acordo com a norma-padrão.",
          "Mais de um candidato foi aprovado nesta etapa.",
          ["Fazem dois anos que ele trabalha aqui.", "Haviam candidatos suficientes para a vaga.", "Aluga-se salas comerciais no centro.", "Precisam-se de analistas de comunicação."],
          "\"Mais de um\" leva o verbo ao singular. \"Fazer\" e \"haver\" impessoais ficam no singular; \"alugam-se salas\" concorda com o sujeito; \"precisa-se de\" fica no singular.", GRAM),
        Q("Assinale a frase correta quanto à concordância nominal e verbal.",
          "Seguem anexos os documentos solicitados.",
          ["Segue anexo os documentos solicitados.", "Seguem anexo os documentos solicitados.", "Segue anexos os documentos solicitados.", "Seguem anexas os documentos solicitados."],
          "O verbo concorda com o sujeito posposto (\"os documentos\"), e \"anexos\" concorda com o substantivo.", GRAM),
        Q("Assinale a frase em que há concordância adequada.",
          "É proibida a entrada de pessoas não autorizadas.",
          ["É proibido a entrada de pessoas não autorizadas.", "São proibido a entrada de pessoas não autorizadas.", "É proibida entradas de pessoas não autorizadas.", "É proibido a entradas de pessoas não autorizadas."],
          "Havendo artigo (\"a entrada\"), o adjetivo concorda com o substantivo: \"proibida\". O sujeito é singular, logo \"é\".", GRAM),
        Q("Assinale a frase em que o uso de \"meio\" e \"meia\" está correto.",
          "Ela chegou meio cansada ao meio-dia e meia.",
          ["Ela chegou meia cansada ao meio-dia e meio.", "Ela chegou meio cansada ao meia-dia e meia.", "Ela chegou meia cansada ao meia-dia e meio.", "Ela chegou meios cansada ao meio-dia e meia."],
          "\"Meio\" como advérbio (= um pouco) é invariável. \"Meio-dia\" é masculino. \"Meia\" refere-se a \"meia hora\".", GRAM),
    ]),
    L("psin-l3", "Regência verbal e nominal", 8, [
        "Assistir no sentido de ver exige a preposição \"a\": \"Assistimos ao evento\". Assistir no sentido de ajudar é transitivo direto.",
        "Preferir: \"Prefiro A a B\", sem \"do que\" nem \"mais\". Obedecer e desobedecer exigem \"a\". Chegar e ir pedem \"a\", e não \"em\": \"chegou ao escritório\".",
        "Informar: \"informar alguém de/sobre algo\" ou \"informar algo a alguém\". Visar no sentido de ter como objetivo exige \"a\". Aspirar no sentido de desejar exige \"a\".",
        "Regência nominal: obediência a, respeito a ou por, residente em, apto a ou para, direito a, falta de."
    ], [
        ("Preferir", "\"Prefiro trabalhar em equipe a trabalhar sozinho\". Evite \"do que\" e \"mais\"."),
        ("Assistir (ver)", "Transitivo indireto: assistir a um filme, a uma palestra."),
        ("Chegar e ir", "Pedem a preposição \"a\": chegou ao escritório, foi ao banco.")
    ], [
        Q("Complete: \"Todos os servidores assistiram ___ evento de abertura.\"",
          "ao",
          ["o", "no", "do", "pelo"],
          "Assistir no sentido de ver exige a preposição \"a\", que se une ao artigo: \"ao evento\".", GRAM),
        Q("Complete: \"Prefiro trabalhar em equipe ___ trabalhar sozinho.\"",
          "a",
          ["do que", "mais que", "que", "ao invés de"],
          "O verbo preferir exige o complemento com \"a\": \"prefiro X a Y\".", GRAM),
        Q("Complete: \"A diretoria informou os empregados ___ mudança de horário.\"",
          "da",
          ["à", "pela", "na", "com a"],
          "Informar alguém de algo: \"informou os empregados da mudança\".", GRAM),
        Q("Complete: \"Os empregados devem obediência ___ regulamento de ética.\"",
          "ao",
          ["do", "pelo", "no", "com o"],
          "O substantivo \"obediência\" rege a preposição \"a\", como o verbo \"obedecer\".", GRAM),
    ]),
], semente=1)

# ---------------------------------------------------------------- pontuação, crase, colocação pronominal
escrever("u-port-crase-pontuacao", "Pontuação, crase e colocação pronominal", "Gerais", "port", ["port-05"], [
    L("pcp-l1", "Pontuação: a vírgula", 8, [
        "Usa-se vírgula para separar itens de enumeração, isolar vocativo, aposto, expressões explicativas (isto é, ou seja), adjuntos adverbiais deslocados e orações adjetivas explicativas, e antes de conjunções adversativas (mas, porém).",
        "Não se separa por vírgula: sujeito e verbo, verbo e complemento, nome e complemento nominal.",
        "Aposto é explicação do termo anterior e vem entre vírgulas: \"Maria Silva, coordenadora de comunicação, apresentou o plano\".",
        "Dois-pontos introduzem enumeração, citação ou explicação. Ponto e vírgula separa itens longos de enumeração ou orações que já contêm vírgulas."
    ], [
        ("Vírgula entre sujeito e verbo", "Não se usa, a menos que haja termo intercalado entre vírgulas."),
        ("Aposto", "Explica um termo e vem isolado por vírgulas."),
        ("Vírgula antes de \"mas\"", "É usada: \"Planejamos a campanha, mas não conseguimos executá-la\".")
    ], [
        Q("Assinale a frase com a pontuação correta.",
          "Os resultados, divulgados ontem, surpreenderam a diretoria.",
          ["Os resultados divulgados ontem, surpreenderam a diretoria.", "Os resultados, divulgados ontem surpreenderam, a diretoria.", "Os resultados divulgados, ontem surpreenderam a diretoria.", "Os resultados divulgados ontem surpreenderam, a diretoria."],
          "O trecho \"divulgados ontem\" é intercalado e vem entre vírgulas. As outras alternativas separam sujeito e verbo ou o verbo do complemento.", GRAM),
        Q("Assinale a frase com a pontuação correta.",
          "Ao final da reunião, o presidente agradeceu os participantes.",
          ["Ao final da reunião o presidente, agradeceu os participantes.", "Ao final, da reunião o presidente agradeceu os participantes.", "Ao final da reunião o presidente agradeceu, os participantes.", "Ao final da reunião o presidente agradeceu os, participantes."],
          "Adjunto adverbial deslocado para o início é separado por vírgula. As demais separam termos que não podem ser separados.", GRAM),
        Q("Assinale a frase em que o aposto está corretamente pontuado.",
          "Maria Silva, coordenadora de comunicação, apresentou o plano.",
          ["Maria Silva coordenadora de comunicação, apresentou o plano.", "Maria Silva, coordenadora de comunicação apresentou o plano.", "Maria, Silva coordenadora de comunicação, apresentou o plano.", "Maria Silva coordenadora, de comunicação apresentou o plano."],
          "O aposto \"coordenadora de comunicação\" é isolado por duas vírgulas.", GRAM),
        Q("Assinale a frase com a pontuação correta.",
          "Planejamos a campanha, mas não conseguimos executá-la.",
          ["Planejamos a campanha mas, não conseguimos executá-la.", "Planejamos, a campanha mas não conseguimos executá-la.", "Planejamos a campanha mas não, conseguimos executá-la.", "Planejamos a campanha mas não conseguimos, executá-la."],
          "A conjunção adversativa \"mas\" é precedida de vírgula. As outras posições separam verbo e complemento.", GRAM),
    ]),
    L("pcp-l2", "Emprego da crase", 7, [
        "Crase é a fusão da preposição \"a\" com o artigo \"a(s)\" ou com o início de \"aquele\", \"aquela\", \"aquilo\". Só ocorre antes de palavra feminina que aceita artigo e exigida por termo que pede \"a\".",
        "Obrigatória: \"Dirija-se à sala\", \"às 14h\", \"à tarde\", \"à noite\", \"à medida que\", \"à luz de\".",
        "Proibida: antes de palavra masculina (\"a pé\"), verbo (\"a partir\"), pronome pessoal (\"a ela\"), pronome de tratamento, expressões repetidas (\"gota a gota\") e cidade sem determinante.",
        "Truque: troque por um verbo que peça \"de\". Se aparecer \"da\", há crase: \"Volto da Bahia\" (vou à Bahia); \"Volto de Brasília\" (vou a Brasília)."
    ], [
        ("Truque da crase", "Se o verbo \"voltar\" pedir \"da\" antes do nome, há crase (Volto da Bahia, vou à Bahia). Se pedir \"de\", não há (Volto de Brasília, vou a Brasília)."),
        ("Crase antes de horas", "Há crase antes de horas determinadas: \"às 14h\", \"à meia-noite\"."),
        ("Crase antes de verbos", "Nunca há crase antes de verbo: \"a partir de\", \"a fazer\".")
    ], [
        Q("Complete: \"Os candidatos devem se dirigir ___ sala indicada no edital.\"",
          "à",
          ["a", "há", "a a", "à à"],
          "\"Dirigir-se\" pede \"a\" e \"sala\" é feminino com artigo: a + a = à.", GRAM),
        Q("Complete: \"A reunião começará ___ 14h.\"",
          "às",
          ["as", "a", "há", "à"],
          "Horas determinadas pedem a preposição \"a\" e o artigo feminino plural: \"às 14h\".", GRAM),
        Q("Complete: \"Ele se referiu ___ ela com respeito.\"",
          "a",
          ["à", "há", "ao", "as"],
          "Não há crase antes de pronome pessoal.", GRAM),
        Q("Assinale a alternativa em que o uso do acento grave está correto.",
          "Viajamos à Bahia e depois voltamos a Brasília.",
          ["Viajamos a Bahia e voltamos à Brasília.", "Viajamos à Brasília e voltamos a Bahia.", "Fomos à pé até o escritório.", "Entregou o documento à ele."],
          "\"Volto da Bahia\" confirma a crase em \"à Bahia\". \"Volto de Brasília\" indica que não há crase. Não há crase antes de masculino (\"a pé\") nem de pronome pessoal (\"a ele\").", GRAM),
    ]),
    L("pcp-l3", "Colocação dos pronomes átonos", 7, [
        "Próclise (pronome antes do verbo): ocorre com palavras atrativas, como negação (não, nunca), advérbios sem pausa (já, sempre, ainda), pronomes relativos e indefinidos, e conjunções subordinativas (que, se, quando).",
        "Ênclise (pronome depois): ocorre quando o verbo inicia a oração, com imperativo afirmativo (\"Envie-me os dados\") e com infinitivo e gerúndio sem atrativo.",
        "Mesóclise (pronome no meio): ocorre com o futuro do presente e o futuro do pretérito quando não há atrativo: \"Entregar-lhe-ei o documento amanhã\".",
        "Na norma-padrão, não se inicia frase com pronome átono."
    ], [
        ("Próclise", "Pronome antes do verbo, atraído por negação, relativos, indefinidos e conjunções subordinativas."),
        ("Ênclise", "Pronome depois do verbo: verbo no início, imperativo afirmativo."),
        ("Mesóclise", "Pronome no meio do verbo, com futuro do presente ou do pretérito sem atrativo: \"dar-lhe-ei\".")
    ], [
        Q("Complete: \"Nunca ___ esqueceremos esse dia.\"",
          "nos",
          ["esqueceremos-nos", "esquecer-nos-emos", "nos-esqueceremos", "esqueceremo-nos"],
          "O advérbio de negação \"nunca\" é palavra atrativa e exige próclise: \"nunca nos esqueceremos\".", GRAM),
        Q("Assinale a alternativa que reescreve \"Entregarei o documento a você amanhã\" substituindo \"a você\" por pronome átono, de acordo com a norma-padrão.",
          "Entregar-lhe-ei o documento amanhã.",
          ["Lhe entregarei o documento amanhã.", "Entregarei-lhe o documento amanhã.", "Entregar-lhe-ia o documento amanhã.", "Lhe entregar-ei o documento amanhã."],
          "Verbo no futuro do presente sem palavra atrativa pede mesóclise. Não se inicia a frase com pronome átono.", GRAM),
        Q("Assinale a frase em que a colocação do pronome está de acordo com a norma-padrão.",
          "Envie-me os dados ainda hoje.",
          ["Me envie os dados ainda hoje.", "Me enviem os dados ainda hoje.", "Enviem me os dados ainda hoje.", "Envie os dados me ainda hoje."],
          "Imperativo afirmativo pede ênclise: \"envie-me\".", GRAM),
        Q("Assinale a frase em que a colocação do pronome está correta.",
          "O servidor que me atendeu foi cordial.",
          ["O servidor que atendeu-me foi cordial.", "O servidor que atendeu me foi cordial.", "O servidor me que atendeu foi cordial.", "O servidor atendeu-me que foi cordial."],
          "O pronome relativo \"que\" é atrativo e exige próclise: \"que me atendeu\".", GRAM),
    ]),
], semente=3)

# ---------------------------------------------------------------- reescrita
escrever("u-port-reescrita", "Reescrita de frases e parágrafos", "Gerais", "port", ["port-06"], [
    L("pree-l1", "Significação das palavras e parônimos", 7, [
        "Em reescrita, a palavra deve ser substituída por outra de sentido equivalente no contexto, sem mudar a ideia.",
        "Pares que mais confundem: ratificar (confirmar) e retificar (corrigir); infringir (violar) e infligir (aplicar pena); tráfego (trânsito) e tráfico (comércio ilegal); discriminar (distinguir) e descriminar (tirar o caráter de crime).",
        "Mais pares: eminente (notável) e iminente (prestes a ocorrer); cumprimento (saudação) e comprimento (extensão); ascender (subir) e acender (pôr fogo); emergir (vir à tona) e imergir (mergulhar)."
    ], [
        ("Ratificar x retificar", "Ratificar é confirmar. Retificar é corrigir."),
        ("Infringir x infligir", "Infringir é violar (a lei). Infligir é aplicar (uma pena)."),
        ("Eminente x iminente", "Eminente é ilustre. Iminente é o que está prestes a acontecer.")
    ], [
        Q("Assinale a alternativa em que a palavra destacada está empregada corretamente.",
          "A decisão do diretor foi ratificada pelo Conselho, que confirmou seus termos.",
          ["O fiscal ratificou o erro do documento, corrigindo as datas.", "O Conselho infringiu penalidade ao funcionário.", "Havia grande tráfico de veículos na avenida.", "O candidato foi descriminado por sua origem."],
          "Ratificar é confirmar. Para corrigir, usa-se retificar; para aplicar pena, infligir; para trânsito, tráfego; para distinguir de forma injusta, discriminar.", GRAM),
        Q("Assinale a alternativa em que a palavra está empregada corretamente.",
          "O risco de falha no sistema é iminente, e as equipes já estão em alerta.",
          ["O iminente professor proferiu a palestra de abertura.", "A iminente autoridade presidiu a cerimônia.", "O iminente jurista recebeu o prêmio.", "Ele é um iminente especialista em direito."],
          "Iminente significa prestes a acontecer. Para pessoas ilustres, usa-se eminente.", GRAM),
        Q("Assinale a alternativa em que a palavra está empregada corretamente.",
          "Os candidatos receberam o cumprimento da diretora ao chegarem.",
          ["O comprimento da diretora foi cordial e caloroso ao receber os candidatos.", "O cumprimento da mesa é de três metros.", "O cumprimento do terreno é de vinte metros.", "Mediu o cumprimento da sala com a trena."],
          "Cumprimento é saudação. Comprimento é a medida de extensão.", GRAM),
        Q("Assinale a alternativa em que a palavra está empregada corretamente.",
          "Ela ascendeu na carreira por mérito.",
          ["Ela acendeu na carreira por mérito.", "O afogado imergiu à superfície.", "O submarino emergiu nas profundezas.", "Ele ascendeu o fogo da lareira."],
          "Ascender é subir. Acender é pôr fogo. Emergir é vir à tona, e imergir é mergulhar.", GRAM),
    ]),
    L("pree-l2", "Reorganização de períodos e níveis de formalidade", 8, [
        "Reescrever bem é manter o sentido, a correção gramatical (concordância, regência, crase) e o registro adequado.",
        "Voz passiva: \"A comissão avaliou todos os projetos\" equivale a \"Todos os projetos foram avaliados pela comissão\". Mudar o tempo verbal ou inverter agente e paciente muda o sentido.",
        "Conectores equivalentes: \"caso\" e \"se\" (condição). \"Embora\" e \"apesar de\" (concessão). Não troque por conector de relação diferente.",
        "Redação oficial pede formalidade, impessoalidade, clareza, concisão e uso da norma-padrão. Evita gírias, contrações informais (\"pra\") e vocativos coloquiais."
    ], [
        ("Voz ativa e passiva", "O agente da ativa vira agente da passiva: \"A comissão avaliou os projetos\" e \"Os projetos foram avaliados pela comissão\"."),
        ("Caso e se", "Ambos podem introduzir condição: \"Caso o prazo seja prorrogado\" e \"Se o prazo for prorrogado\"."),
        ("Registro formal", "Norma-padrão, impessoalidade, objetividade, sem gírias nem expressões coloquiais.")
    ], [
        Q("Assinale a reescrita de \"A comissão avaliou todos os projetos\" que mantém o sentido e a correção gramatical.",
          "Todos os projetos foram avaliados pela comissão.",
          ["Todos os projetos avaliaram a comissão.", "Todos os projetos foi avaliado pela comissão.", "Todos os projetos serão avaliados pela comissão.", "A comissão foi avaliada por todos os projetos."],
          "Na voz passiva, o objeto vira sujeito e concorda com o verbo (\"foram avaliados\"). A mudança para \"serão\" altera o tempo, e a inversão de papéis muda o sentido.", GRAM),
        Q("Assinale a reescrita de \"Caso o prazo seja prorrogado, os candidatos serão avisados\" que preserva o sentido.",
          "Se o prazo for prorrogado, os candidatos serão avisados.",
          ["Embora o prazo seja prorrogado, os candidatos serão avisados.", "Porque o prazo for prorrogado, os candidatos serão avisados.", "Apesar de o prazo ser prorrogado, os candidatos serão avisados.", "Quando o prazo foi prorrogado, os candidatos serão avisados."],
          "\"Caso\" e \"se\" expressam condição. As outras opções introduzem concessão, causa ou tempo, mudando o sentido.", GRAM),
        Q("Para um comunicado oficial, a reescrita mais adequada de \"Cara galera, o evento foi adiado pra semana que vem\" é",
          "Comunicamos que o evento foi adiado para a semana seguinte.",
          ["Pessoal, o evento foi adiado pra semana que vem, beleza?", "Galera, o evento ficou pra depois, tá?", "Avisamos que o rolê foi adiado.", "Atenção, pessoal: o evento foi pra semana que vem."],
          "O comunicado oficial pede registro formal e impessoal, sem gírias ou contrações informais.", REDOF),
        Q("São características da redação oficial todas as seguintes, EXCETO",
          "uso de gírias e expressão pessoal para aproximar-se do leitor.",
          ["impessoalidade.", "clareza e concisão.", "formalidade e padronização.", "uso da norma-padrão da língua portuguesa."],
          "A redação oficial é impessoal, clara, concisa, formal e padronizada. Gírias e personalismo vão contra esses princípios.", REDOF),
    ]),
], semente=4)
