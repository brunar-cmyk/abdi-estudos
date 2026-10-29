from lib import Q, L, escrever

CHI = "Referência conceitual: R. Chinem, Assessoria de Imprensa: como fazer; J. Duarte (org.), Assessoria de Imprensa e Relacionamento com a Mídia"
LAGE = "Referência conceitual: N. Lage, A Reportagem: teoria e técnica de entrevista e pesquisa jornalística"
MEL = "Referência conceitual: J. Marques de Melo e S. Assis, Gêneros e Formatos Jornalísticos"
MAN = "Referência conceitual: manuais de redação de veículos de imprensa brasileiros (lide, pirâmide invertida e padronização)"
BUE = "Referência conceitual: W. C. Bueno, Comunicação científica e divulgação científica: aproximações e rupturas conceituais"
DIG = "Referência conceitual: marketing de conteúdo e comunicação digital (práticas consolidadas de SEO, UX e métricas)"
DES = "Referência conceitual: fundamentos de design gráfico e de produção gráfica"
AUD = "Referência conceitual: fundamentos de fotografia, vídeo e áudio"

# ------------------------------------------------------------------ assessoria, imprensa, gêneros
escrever("u-esp-assessoria-imprensa", "Assessoria de comunicação e de imprensa, relacionamento com a imprensa e gêneros jornalísticos",
         "Específicos", "esp", ["esp-07", "esp-08", "esp-09"], [
    L("aim-l1", "Assessoria de comunicação e assessoria de imprensa", 8, [
        "Assessoria de comunicação é a estrutura que planeja e executa a comunicação de uma organização. Abrange imprensa, relações públicas, comunicação interna e digital, eventos e identidade visual.",
        "Assessoria de imprensa cuida do relacionamento com a mídia: atende jornalistas, sugere pautas, escreve releases e notas, organiza entrevistas, monitora e analisa o que sai publicado.",
        "Instrumentos: release (texto enviado à imprensa), mailing (lista segmentada de contatos de imprensa), press kit (material de apoio: release, fotos, perfis e dados), clipping (coleta e análise das matérias publicadas) e media training (treinamento de porta-vozes).",
        "O resultado da assessoria é mídia espontânea (conquistada): a matéria sai porque o veículo julgou relevante, e a organização não paga por ela. Mídia paga é a publicidade.",
        "O assessor não manda na pauta: o jornalista decide se publica. Por isso o trabalho exige informação de interesse público, rapidez e credibilidade."
    ], [
        ("Clipping", "Coleta, organização e análise das matérias publicadas sobre a organização."),
        ("Mailing", "Lista segmentada de contatos de imprensa para o envio de releases e sugestões de pauta."),
        ("Media training", "Treinamento de porta-vozes para dar entrevistas.")
    ], [
        Q("Em assessoria de imprensa, o clipping consiste em",
          "coletar, organizar e analisar as matérias publicadas na mídia sobre a organização.",
          ["comprar espaço publicitário em veículos de comunicação.", "treinar porta-vozes para entrevistas.", "organizar uma coletiva de imprensa.", "elaborar o manual de identidade visual."],
          "O clipping reúne as aparições na mídia e permite medir presença, tom e temas.", CHI),
        Q("Uma lista de contatos de jornalistas e veículos, organizada por editorias e interesses, usada para o envio de releases, é chamada de",
          "mailing.",
          ["clipping.", "briefing.", "press kit.", "media training."],
          "Mailing é o cadastro segmentado de contatos de imprensa.", CHI),
        Q("A matéria publicada por um veículo, sem pagamento, porque o jornalista a considerou relevante a partir de uma sugestão de pauta da assessoria, é exemplo de",
          "mídia espontânea (ou conquistada).",
          ["mídia paga.", "publicidade institucional.", "patrocínio.", "propaganda eleitoral."],
          "Mídia espontânea é fruto do trabalho de relacionamento, sem compra de espaço.", CHI),
        Q("O treinamento voltado a preparar dirigentes e técnicos para falar com jornalistas, com simulações de entrevista, é conhecido como",
          "media training.",
          ["social listening.", "benchmarking.", "brainstorming.", "merchandising."],
          "O media training prepara o porta-voz para dar entrevistas com clareza e segurança.", CHI),
    ]),
    L("aim-l2", "Relacionamento com a imprensa e fontes de informação", 9, [
        "Boas práticas: transparência, agilidade, respeito ao prazo de fechamento (deadline), credibilidade e tratamento igualitário dos veículos, salvo exclusividade previamente acordada. Não se mente a jornalista.",
        "Fontes de informação: oficiais (instituições e seus representantes), oficiosas (próximas à fonte oficial, mas sem autorização para falar em nome dela) e independentes (sem vínculo direto com o fato). Há também fontes especializadas, testemunhais e documentais.",
        "Regras de entrevista: on the record (pode publicar e atribuir), off the record (a informação não pode ser publicada nem atribuída), background (pode ser usada, sem identificar a fonte) e embargo (a informação só pode ser publicada a partir de data e hora combinadas).",
        "Instrumentos de relacionamento: sugestão de pauta, nota oficial, entrevista individual, coletiva de imprensa e visita à redação. É recomendável designar um porta-voz ou poucos porta-vozes."
    ], [
        ("Fonte oficiosa", "Próxima à fonte oficial, mas sem autorização para falar em nome da organização."),
        ("Off the record", "Informação que o jornalista não pode publicar nem atribuir à fonte."),
        ("Embargo", "Informação liberada com antecedência, para publicação só a partir de data e hora combinadas.")
    ], [
        Q("Uma pessoa próxima ao presidente de uma instituição, que repassa informações sem autorização para falar em nome da instituição, é classificada como fonte",
          "oficiosa.",
          ["oficial.", "independente.", "documental.", "testemunhal."],
          "A fonte oficiosa tem proximidade com a fonte oficial, mas não fala oficialmente por ela.", LAGE),
        Q("Quando uma fonte informa algo ao jornalista em caráter \"off the record\", isso significa que a informação",
          "não pode ser publicada nem atribuída à fonte.",
          ["deve ser publicada, com identificação da fonte.", "pode ser publicada, com a identificação da fonte.", "pode ser publicada, mas sem citar o veículo.", "deve ser publicada apenas depois de uma semana."],
          "Off the record é combinado de confidencialidade: o jornalista não publica nem atribui.", LAGE),
        Q("Uma assessoria envia a jornalistas um comunicado com data e hora a partir das quais a informação poderá ser divulgada. Essa prática é conhecida como",
          "embargo.",
          ["clipping.", "background.", "mailing.", "furo."],
          "No embargo, a informação é antecipada, mas só pode ser publicada a partir do momento combinado.", CHI),
        Q("Em um bom relacionamento com a imprensa, a assessoria deve",
          "responder com agilidade, respeitar os prazos de fechamento e dar tratamento igualitário aos veículos.",
          ["privilegiar sempre o veículo mais antigo.", "omitir informações incômodas dos jornalistas.", "exigir aprovação prévia do texto de todas as matérias.", "dar respostas apenas depois de publicada a matéria."],
          "Transparência, agilidade e credibilidade são a base. Exigir aprovação prévia de matéria fere a independência do jornalista.", CHI),
    ]),
    L("aim-l3", "Jornalismo do zero: critérios de noticiabilidade e gêneros", 10, [
        "Jornalismo é a atividade de apurar, selecionar, editar e publicar informações de interesse público. O jornalista verifica os fatos, ouve as partes e tem independência editorial.",
        "Valores-notícia, ou critérios de noticiabilidade, ajudam a decidir o que vira notícia: atualidade, proximidade, relevância e impacto, interesse público, conflito, proeminência dos envolvidos e caráter inusitado.",
        "Gêneros jornalísticos, na classificação de Marques de Melo: informativo (nota, notícia, reportagem, entrevista), opinativo (editorial, comentário, artigo, resenha, coluna, crônica, caricatura, carta), interpretativo (análise, perfil, enquete, cronologia, dossiê), diversional e utilitário (serviço, indicadores, roteiros).",
        "Notícia relata um fato recente de forma objetiva e relativamente curta. Reportagem aprofunda o tema, traz contexto, várias vozes e dados. Nota é uma informação breve. Entrevista dá voz a uma fonte, em perguntas e respostas ou em texto corrido.",
        "Para um comunicador de formação publicitária, a diferença-chave é a finalidade: o jornalismo busca informar de forma independente, e a publicidade busca persuadir em nome de um anunciante."
    ], [
        ("Valores-notícia (critérios de noticiabilidade)", "Atualidade, proximidade, relevância e impacto, interesse público, conflito, proeminência e caráter inusitado."),
        ("Notícia x reportagem", "Notícia relata o fato de forma objetiva e curta. Reportagem aprofunda, contextualiza e ouve várias vozes."),
        ("Gêneros opinativos", "Editorial, comentário, artigo, resenha, coluna, crônica, caricatura e carta.")
    ], [
        Q("De acordo com a classificação de gêneros jornalísticos de Marques de Melo, o editorial pertence ao gênero",
          "opinativo.",
          ["informativo.", "diversional.", "utilitário.", "publicitário."],
          "O editorial expressa a posição do veículo, o que o situa entre os gêneros opinativos.", MEL),
        Q("A diferença entre notícia e reportagem é que a reportagem tende a ser",
          "mais aprofundada, com contexto, dados e várias vozes, enquanto a notícia relata o fato recente de forma objetiva e curta.",
          ["mais curta, sem fontes.", "sempre opinativa.", "assinada apenas por assessores.", "escrita sem apuração."],
          "Notícia relata o fato. Reportagem amplia a abordagem e aprofunda o tema.", LAGE),
        Q("Entre os critérios de noticiabilidade (valores-notícia) usados para decidir se um fato merece ser publicado estão",
          "atualidade, proximidade, relevância e impacto, interesse público e proeminência dos envolvidos.",
          ["o tamanho da assessoria e a verba de publicidade.", "a simpatia do assessor de imprensa.", "o desejo do anunciante em aparecer.", "a quantidade de adjetivos no texto."],
          "São critérios editoriais, e não comerciais.", LAGE),
        Q("Textos de serviço, como indicadores, cotações e roteiros, que ajudam o leitor em decisões do dia a dia, enquadram-se no gênero",
          "utilitário.",
          ["opinativo.", "diversional.", "publicitário.", "ficcional."],
          "O gênero utilitário orienta o público com informações de serviço.", MEL),
    ]),
], semente=0)

# ------------------------------------------------------------------ redação, edição, ciência
escrever("u-esp-redacao-edicao-ciencia", "Redação jornalística, edição e revisão, comunicação científica, tecnológica e ambiental",
         "Específicos", "esp", ["esp-10", "esp-11", "esp-22"], [
    L("red-l1", "Redação jornalística: lide e pirâmide invertida", 8, [
        "Lide (lead) é o parágrafo de abertura da notícia. Ele responde, em geral, às perguntas: o quê, quem, quando, onde, como e por quê.",
        "Pirâmide invertida: as informações mais importantes vêm primeiro, em ordem decrescente de importância. Assim o leitor entende o essencial logo de início, e o texto pode ser cortado pelo fim sem perder o principal.",
        "Estrutura típica: título (informativo, com verbo, em geral no presente), linha fina ou subtítulo, lide e corpo do texto.",
        "Linguagem: clara, concisa e objetiva, com frases curtas, preferência pela voz ativa e sem adjetivos opinativos. As informações devem ser atribuídas às fontes, em discurso direto (entre aspas) ou indireto."
    ], [
        ("Lide", "Parágrafo de abertura da notícia que traz as informações essenciais: o quê, quem, quando, onde, como e por quê."),
        ("Pirâmide invertida", "Estrutura em que as informações mais importantes vêm primeiro, em ordem decrescente de importância."),
        ("Discurso direto x indireto", "Direto: reproduz a fala entre aspas. Indireto: relata a fala com as palavras do jornalista.")
    ], [
        Q("O lide de uma notícia tem como função principal",
          "apresentar logo no início as informações essenciais do fato, respondendo às perguntas básicas (o quê, quem, quando, onde, como e por quê).",
          ["apresentar a opinião do jornalista sobre o fato.", "reproduzir o texto integral do release da assessoria.", "deixar as informações essenciais para o final.", "apresentar apenas o título e a legenda."],
          "O lide resume o essencial e orienta a leitura do restante da notícia.", MAN),
        Q("Na técnica da pirâmide invertida, o texto jornalístico é organizado",
          "do mais importante para o menos importante.",
          ["do menos importante para o mais importante.", "em ordem cronológica, do início ao fim, sempre.", "com a conclusão no primeiro parágrafo e a opinião no último.", "sem hierarquia entre as informações."],
          "Os dados mais relevantes aparecem primeiro, o que facilita a leitura e a edição por cortes.", MAN),
        Q("Entre as características desejáveis da linguagem jornalística está",
          "a clareza, a concisão e a objetividade, com frases curtas e preferência pela voz ativa.",
          ["o uso de adjetivos opinativos para reforçar a mensagem.", "as frases longas e cheias de intercalações.", "o uso de jargões técnicos sem explicação.", "o tom promocional da organização."],
          "A notícia busca informar de modo claro e imparcial.", MAN),
        Q("Quando o jornalista escreve \"O presidente afirmou que as inscrições serão prorrogadas\", ele utiliza",
          "discurso indireto, atribuindo a informação à fonte.",
          ["discurso direto, entre aspas.", "opinião, sem atribuição.", "linguagem publicitária.", "um recurso de edição de imagem."],
          "No discurso indireto, a fala é relatada com palavras do jornalista, sem aspas, mas com atribuição.", MAN),
    ]),
    L("red-l2", "Release, nota, entrevista, artigo e texto institucional", 9, [
        "Release é o texto enviado à imprensa para sugerir pauta e divulgar informação. Para ser aproveitado, precisa ter relevância jornalística, linguagem objetiva (de notícia), título e lide claros, dados de contato e informações verificáveis. Deve evitar o tom publicitário e a adjetivação promocional.",
        "Nota é um texto curto e direto, com uma informação objetiva. Nota oficial é o posicionamento formal da organização sobre um assunto, útil em situações sensíveis ou de crise.",
        "Entrevista pode ser publicada em perguntas e respostas (pingue-pongue) ou em texto corrido. Exige pesquisa prévia, pauta de perguntas, gravação e checagem das informações. Perfil é o retrato de uma pessoa.",
        "Artigo é texto opinativo, assinado, em que o autor defende um ponto de vista com argumentos. Texto institucional é a voz da organização: apresenta sua missão, serviços e resultados, em linguagem clara, com tom formal e sem excesso de promoção."
    ], [
        ("Release adequado", "Tem relevância jornalística, linguagem objetiva, título e lide claros, dados de contato e evita tom publicitário."),
        ("Nota oficial", "Posicionamento formal da organização sobre um tema ou acontecimento, em texto curto."),
        ("Artigo", "Texto opinativo assinado, que defende uma tese com argumentos.")
    ], [
        Q("O release enviado por uma assessoria à imprensa tem maior chance de ser aproveitado quando",
          "apresenta informação de interesse público, em linguagem jornalística e objetiva, com dados de contato.",
          ["usa adjetivos elogiosos e slogans da organização.", "traz apenas o logotipo e o telefone.", "é longo, sem título e sem lide.", "é enviado a todos os veículos, sem segmentação."],
          "O release deve se parecer com uma notícia, com relevância e informações verificáveis.", CHI),
        Q("A manifestação formal de uma organização, em texto curto, sobre um assunto sensível ou acontecimento que a envolve é chamada de",
          "nota oficial.",
          ["artigo de opinião.", "editorial.", "crônica.", "resenha."],
          "A nota oficial registra o posicionamento da organização e é muito usada na gestão de crises.", CHI),
        Q("A entrevista publicada em formato de perguntas e respostas, reproduzindo o diálogo, é conhecida como",
          "pingue-pongue.",
          ["lide.", "editorial.", "mailing.", "release."],
          "O pingue-pongue mostra as perguntas do entrevistador e as respostas do entrevistado.", LAGE),
        Q("O texto opinativo, assinado, em que o autor defende um ponto de vista com argumentos, é o",
          "artigo.",
          ["release.", "nota.", "lide.", "clipping."],
          "O artigo é um gênero opinativo assinado.", MEL),
    ]),
    L("red-l3", "Edição e revisão de conteúdos", 8, [
        "Edição é a seleção, a hierarquização, o corte, a titulação e a padronização do conteúdo, para que ele atenda ao público e ao estilo do veículo ou da organização.",
        "Revisão é a conferência do texto final: ortografia, gramática, pontuação e também fatos, nomes, cargos, datas, números e siglas. Erros de informação prejudicam a credibilidade.",
        "Manual de redação ou guia de estilo padroniza grafias, formas de tratamento, siglas e uso de números, e garante coerência entre diferentes autores.",
        "Fluxo típico: pauta, apuração, redação, edição, revisão, aprovação e publicação. Checar fontes, dar crédito a fotos e a textos e respeitar direitos autorais fazem parte da edição responsável."
    ], [
        ("Edição x revisão", "Edição seleciona, hierarquiza, corta e titula. Revisão confere erros de língua e de informação (nomes, cargos, datas, números)."),
        ("Guia de estilo", "Documento que padroniza grafias, siglas, formas de tratamento e formatação."),
        ("O que conferir na revisão de fatos", "Nomes, cargos, datas, números, grafia de siglas e citações.")
    ], [
        Q("A etapa em que se confere o texto final, verificando ortografia, gramática, pontuação e, também, nomes, cargos, datas e números, é a",
          "revisão.",
          ["pauta.", "apuração.", "sugestão de pauta.", "distribuição."],
          "A revisão corrige erros de língua e de informação antes da publicação.", MAN),
        Q("A edição de um conteúdo envolve, entre outras ações,",
          "selecionar, hierarquizar, cortar, titular e padronizar o material.",
          ["apenas corrigir erros de digitação.", "criar o logotipo da organização.", "contratar fornecedores de impressão.", "definir a remuneração dos redatores."],
          "A edição organiza e qualifica o conteúdo, e a revisão faz a conferência final.", MAN),
        Q("O documento que padroniza grafias, siglas, formas de tratamento e outros critérios de redação em uma organização é o",
          "manual de redação (ou guia de estilo).",
          ["mailing.", "press kit.", "plano de cargos.", "termo de referência."],
          "O guia de estilo garante coerência entre textos de diferentes autores.", MAN),
        Q("Antes de publicar um comunicado que cita o nome e o cargo de um dirigente, a conduta mais adequada de revisão é",
          "conferir a grafia do nome e o cargo atual em fonte confiável.",
          ["confiar na memória do redator.", "copiar o cargo de um texto antigo.", "omitir o cargo para evitar erro.", "publicar e corrigir só se houver reclamação."],
          "Erros de nome e de cargo são comuns e prejudicam a credibilidade. A checagem faz parte da revisão.", MAN),
    ]),
    L("red-l4", "Comunicação científica, tecnológica e ambiental", 9, [
        "Disseminação científica é a circulação do conhecimento entre especialistas, como em periódicos e congressos. Divulgação científica traduz esse conhecimento para o público leigo, em linguagem acessível (Bueno). O jornalismo científico é uma forma de divulgação.",
        "Desafios: manter o rigor sem jargão, contextualizar resultados, indicar incertezas e limites, citar fontes e estudos e evitar o sensacionalismo e as promessas exageradas.",
        "Na comunicação tecnológica, vale explicar o problema que a inovação resolve, para quem e com que evidência, evitando tecnicismo. Na comunicação ambiental e de sustentabilidade, deve haver coerência entre o discurso e as práticas.",
        "Greenwashing é divulgar uma imagem ambientalmente responsável sem práticas que a sustentem, ou exagerando benefícios. Dados, metas e resultados verificáveis protegem a reputação.",
        "No Planejamento Estratégico 2024-2029 da ABDI, há objetivos de ampliar a maturidade digital e boas práticas ambientais, sociais e de governança no setor produtivo, temas centrais para a comunicação científica e tecnológica da Agência."
    ], [
        ("Divulgação x disseminação científica", "Divulgação: tradução para o público leigo. Disseminação: circulação entre especialistas."),
        ("Greenwashing", "Imagem ambientalmente responsável sem práticas que a sustentem, ou com benefícios exagerados."),
        ("Cuidados na comunicação de ciência", "Rigor, contexto, citação das fontes, indicação de incertezas e ausência de sensacionalismo.")
    ], [
        Q("Segundo a distinção de Wilson Bueno, a divulgação científica é a comunicação do conhecimento científico dirigida",
          "ao público leigo, com linguagem acessível, enquanto a disseminação ocorre entre especialistas.",
          ["apenas a especialistas, em periódicos.", "exclusivamente a investidores.", "somente a órgãos de controle.", "apenas a alunos de pós-graduação."],
          "Divulgação traduz o conhecimento para o grande público. A disseminação circula entre pares.", BUE),
        Q("Divulgar uma imagem de organização ambientalmente responsável, sem práticas que a sustentem, ou exagerando benefícios, caracteriza",
          "greenwashing.",
          ["benchmarking.", "endomarketing.", "merchandising.", "storytelling."],
          "Greenwashing é o discurso verde sem lastro nas práticas, e fere a credibilidade.", BUE),
        Q("Ao comunicar os resultados de uma pesquisa científica ao público em geral, a conduta mais adequada é",
          "explicar o estudo em linguagem acessível, indicar limites e incertezas e citar as fontes.",
          ["apresentar o resultado como verdade definitiva.", "usar linguagem técnica sem explicação.", "omitir a fonte do estudo.", "exagerar os benefícios para chamar atenção."],
          "A boa divulgação científica combina clareza, rigor e transparência sobre incertezas.", BUE),
        Q("Entre os cuidados ao divulgar uma inovação tecnológica de uma instituição, está",
          "explicar o problema que ela resolve e apresentar evidências, evitando promessas exageradas.",
          ["usar termos técnicos sem explicação, para impressionar.", "prometer resultados garantidos.", "omitir as limitações da tecnologia.", "evitar citar parceiros e fontes."],
          "A comunicação tecnológica deve ser acessível, honesta e apoiada em evidências.", BUE),
    ]),
], semente=1)

# ------------------------------------------------------------------ digital, redes, multimídia, audiovisual, design
escrever("u-esp-digital-midia", "Comunicação digital, redes sociais, multimídia, audiovisual e design", "Específicos", "esp",
         ["esp-13", "esp-14", "esp-15", "esp-16", "esp-17"], [
    L("dig-l1", "Comunicação digital e produção de conteúdo", 8, [
        "Conteúdo digital deve ser pensado para a persona (representação do público-alvo), com objetivo claro e formato adequado ao canal.",
        "SEO é o conjunto de técnicas para melhorar o posicionamento de páginas nos buscadores: palavras-chave relevantes, títulos e descrições claros, conteúdo útil e boa estrutura. CTA (call to action) é a chamada que convida o público a agir, como \"inscreva-se\".",
        "Funil de conteúdo: topo (atrair e informar), meio (engajar e aprofundar) e fundo (converter). Newsletter exige consentimento (opt-in) e opção de descadastro, em linha com a LGPD.",
        "Boas práticas: páginas responsivas, textos escaneáveis, linguagem simples e acessibilidade, como texto alternativo em imagens, legendas em vídeos e bom contraste."
    ], [
        ("SEO", "Técnicas para melhorar o posicionamento de páginas nos resultados de busca."),
        ("CTA (call to action)", "Chamada que convida o público a realizar uma ação, como se inscrever ou baixar um material."),
        ("Texto alternativo", "Descrição de uma imagem lida por leitores de tela, que garante acessibilidade.")
    ], [
        Q("O conjunto de técnicas que visa melhorar o posicionamento de páginas nos resultados dos mecanismos de busca é chamado de",
          "SEO.",
          ["CRM.", "CTR.", "ROI.", "KPI."],
          "SEO significa otimização para mecanismos de busca.", DIG),
        Q("A chamada em uma página ou peça, como \"Inscreva-se agora\", que convida o público a realizar uma ação, é um",
          "call to action (CTA).",
          ["briefing.", "mailing.", "storyboard.", "clipping."],
          "O CTA orienta o próximo passo do usuário.", DIG),
        Q("A representação semifictícia do público-alvo, construída a partir de dados e usada para orientar a produção de conteúdo, é a",
          "persona.",
          ["mailing.", "press kit.", "landing page.", "briefing."],
          "A persona ajuda a definir temas, linguagem e formatos.", DIG),
        Q("O recurso que descreve uma imagem em texto, para ser lido por leitores de tela, é o",
          "texto alternativo.",
          ["rodapé.", "hiperlink.", "metadado de gráfica.", "banner."],
          "O texto alternativo torna imagens acessíveis a pessoas com deficiência visual.", DIG),
    ]),
    L("dig-l2", "Redes sociais: planejamento, produção, monitoramento e métricas", 9, [
        "Planejar redes sociais é definir objetivos, públicos, tom de voz, linha editorial, formatos por plataforma e calendário editorial. A produção e a publicação seguem o calendário, com revisão.",
        "Monitoramento e escuta social (social listening) acompanham menções, comentários e tendências. A moderação define como responder a elogios, dúvidas, críticas e ataques.",
        "Alcance é o número de pessoas únicas que viram o conteúdo. Impressões são o total de exibições, incluindo repetidas. Engajamento reúne interações (curtidas, comentários, compartilhamentos, salvamentos).",
        "Taxa de engajamento = interações divididas pelo alcance (ou pelos seguidores). CTR = cliques divididos por impressões. CPM = custo por mil impressões. Seguidores e curtidas isolados são métricas de vaidade, que não provam resultado.",
        "Conteúdo orgânico não é pago. Conteúdo pago (impulsionamento ou anúncio) amplia o alcance. Relatórios devem relacionar as métricas aos objetivos do plano."
    ], [
        ("Alcance x impressões", "Alcance: pessoas únicas atingidas. Impressões: total de exibições, incluindo repetidas."),
        ("CTR", "Taxa de cliques: cliques divididos por impressões."),
        ("Calendário editorial", "Cronograma de temas, formatos, datas e responsáveis pelas publicações.")
    ], [
        Q("Em relatório de redes sociais, o número de pessoas únicas que visualizaram uma publicação é chamado de",
          "alcance.",
          ["impressões.", "engajamento.", "taxa de cliques.", "frequência de postagem."],
          "Alcance conta pessoas únicas. Impressões contam todas as exibições, inclusive as repetidas.", DIG),
        Q("Um anúncio teve 2.000 impressões e 50 cliques. A taxa de cliques (CTR) foi de",
          "2,5%.",
          ["0,25%.", "4%.", "25%.", "40%."],
          "CTR é 50 dividido por 2.000, o que dá 0,025, ou 2,5%.", DIG),
        Q("Uma publicação alcançou 6.000 pessoas e gerou 300 interações (curtidas, comentários e compartilhamentos). A taxa de engajamento sobre o alcance foi de",
          "5%.",
          ["0,5%.", "2%.", "20%.", "50%."],
          "300 dividido por 6.000 é 0,05, ou 5%.", DIG),
        Q("Um instrumento que organiza datas, temas, formatos, plataformas e responsáveis pelas publicações em um período é o",
          "calendário editorial.",
          ["clipping.", "mailing.", "press kit.", "manual de identidade."],
          "O calendário editorial dá previsibilidade e coerência à produção de conteúdo.", DIG),
    ]),
    L("dig-l3", "Conteúdo multimídia e comunicação audiovisual", 9, [
        "Conteúdo multimídia combina texto, imagem, áudio, vídeo, infográficos e interatividade. A narrativa transmídia expande a mesma história por várias plataformas, e cada uma contribui com uma parte. Reaproveitar um conteúdo em vários formatos reduz custos.",
        "Gestão de conteúdo usa um sistema de gerenciamento (CMS), banco de imagens com metadados e controle de direitos de uso e de crédito.",
        "Fotografia: enquadramento, luz e composição. A regra dos terços divide a imagem em nove partes e posiciona o ponto de interesse nas interseções. Planos: geral, médio, primeiro plano e close.",
        "Vídeo: roteiro (texto), storyboard (desenho das cenas), planos e movimentos de câmera, captação e edição. Áudio: microfone adequado, controle do ruído e direitos da trilha. Legendas e audiodescrição ampliam a acessibilidade."
    ], [
        ("Regra dos terços", "Divide a imagem em nove partes iguais e posiciona o elemento principal em uma das interseções."),
        ("Storyboard", "Sequência de desenhos ou imagens que planeja as cenas de um vídeo."),
        ("Narrativa transmídia", "Uma história expandida em várias plataformas, cada uma com uma parte do conteúdo.")
    ], [
        Q("Em fotografia, a regra dos terços recomenda",
          "posicionar o elemento principal em uma das interseções das linhas que dividem a imagem em nove partes.",
          ["centralizar sempre o elemento principal.", "usar apenas planos gerais.", "evitar qualquer espaço vazio.", "sempre usar flash."],
          "A regra dos terços cria composições equilibradas e dinâmicas.", AUD),
        Q("O planejamento visual de um vídeo, com desenhos ou imagens das cenas em sequência, é o",
          "storyboard.",
          ["clipping.", "release.", "mailing.", "benchmarking."],
          "O storyboard antecipa enquadramentos e sequência antes da gravação.", AUD),
        Q("O plano que mostra o rosto de uma pessoa em detalhe, com destaque para expressões, é o",
          "close (ou primeiríssimo plano).",
          ["plano geral.", "plano médio.", "plano-sequência.", "plano de conjunto."],
          "O close aproxima a câmera do rosto ou de um detalhe.", AUD),
        Q("A narrativa em que uma mesma história é expandida por várias plataformas, com cada uma contribuindo com uma parte do conteúdo, é chamada de",
          "transmídia.",
          ["monomídia.", "unimídia.", "mídia paga.", "mídia espontânea."],
          "Na narrativa transmídia, cada plataforma acrescenta elementos à história.", AUD),
    ]),
    L("dig-l4", "Comunicação visual: design, identidade visual e produção gráfica", 9, [
        "Elementos do design: ponto, linha, forma, cor, tipografia e espaço. Princípios: contraste, alinhamento, proximidade, repetição e hierarquia visual, que guia o olhar do mais importante ao menos importante.",
        "Cor: RGB (vermelho, verde e azul) é o sistema aditivo das telas. CMYK (ciano, magenta, amarelo e preto) é o sistema subtrativo usado na impressão.",
        "Imagem vetorial é feita por fórmulas matemáticas e pode ser ampliada sem perda (logotipos). Imagem raster, ou bitmap, é feita de pixels e perde qualidade ao ampliar (fotografias).",
        "Resolução: cerca de 72 ppi para telas e 300 dpi para impressão. Sangria é a margem extra, além do corte final, que evita bordas brancas. Gráficas costumam receber arquivos em PDF com fontes incorporadas ou convertidas em curvas.",
        "Legibilidade e contraste entre texto e fundo são requisitos de acessibilidade. Identidade visual: logotipo, símbolo, cores, tipografia e padrões, reunidos em um manual."
    ], [
        ("RGB x CMYK", "RGB: sistema aditivo das telas. CMYK: sistema subtrativo da impressão."),
        ("Vetor x raster", "Vetor: fórmulas matemáticas, sem perda ao ampliar. Raster: pixels, perde qualidade ao ampliar."),
        ("Sangria", "Margem extra, além da linha de corte, para evitar bordas brancas na impressão.")
    ], [
        Q("O sistema de cores usado na impressão gráfica é o",
          "CMYK.",
          ["RGB.", "HSL.", "Pantone digital apenas.", "escala de cinza apenas."],
          "A impressão trabalha com ciano, magenta, amarelo e preto (CMYK). As telas usam RGB.", DES),
        Q("Um logotipo que precisa ser ampliado em uma fachada sem perder nitidez deve ser mantido em formato",
          "vetorial.",
          ["raster, com baixa resolução.", "de captura de tela.", "de miniatura.", "de bitmap de 72 ppi."],
          "Imagens vetoriais são escaláveis sem perda de qualidade.", DES),
        Q("Para um material impresso, a resolução de imagem geralmente recomendada é de",
          "300 dpi.",
          ["72 dpi.", "10 dpi.", "30 dpi.", "1 dpi."],
          "Impressão exige maior resolução que a tela, que usa em torno de 72 ppi.", DES),
        Q("A margem extra de uma arte gráfica, além da linha de corte, usada para evitar bordas brancas após o refile, chama-se",
          "sangria.",
          ["gramatura.", "hierarquia.", "mailing.", "contraforma."],
          "A sangria compensa pequenas variações no corte do papel.", DES),
    ]),
], semente=2)
