from lib import Q, L, escrever

# ---- contas usadas nas questões (verificadas) ------------------------------------------------
assert 600 / 12000 == 0.05 and 150 / 30000 == 0.005 and 600 / 30000 == 0.02
assert 900 / 30000 * 1000 == 30

T = "Referência conceitual: teorias da comunicação (Lazarsfeld; McCombs e Shaw; Noelle-Neumann; Adorno e Horkheimer; Shannon e Weaver; Schramm; Jakobson)"
K = "Referência conceitual: M. M. K. Kunsch, Planejamento de Relações Públicas na Comunicação Integrada (4ª ed., 2003); J. Duarte (org.), Comunicação Pública (2007)"
CF = "Constituição Federal de 1988, "
J = "Referência conceitual: N. Lage, A Reportagem; R. Chinem, Assessoria de Imprensa: como fazer; manuais de redação de veículos de imprensa"
D = "Referência conceitual: marketing de conteúdo e métricas de redes sociais; fundamentos de design e produção gráfica"
G = "Referência conceitual: J. J. Forni, Gestão de Crises e Comunicação; Duarte e Barros (orgs.), Métodos e Técnicas de Pesquisa em Comunicação; teoria dos stakeholders"
LAI = "Lei 12.527/2011, "
LGPD = "Lei 13.709/2018, "
LS = "Lei 15.263/2025, "

TOPICOS = ["esp-01", "esp-02", "esp-03", "esp-05", "esp-06", "esp-12", "esp-07", "esp-08", "esp-09", "esp-10", "esp-11",
           "esp-13", "esp-14", "esp-16", "esp-17", "esp-18", "esp-19", "esp-20", "esp-21", "esp-22", "esp-23", "esp-24", "esp-25", "esp-26"]

escrever("u-esp-treino-fgv", "Treino no estilo da banca: Comunicação e Marketing", "Específicos", "esp", TOPICOS, [
    L("tfg-l1", "Treino FGV: teorias, modelos e funções da linguagem", 10, [
        "Como a banca cobra: um texto-base (caso ou trecho) e uma pergunta sobre o conceito exato. Treine reconhecer a teoria pela descrição do fenômeno, sem o nome dela.",
        "Distinções que mais caem: fluxo em duas etapas (líderes de opinião) x agulha hipodérmica (efeito direto) x agenda-setting (sobre o que pensar) x espiral do silêncio (medo do isolamento).",
        "Modelo de Shannon e Weaver é linear e não prevê feedback. Modelos circulares (Osgood e Schramm) incluem retorno e campo de experiência comum.",
        "Indústria cultural (Adorno e Horkheimer) descreve a cultura transformada em mercadoria padronizada. O conceito não se resume às empresas nem às técnicas de comunicação.",
        "Jakobson: emotiva (emissor), conativa (receptor), referencial (contexto), poética (mensagem), fática (canal) e metalinguística (código)."
    ], [
        ("Como reconhecer o fluxo em duas etapas num caso", "As pessoas dizem que souberam do assunto por alguém próximo que acompanha a mídia e que também interpreta os fatos."),
        ("O que o modelo de Shannon e Weaver não pressupõe", "Feedback. É um modelo linear, centrado na transmissão do sinal, com ruído."),
        ("Agenda-setting x espiral do silêncio", "Agenda-setting: a pauta da mídia influencia a pauta do público. Espiral do silêncio: o receio do isolamento leva a calar opiniões vistas como minoritárias.")
    ], [
        Q("Leia o texto. \"Uma pesquisa de recepção sobre uma campanha de saúde constatou que a maior parte das pessoas não se informou diretamente pelos telejornais. Elas relataram ter conhecido a campanha por conversas com vizinhos e colegas que acompanham o noticiário com regularidade e que, ao comentar os fatos, davam também a sua interpretação.\" O resultado se aproxima da hipótese do fluxo em duas etapas, porque ela sustenta que",
          "a influência dos meios é, em boa parte, mediada por líderes de opinião, que filtram, repassam e interpretam as informações para os seus grupos.",
          ["os meios atingem indivíduos isolados e passivos, que reagem de modo direto e uniforme ao estímulo, o que dispensa qualquer mediação social.", "os meios definem a lista de temas que o público considera relevantes, sem exercer influência sobre as opiniões formadas pelas pessoas.", "as pessoas silenciam as opiniões que julgam minoritárias, por receio de isolamento, e isso reforça a impressão de consenso.", "a cultura é produzida em série, como mercadoria padronizada, o que reduz a capacidade crítica do público."],
          "O texto descreve a mediação por pessoas próximas que acompanham a mídia e interpretam os fatos, que é o núcleo do fluxo em duas etapas. As demais alternativas descrevem a hipótese hipodérmica, o agendamento, a espiral do silêncio e a indústria cultural.", T, "esp-01"),
        Q("Leia o texto. \"Um órgão público tratava toda falha de entendimento como problema técnico do canal: se o público não compreendia o comunicado, atribuía-se a falha à transmissão. Depois, a equipe passou a pedir retorno do público, a ajustar a linguagem e a reenviar a mensagem.\" A primeira postura se aproxima do modelo matemático de Shannon e Weaver, e a segunda incorpora um elemento que esse modelo, em sua forma original, não pressupõe, que é",
          "o feedback, que torna o processo circular e permite ajustar a mensagem.",
          ["o ruído, que passa a ser considerado fonte de distorção entre o transmissor e o receptor.", "o canal, que passa a ser escolhido de acordo com a mensagem.", "o transmissor, que codifica a mensagem em sinais.", "a fonte de informação, que seleciona a mensagem a ser enviada."],
          "O modelo original é linear: fonte, transmissor, canal, receptor e destino, com ruído. O retorno do receptor, que permite ajustes e torna o processo circular, é típico dos modelos de Osgood e Schramm.", T, "esp-02"),
        Q("Leia o texto. \"Durante uma semana, quase todos os telejornais destacaram um escândalo envolvendo uma estatal. Em enquete posterior, a maioria apontou esse tema como o problema mais importante do país, embora muitos entrevistados dissessem evitar o assunto em ambientes de trabalho, por receio de discordar da maioria que imaginavam existir.\" O texto combina duas hipóteses da área, que são, respectivamente,",
          "o agendamento (agenda-setting), pela coincidência entre a pauta da mídia e a do público, e a espiral do silêncio, pelo silêncio diante de uma opinião percebida como majoritária.",
          ["a agulha hipodérmica, pelo efeito direto e uniforme, e o fluxo em duas etapas, pela mediação de líderes de opinião.", "a indústria cultural, pela padronização do conteúdo, e o agendamento, pela mediação de líderes de opinião.", "o fluxo em duas etapas, pela mediação de líderes de opinião, e a espiral do silêncio, pela padronização do conteúdo.", "o agendamento, pela cultura em série, e a agulha hipodérmica, pelo silêncio diante da maioria."],
          "A coincidência entre os temas da mídia e os temas do público caracteriza o agendamento. O receio de expor opinião que se supõe minoritária caracteriza a espiral do silêncio.", T, "esp-01"),
        Q("Sobre o conceito de indústria cultural, formulado por Adorno e Horkheimer, é correto afirmar que ele",
          "descreve a conversão da cultura em mercadoria padronizada e produzida em série para o consumo, com efeito de reduzir a capacidade crítica, e não se limita às empresas ou às técnicas de comunicação.",
          ["designa apenas as empresas de rádio e televisão que produzem conteúdo, sem relação com a lógica de mercado.", "sustenta que o público seleciona e filtra livremente os conteúdos, o que neutraliza o poder da mídia.", "afirma que os líderes de opinião intermediam o acesso do público aos meios de comunicação.", "explica a influência da mídia pelos temas que ela destaca em sua agenda."],
          "Para os autores, trata-se de uma prática social em que a produção cultural passa a ser orientada pelo mercado. A segunda alternativa descreve a recepção ativa, a terceira o fluxo em duas etapas e a quarta o agendamento.", T, "esp-01"),
        Q("Leia os trechos de um comunicado: (I) \"Estamos orgulhosos do resultado do programa.\" (II) \"Inscreva-se até sexta-feira.\" (III) \"As inscrições vão de 20/10 a 10/11.\" (IV) \"Inscrição, neste edital, é o ato de preencher o requerimento e enviá-lo.\" As funções da linguagem predominantes em I, II, III e IV são, respectivamente,",
          "emotiva, conativa, referencial e metalinguística.",
          ["conativa, emotiva, referencial e poética.", "emotiva, referencial, conativa e fática.", "referencial, conativa, emotiva e metalinguística.", "poética, conativa, referencial e fática."],
          "I expressa o sentimento do emissor (emotiva). II busca agir sobre o receptor (conativa). III informa sobre o contexto (referencial). IV explica o próprio código (metalinguística).", T, "esp-02"),
    ]),
    L("tfg-l2", "Treino FGV: comunicação organizacional, pública, identidade e comunicação interna", 10, [
        "Como a banca cobra: um caso de organização com um problema de comunicação e a pergunta pelo diagnóstico ou pela classificação correta.",
        "Comunicação integrada exige política global e planejamento conjunto entre as áreas. Mensagens contraditórias são o sintoma mais citado.",
        "Comunicação pública é centrada no cidadão e no interesse público. A Constituição (art. 37, § 1º) veda promoção pessoal em publicidade de órgãos públicos.",
        "Identidade é o que a organização declara ser. Imagem é a percepção dos públicos. Reputação é o julgamento acumulado ao longo do tempo.",
        "Fluxos da comunicação interna: descendente, ascendente, horizontal e diagonal. A comunicação institucional trabalha a imagem da organização, e a mercadológica trabalha produtos e vendas."
    ], [
        ("Sintoma típico de falta de comunicação integrada", "Áreas diferentes divulgando mensagens contraditórias sobre o mesmo assunto."),
        ("Identidade x imagem", "Identidade é o que a organização declara ser. Imagem é como os públicos a percebem."),
        ("Fluxo ascendente", "Informações e opiniões que partem dos empregados em direção à direção.")
    ], [
        Q("Leia o texto. \"Uma agência de fomento afirma, em campanha nacional, que valoriza a transparência e a escuta. No mesmo período, a comunicação interna publica avisos sem explicar mudanças de regras, a assessoria dá versões diferentes sobre o mesmo projeto e o marketing promove um serviço com mensagens que contradizem a campanha.\" À luz da comunicação integrada, o principal problema descrito é",
          "a ausência de política global e de planejamento conjunto entre as áreas, que produz mensagens incoerentes e enfraquece a identidade e a reputação.",
          ["o excesso de comunicação administrativa, em detrimento da mercadológica, o que desequilibra o composto da comunicação.", "o uso de canais digitais em vez de impressos, o que fragmenta o público externo.", "a falta de públicos externos definidos, já que a comunicação integrada trata apenas do público interno.", "a valorização exagerada da comunicação interna, que deveria ser extinta para evitar ruído."],
          "Mensagens contraditórias entre assessoria, comunicação interna e marketing indicam falta de integração, o que fere a coerência do discurso e a reputação.", K, "esp-05"),
        Q("Leia o texto. \"Em uma peça sobre um programa do governo, aparecem o nome, a foto e o slogan pessoal do dirigente, sem informação sobre como o cidadão pode acessar o serviço.\" Sob a ótica da comunicação pública e da Constituição Federal, a peça é inadequada porque",
          "a publicidade de órgãos públicos deve ter caráter educativo, informativo ou de orientação social, sendo vedada a promoção pessoal de autoridades, e deve se orientar ao cidadão e ao acesso ao serviço.",
          ["a publicidade de órgãos públicos é vedada em qualquer hipótese, em respeito ao princípio da economicidade.", "a Constituição só proíbe a promoção pessoal em períodos eleitorais, e a peça deveria apenas ser veiculada fora deles.", "a comunicação pública só pode ser feita por veículos impressos e pela imprensa oficial.", "a peça deveria destacar ainda mais o dirigente, para ampliar a credibilidade do programa."],
          "O art. 37, § 1º, da Constituição exige caráter educativo, informativo ou de orientação social e veda nomes, símbolos ou imagens que caracterizem promoção pessoal.", CF + "art. 37, § 1º (planalto.gov.br); " + K, "esp-03"),
        Q("Leia o texto. \"Pesquisa com empresas atendidas mostrou que a agência é vista como burocrática e lenta, embora declare, em sua visão, ser referência em soluções inovadoras e inclusivas. Em cinco anos, a percepção se manteve estável.\" A situação descreve",
          "uma distância entre a identidade declarada e a imagem percebida, que, mantida ao longo do tempo, consolida uma reputação desfavorável.",
          ["uma coincidência entre identidade e imagem, com reputação ainda em formação.", "um problema exclusivamente visual, que se resolve com a troca do logotipo.", "um efeito de ruído técnico no canal, sem relação com a reputação.", "uma falha de comunicação mercadológica, restrita à propaganda de produtos."],
          "Identidade é o que a organização declara. Imagem é a percepção dos públicos. Quando a imagem destoa da identidade por muito tempo, a reputação se firma em torno dessa percepção.", K, "esp-06"),
        Q("Leia o texto. \"Uma organização realiza reunião mensal em que os empregados enviam perguntas à direção, que as responde publicamente. Mantém também uma caixa de sugestões. Os comunicados da presidência seguem por e-mail.\" Em relação aos fluxos da comunicação interna, as ações descritas correspondem, respectivamente, aos fluxos",
          "ascendente (reunião com perguntas e caixa de sugestões) e descendente (comunicados da presidência).",
          ["horizontal (reunião e caixa de sugestões) e diagonal (comunicados da presidência).", "descendente (reunião e caixa de sugestões) e ascendente (comunicados da presidência).", "diagonal (reunião com perguntas) e horizontal (caixa de sugestões e comunicados).", "ascendente (comunicados da presidência) e horizontal (reunião e caixa de sugestões)."],
          "Perguntas e sugestões partem dos empregados para a direção (ascendente). Comunicados da presidência vão da direção para a base (descendente).", K, "esp-12"),
        Q("Leia o texto. \"A agência patrocina um seminário sobre transformação digital e exige, como contrapartida, o uso de sua logomarca nas peças de divulgação e um estande institucional. O objetivo declarado é associar a marca ao tema e ampliar sua visibilidade, e não vender um produto.\" Segundo a classificação de Kunsch, a ação se insere principalmente na comunicação",
          "institucional, pois trabalha imagem, identidade e visibilidade da organização, e não a venda direta de produtos.",
          ["mercadológica, pois toda ação com logomarca visa à venda imediata de um produto.", "administrativa, pois depende de formalização por documentos e normas internas.", "interna, pois o público principal é o corpo de empregados.", "política, pois busca apoio para candidatos e partidos."],
          "O patrocínio com associação de marca e visibilidade, sem oferta de produto, é típico da comunicação institucional.", K, "esp-03"),
    ]),
    L("tfg-l3", "Treino FGV: assessoria, imprensa e redação jornalística", 10, [
        "Como a banca cobra: caso de assessoria com um problema (release ignorado, fonte, gênero) e a pergunta pela causa ou pela conduta correta.",
        "Release com tom promocional, sem fato novo e sem dado verificável tende a ser ignorado. Linguagem de notícia e relevância jornalística aumentam o aproveitamento.",
        "Fontes: oficial, oficiosa e independente. Regras de entrevista: on, off the record (não publica nem atribui), background (publica sem identificar a fonte) e embargo.",
        "Lide objetivo traz o essencial (o quê, quem, quando, onde, como e por quê). Título informativo, com verbo, concreto e curto, é preferível a título vago ou promocional.",
        "Gêneros: artigo é opinativo e assinado. Reportagem aprofunda, notícia relata o fato, editorial expressa a posição do veículo."
    ], [
        ("Por que um release costuma ser ignorado", "Falta de fato novo e de relevância jornalística, tom promocional e ausência de dados verificáveis."),
        ("Background x off the record", "Background: a informação pode ser usada sem identificar a fonte. Off the record: não pode ser publicada nem atribuída."),
        ("Bom título jornalístico", "Informativo, concreto, com verbo e curto.")
    ], [
        Q("Leia o texto. \"A assessoria enviou release dizendo que a agência 'tem a alegria de comunicar mais um ano de excelência, com equipe comprometida e resultados incríveis'. Nenhum veículo o publicou.\" A causa mais provável é que o texto",
          "não traz fato novo nem dados de interesse público e adota tom promocional, em vez da linguagem objetiva de notícia, o que reduz o seu valor-notícia.",
          ["foi enviado sem pagamento pela publicação, o que impede a veiculação por veículos sérios.", "trouxe dados verificáveis em excesso, o que dificulta a leitura do jornalista.", "foi enviado a poucos veículos, todos eles segmentados na editoria correta.", "usou título informativo e lide com as informações essenciais."],
          "Release precisa de relevância jornalística, fato novo e linguagem de notícia. Adjetivos promocionais e ausência de dados levam à rejeição. A publicação em mídia espontânea não é paga.", J, "esp-07"),
        Q("Leia o texto. \"Um assessor repassa a um repórter, sem autorização da diretoria, informações sobre uma decisão ainda não anunciada. O repórter publica a informação sem citar a origem, atribuindo-a a 'fontes próximas à diretoria'.\" A situação envolve uma fonte e uma regra de entrevista que são, respectivamente,",
          "oficiosa e background.",
          ["oficial e off the record.", "independente e embargo.", "oficial e embargo.", "oficiosa e off the record."],
          "O assessor próximo à fonte oficial, sem autorização para falar em seu nome, é fonte oficiosa. Publicar sem identificar a origem é o regime de background. No off the record, a informação não é publicada nem atribuída.", J, "esp-08"),
        Q("Considere o fato: uma agência de fomento lançou ontem, em Brasília, um portal gratuito com 120 conjuntos de dados abertos, para facilitar o controle social e a reutilização de informações. O lide mais adequado, em texto jornalístico, é",
          "\"Uma agência de fomento lançou ontem, em Brasília, um portal gratuito com 120 conjuntos de dados abertos, para facilitar o controle social e a reutilização de informações.\"",
          ["\"Em um dia histórico para a transparência, a agência de fomento realizou um evento memorável, que marcará uma nova era.\"", "\"Desde sua criação, a agência de fomento trabalha para promover o desenvolvimento do país, e hoje houve novidades.\"", "\"É louvável a iniciativa da agência de fomento, que finalmente lançou um portal de dados.\"", "\"Foi lançado um portal gratuito, o que deve beneficiar muita gente.\""],
          "O lide traz o essencial (o quê, quem, quando, onde, como e por quê) em linguagem objetiva. As demais opções são promocionais, vagas ou opinativas.", J, "esp-10"),
        Q("Leia o texto. \"Um especialista, em texto assinado, defende que os órgãos públicos devem adotar linguagem simples, apresentando argumentos e exemplos para sustentar o ponto de vista.\" Segundo a classificação de Marques de Melo, o texto pertence ao gênero e à categoria, respectivamente,",
          "artigo, da categoria opinativa.",
          ["reportagem, da categoria informativa.", "nota, da categoria utilitária.", "perfil, da categoria interpretativa.", "editorial, da categoria informativa."],
          "Texto assinado que defende tese com argumentos é um artigo, gênero opinativo. O editorial é opinativo, mas expressa a posição do veículo e não é assinado por um colaborador.", J, "esp-09"),
        Q("Para a notícia sobre o lançamento do portal de dados abertos, o título mais adequado é",
          "\"Portal reúne 120 conjuntos de dados abertos para fortalecer o controle social\".",
          ["\"Um grande avanço para a transparência!\"", "\"Portal\"", "\"Agência faz anúncio importante em evento especial\"", "\"Será que agora vai dar certo?\""],
          "O bom título é informativo, concreto, com verbo e curto. Os demais são vagos, exclamativos ou opinativos.", J, "esp-11"),
    ]),
    L("tfg-l4", "Treino FGV: digital, redes sociais, acessibilidade e produção gráfica", 10, [
        "Como a banca cobra: relatório com números e pergunta pela métrica correta, ou caso com problema de canal e pergunta pela melhor ação.",
        "Taxa de engajamento = interações divididas pelo alcance (ou por outra base indicada). CTR = cliques divididos por impressões. CPM = custo dividido por impressões, vezes mil.",
        "SEO depende de título e descrição claros, palavras-chave relevantes, conteúdo útil e boa experiência no celular.",
        "Acessibilidade: texto alternativo em imagens, legendas em vídeos, contraste adequado e informação principal em texto.",
        "Produção gráfica: impressão usa CMYK, 300 dpi e sangria. Imagens de 72 ppi, em RGB e sem sangria geram problemas na gráfica."
    ], [
        ("Taxa de engajamento sobre o alcance", "Interações divididas pelo alcance."),
        ("CPM", "Custo por mil impressões: custo dividido pelas impressões e multiplicado por mil."),
        ("Problemas de enviar à gráfica imagem de 72 ppi em RGB sem sangria", "Pixelização, mudança de cores na conversão para CMYK e bordas brancas após o corte.")
    ], [
        Q("Leia o texto. \"O relatório mensal de um perfil institucional registrou alcance de 12.000 pessoas, 30.000 impressões, 600 interações e 150 cliques.\" A taxa de engajamento sobre o alcance e a taxa de cliques (CTR) foram, respectivamente,",
          "5% e 0,5%.",
          ["2% e 0,5%.", "5% e 2,5%.", "20% e 5%.", "0,5% e 5%."],
          "Engajamento sobre o alcance: 600 dividido por 12.000 é 5%. CTR: 150 dividido por 30.000 é 0,5%. O valor de 2% seria o engajamento calculado sobre as impressões.", D, "esp-14"),
        Q("Uma campanha paga custou R$ 900,00 e gerou 30.000 impressões. O custo por mil impressões (CPM) foi de",
          "R$ 30,00.",
          ["R$ 3,00.", "R$ 300,00.", "R$ 0,03.", "R$ 27,00."],
          "CPM é o custo dividido pelas impressões e multiplicado por mil: 900 dividido por 30.000, vezes 1.000, é R$ 30,00.", D, "esp-14"),
        Q("Leia o texto. \"Uma página institucional tem conteúdo de qualidade, mas título genérico, sem palavras-chave, e carrega lentamente no celular. O número de acessos orgânicos é baixo.\" A ação mais adequada é",
          "otimizar título e descrição, usar palavras-chave relevantes e melhorar o desempenho e a responsividade em dispositivos móveis.",
          ["aumentar exclusivamente o investimento em mídia paga, sem alterar a página.", "trocar o conteúdo por textos mais longos e sem estrutura.", "remover o título para evitar duplicidade com a descrição.", "desativar a versão para celular, pois o acesso orgânico vem de computadores."],
          "SEO e experiência do usuário dependem de título, descrição, palavras-chave e desempenho em dispositivos móveis.", D, "esp-13"),
        Q("Leia o texto. \"Uma publicação em rede social traz apenas uma imagem com todo o texto embutido, um vídeo sem legendas e cores de baixo contraste.\" Do ponto de vista da acessibilidade, a melhor correção é",
          "manter a informação principal também em texto, incluir texto alternativo na imagem, legendar o vídeo e melhorar o contraste entre texto e fundo.",
          ["manter tudo como está, pois a acessibilidade só é exigida em sítios oficiais impressos.", "remover o vídeo e a imagem, deixando apenas o título.", "aumentar o tamanho da imagem, sem alterar o conteúdo.", "incluir mais texto embutido na imagem, para facilitar a leitura."],
          "Texto alternativo, legendas e bom contraste permitem o acesso de pessoas com deficiência visual ou auditiva. A Lei Brasileira de Inclusão define acessibilidade como condição de alcance, com autonomia, da informação e da comunicação.", "Lei 13.146/2015, art. 3º, I e V (planalto.gov.br); " + D, "esp-13"),
        Q("Leia o texto. \"A equipe enviará à gráfica um cartaz A3 com fotos retiradas de um site (72 ppi), em RGB e sem sangria.\" Os problemas mais prováveis são",
          "imagens pixeladas, alteração de cores na conversão para CMYK e bordas brancas após o corte.",
          ["nenhum, pois a gráfica converte automaticamente qualquer arquivo sem perda de qualidade.", "apenas o aumento do custo do papel, sem efeito visual.", "excesso de resolução, que torna a impressão mais lenta, mas sem outros efeitos.", "perda de cor apenas nos textos, mantendo as imagens inalteradas."],
          "Imagens de 72 ppi pixelam ao serem ampliadas. A impressão usa CMYK, e a conversão de RGB pode alterar as cores. A sangria evita bordas brancas depois do corte.", D, "esp-17"),
    ]),
    L("tfg-l5", "Treino FGV: eventos, pesquisa, crises e públicos", 10, [
        "Como a banca cobra: caso com dados de pesquisa, linha do tempo de crise ou perfil de público, e a pergunta pela conduta ou classificação correta.",
        "Pesquisa quantitativa: amostra representativa, margem de erro e generalização estatística. Qualitativa: aprofundamento de percepções, sem generalizar.",
        "Na crise, a resposta inicial mais indicada é acionar o comitê, apurar os fatos, definir mensagens e porta-voz, e comunicar com rapidez e transparência, sem negar ou especular.",
        "Matriz de poder e interesse: alto poder e baixo interesse, manter satisfeito. Alto poder e alto interesse, gerenciar de perto. Baixo poder e alto interesse, manter informado.",
        "Indicadores de produto (inscritos, posts) medem produção. Indicadores de efeito (mudança de comportamento) estão mais próximos do objetivo."
    ], [
        ("Pesquisa quantitativa x qualitativa", "Quantitativa: generaliza dentro da margem de erro. Qualitativa: aprofunda percepções, sem generalização."),
        ("Resposta inicial a uma crise", "Acionar o comitê, apurar fatos, definir mensagens e porta-voz único, e comunicar de forma rápida e transparente."),
        ("Alto poder e baixo interesse", "Manter satisfeito.")
    ], [
        Q("Leia o texto. \"Uma área de comunicação contratou pesquisa com 1.200 empregados escolhidos aleatoriamente, com questionário estruturado e margem de erro de 3 pontos percentuais. Em seguida, organizou grupos focais com 10 empregados.\" É correto afirmar que",
          "a primeira pesquisa é quantitativa e permite generalização estatística dentro da margem de erro, enquanto os grupos focais são qualitativos e aprofundam percepções, sem generalizar.",
          ["os grupos focais permitem generalizar os resultados para todos os empregados, pois são mais profundos que a pesquisa por questionário.", "a pesquisa por questionário é qualitativa, pois ouve muitas pessoas, e os grupos focais são quantitativos, pois reúnem poucas pessoas.", "a margem de erro de 3 pontos indica que 3% dos empregados não responderam ao questionário.", "nenhuma das duas técnicas pode ser usada para conhecer a percepção dos empregados."],
          "A amostra aleatória e o questionário estruturado caracterizam a pesquisa quantitativa. Grupos focais são técnica qualitativa, que busca compreender motivos e percepções, sem generalizar.", G, "esp-19"),
        Q("Leia o texto. \"Em uma sexta-feira à noite, a organização descobre um vazamento de dados cadastrais de participantes de um evento, e capturas de tela começam a circular nas redes.\" A resposta inicial mais adequada, em gestão de crises, é",
          "acionar o comitê de crise, apurar os fatos, definir as mensagens e o porta-voz e comunicar de modo rápido e transparente aos afetados e ao público interno, sem especular.",
          ["aguardar a segunda-feira para evitar decisões precipitadas, mantendo silêncio nas redes.", "negar o vazamento até que haja prova definitiva, para proteger a reputação.", "autorizar que cada diretor dê a sua versão à imprensa, para ampliar a transparência.", "publicar apenas uma nota genérica, sem informar o que ocorreu, para evitar pânico."],
          "A crise exige resposta rápida, verdadeira e coordenada, por porta-voz definido, sem negar fatos nem especular. A demora e as versões diferentes agravam o dano.", G, "esp-20"),
        Q("Leia o texto. \"Uma associação setorial tem grande poder de influência sobre a política industrial, mas pouco interesse nas ações do dia a dia da agência.\" Na matriz de poder e interesse, esse público deve ser",
          "mantido satisfeito, com informações estratégicas em momentos relevantes.",
          ["gerenciado de perto, com contato diário e participação em todas as decisões.", "apenas mantido informado, por ter baixo poder.", "monitorado, sem qualquer ação de relacionamento.", "ignorado, por ter baixo interesse."],
          "Alto poder e baixo interesse pedem manter satisfeito. Gerenciar de perto é para alto poder e alto interesse.", G, "esp-21"),
        Q("Leia o texto. \"Após um seminário, o relatório informou 800 inscritos, 520 presentes e, três meses depois, que 40% dos participantes passaram a adotar a prática apresentada.\" O indicador mais próximo do efeito sobre o objetivo do evento é",
          "o percentual de participantes que passaram a adotar a prática apresentada.",
          ["o número de inscritos.", "o número de presentes.", "a quantidade de posts publicados sobre o evento.", "o custo por participante."],
          "Inscritos e presentes medem participação (produto). A adoção da prática mede mudança de comportamento, que é o efeito desejado.", G, "esp-18"),
        Q("Leia o texto. \"Diante do risco de rompimento de um reservatório, um órgão publica nota técnica cheia de jargões, sem indicar o que a população deve fazer e sem mencionar incertezas.\" Em comunicação de risco, a nota é inadequada porque",
          "não usa linguagem clara, não orienta ações de proteção e não é transparente sobre as incertezas.",
          ["cumpre todos os requisitos, pois linguagem técnica é sempre preferível em situações de risco.", "revela incertezas em excesso, o que deveria ser evitado para impedir o pânico.", "deveria ter sido publicada apenas depois do fim do risco.", "deveria ser substituída por mensagens publicitárias do órgão."],
          "A comunicação de risco informa com clareza sobre perigos e sobre como se proteger, com base técnica e transparência sobre incertezas.", G, "esp-20"),
    ]),
    L("tfg-l6", "Treino FGV: legislação, acessibilidade e comunicação científica", 10, [
        "Como a banca cobra: caso prático e a pergunta pela norma ou conduta aplicável. Cite o dispositivo mentalmente: art. 5º da CF, art. 37, § 1º, LAI, LGPD, LBI, Lei 15.263.",
        "LAI: publicidade como regra, sigilo como exceção. Pedido sem justificativa de motivo, resposta imediata ou em até 20 dias, prorrogável por mais 10. Aplica-se, no que couber, a entidades privadas sem fins lucrativos que recebem recursos públicos.",
        "Direito de resposta (CF, art. 5º, V): proporcional ao agravo, além de indenização por dano material, moral ou à imagem.",
        "LGPD: finalidade, necessidade, transparência, consentimento e direitos do titular (acesso, correção, eliminação de dados tratados com consentimento).",
        "Linguagem simples (Lei 15.263/2025): frases curtas e diretas, voz ativa, informação mais importante primeiro, siglas explicadas. Greenwashing é discurso ambiental sem lastro nas práticas."
    ], [
        ("Prazo de resposta a pedido de acesso à informação", "Imediato, se disponível. Senão, até 20 dias, prorrogável por mais 10, com justificativa."),
        ("Direito de resposta (CF, art. 5º, V)", "Proporcional ao agravo, além de indenização por dano material, moral ou à imagem."),
        ("Greenwashing", "Imagem ambientalmente responsável sem práticas que a sustentem.")
    ], [
        Q("Leia o texto. \"Um cidadão pede, por e-mail, informações sobre os repasses de recursos públicos recebidos, por contrato de gestão, por uma entidade privada sem fins lucrativos, e não quer informar o motivo do pedido.\" De acordo com a Lei de Acesso à Informação, é correto afirmar que",
          "a lei se aplica, no que couber, à entidade, quanto à parcela dos recursos públicos recebida e à sua destinação; o motivo não pode ser exigido; e a resposta é imediata, se disponível, ou em até 20 dias, prorrogáveis por mais 10.",
          ["a lei não se aplica a entidades privadas, ainda que recebam recursos públicos.", "o cidadão deve justificar por escrito o interesse, sob pena de indeferimento.", "o prazo de resposta é de 5 dias, improrrogáveis, em qualquer hipótese.", "o pedido só é válido se for feito presencialmente, com cópia de documento de identidade."],
          "O art. 2º estende a LAI a entidades privadas sem fins lucrativos que recebem recursos públicos por contrato de gestão, quanto à parcela recebida e sua destinação. O art. 10, § 3º, veda exigir os motivos, e o art. 11 fixa 20 dias, prorrogáveis por 10.", LAI + "arts. 2º, 10, § 3º, e 11 (planalto.gov.br)", "esp-24"),
        Q("Leia o texto. \"Um jornal atribui falsamente a um servidor o desvio de recursos. O servidor pede retratação.\" De acordo com a Constituição Federal, ele",
          "tem assegurado o direito de resposta, proporcional ao agravo, além de indenização por dano material, moral ou à imagem, sem que isso signifique censura prévia à imprensa.",
          ["só pode exercer o direito de resposta depois de condenação criminal do jornal.", "não tem qualquer direito, pois a liberdade de imprensa impede qualquer reparação.", "tem direito apenas a um pedido informal de desculpas, sem indenização.", "depende da autorização de um ministro de Estado para exercer o direito de resposta."],
          "O art. 5º, V, assegura o direito de resposta proporcional ao agravo e a indenização. O art. 220 protege a liberdade de informação, mas não afasta a responsabilização posterior.", CF + "arts. 5º, V, e 220 (planalto.gov.br)", "esp-23"),
        Q("Leia o texto. \"Um setor de comunicação cria uma lista com os contatos de pessoas que participaram de um evento e passa a enviar newsletters promocionais, sem informar a finalidade do uso dos dados nem oferecer meio de descadastro.\" À luz da LGPD, a conduta",
          "afronta os princípios da finalidade e da transparência e dificulta o exercício dos direitos do titular, sendo recomendável coletar o necessário, informar a finalidade, obter consentimento claro e oferecer descadastro.",
          ["é regular, pois dados de contato de participantes de evento são públicos e dispensam qualquer cuidado.", "é regular, desde que a newsletter seja enviada apenas em dias úteis.", "só seria irregular se os dados fossem sensíveis, o que torna os demais dados livres.", "é regular, porque a LGPD não se aplica a atividades de comunicação."],
          "O tratamento de dados pessoais exige finalidade informada, necessidade, transparência e base legal. O titular pode, por exemplo, pedir a eliminação dos dados tratados com consentimento (art. 18).", LGPD + "arts. 6º, 7º e 18 (planalto.gov.br)", "esp-25"),
        Q("Considere o texto original de um aviso: \"Em face da necessidade de adimplemento tempestivo das obrigações, informa-se aos interessados que a documentação deverá ser protocolizada.\" A reescrita que melhor atende às técnicas da Política Nacional de Linguagem Simples é",
          "\"Envie os documentos pelo portal até 10/11. Quem perder o prazo não poderá se inscrever.\"",
          ["\"Fica a documentação sujeita a protocolização tempestiva, sob pena de inadmissão do requerimento.\"", "\"Ressalta-se a necessidade de que sejam observados os prazos, sendo imprescindível que os documentos sejam protocolizados.\"", "\"Informa-se que, tendo em vista os prazos, os documentos devem ser, em tempo hábil, enviados pelos interessados.\"", "\"A documentação, caso seja enviada, deverá, até a data, que será oportunamente informada, ser protocolizada.\""],
          "A Lei 15.263/2025 recomenda frases curtas e em ordem direta, voz ativa, palavras comuns e as informações mais importantes primeiro. A reescrita correta é direta e traz o prazo logo no início.", LS + "art. 5º (planalto.gov.br)", "esp-26"),
        Q("Leia o texto. \"Uma campanha afirma que a operação de uma organização é '100% sustentável', mas não apresenta dados, metas nem certificações.\" Em comunicação ambiental, o caso configura",
          "risco de greenwashing, sendo recomendável apresentar dados, metas e resultados verificáveis.",
          ["divulgação científica rigorosa, que dispensa a apresentação de fontes.", "comunicação de risco, pois alerta o público sobre perigos ambientais.", "disseminação científica entre especialistas, em periódicos.", "comunicação administrativa, por tratar de fluxos internos da organização."],
          "Alegações ambientais sem dados e sem lastro nas práticas são o traço do greenwashing. Dados verificáveis protegem a credibilidade e a reputação.", "Referência conceitual: W. C. Bueno, Comunicação científica e divulgação científica; práticas de comunicação ambiental", "esp-22"),
    ]),
], semente=0)
