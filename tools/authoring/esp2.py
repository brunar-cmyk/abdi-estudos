from lib import Q, L, escrever

EVT = "Referência conceitual: L. C. H. Zanella, Manual de Organização de Eventos; prática de cerimonial e protocolo"
PES = "Referência conceitual: J. Duarte e A. Barros (orgs.), Métodos e Técnicas de Pesquisa em Comunicação"
CRI = "Referência conceitual: J. J. Forni, Gestão de Crises e Comunicação"
PUB = "Referência conceitual: teoria dos stakeholders (R. E. Freeman) e matriz poder e interesse (A. Mendelow)"
CF = "Constituição Federal de 1988 (planalto.gov.br), "
LAI = "Lei 12.527/2011 (planalto.gov.br), "
LGPD = "Lei 13.709/2018 (planalto.gov.br), "
LBI = "Lei 13.146/2015 (planalto.gov.br), "
LS = "Lei 15.263/2025 (planalto.gov.br), "

escrever("u-esp-eventos-pesquisa-crise", "Eventos, pesquisa de opinião, gestão de crises e relacionamento com públicos", "Específicos", "esp",
         ["esp-18", "esp-19", "esp-20", "esp-21"], [
    L("evt-l1", "Planejamento e organização de eventos", 9, [
        "Evento é uma ação planejada para reunir pessoas em torno de um objetivo. Tipos: institucionais, corporativos, científicos, culturais, sociais e promocionais.",
        "Etapas: planejamento (objetivo, público, tema, data, local, orçamento, cronograma, equipe), execução (credenciamento, recepção, cerimonial, comunicação, operação) e pós-evento (avaliação, relatório, agradecimentos e clipping).",
        "Ferramentas: briefing, checklist, cronograma, planilha de custos, contratos com fornecedores e plano de contingência para imprevistos.",
        "Cerimonial e protocolo organizam a ordem de precedência das autoridades, a composição da mesa e a condução da cerimônia, em geral pelo mestre de cerimônias.",
        "Acessibilidade do espaço (rampas, Libras, legendas), sustentabilidade e comunicação do evento (convite, site, redes, imprensa) fazem parte do planejamento. A participação da ABDI em feiras e eventos da atividade-fim é hipótese de inexigibilidade de licitação, e o apoio a eventos de terceiros pode ocorrer por convênio de patrocínio."
    ], [
        ("Etapas de um evento", "Planejamento, execução e pós-evento (avaliação e relatório)."),
        ("Plano de contingência", "Plano para lidar com imprevistos, como mudança de clima, falha de equipamento ou ausência de palestrante."),
        ("Cerimonial", "Conjunto de normas de precedência e condução da cerimônia, incluindo a composição da mesa.")
    ], [
        Q("Entre as etapas básicas de organização de um evento, a avaliação de resultados, com relatório e pesquisa de satisfação, ocorre no",
          "pós-evento.",
          ["pré-evento, antes de definir o objetivo.", "início do credenciamento.", "momento da escolha do local.", "briefing."],
          "A avaliação fecha o ciclo e gera aprendizados para os próximos eventos.", EVT),
        Q("O plano elaborado para lidar com imprevistos, como falha de equipamento ou ausência de palestrante, é o",
          "plano de contingência.",
          ["clipping.", "mailing.", "media training.", "manual de identidade visual."],
          "O plano de contingência prevê alternativas para situações imprevistas.", EVT),
        Q("Ao definir a ordem de precedência das autoridades e a composição da mesa em uma solenidade, o profissional atua no",
          "cerimonial e protocolo.",
          ["marketing de performance.", "design gráfico.", "clipping.", "social listening."],
          "Cerimonial e protocolo regem a ordem de precedência e a condução da cerimônia.", EVT),
        Q("Segundo o Regulamento de Licitações e Contratos da ABDI, a participação da ABDI em feiras, exposições, congressos, seminários e eventos relacionados com sua atividade-fim é hipótese de",
          "inexigibilidade de licitação.",
          ["concorrência obrigatória.", "pregão obrigatório.", "leilão.", "contratação vedada."],
          "O art. 11, VIII, do Regulamento de Licitações e Contratos prevê essa hipótese.", "Regulamento de Licitações e Contratos da ABDI (Resolução CD 005/2021), art. 11, VIII (abdi.com.br)"),
    ]),
    L("evt-l2", "Pesquisa de opinião e avaliação de resultados de comunicação", 9, [
        "Pesquisa quantitativa trabalha com amostras representativas e questionários estruturados, e produz resultados estatísticos generalizáveis, com margem de erro e nível de confiança. Pesquisa qualitativa, como entrevistas em profundidade e grupos focais, busca compreender percepções e motivos, sem generalizar.",
        "Quanto maior e mais bem selecionada a amostra, menor a margem de erro. Viés de amostragem e perguntas induzidas comprometem os resultados.",
        "Tipos: pesquisa de opinião, de imagem e reputação, de satisfação, de clima organizacional e de audiência.",
        "Avaliação de resultados: produtos (outputs), como o número de releases e posts; efeitos (outtakes e outcomes), como mudança de percepção ou comportamento; e impacto no objetivo institucional. Na análise de mídia, a valência classifica as menções como positivas, neutras ou negativas.",
        "Indicadores devem estar ligados aos objetivos do plano. Métricas de vaidade (curtidas, seguidores) isoladas não bastam."
    ], [
        ("Quantitativa x qualitativa", "Quantitativa: amostra representativa e resultados estatísticos. Qualitativa: percepções e motivos em profundidade, sem generalizar."),
        ("Margem de erro", "Quanto maior e melhor selecionada a amostra, menor a margem de erro."),
        ("Valência", "Classificação das menções na mídia como positivas, neutras ou negativas.")
    ], [
        Q("A técnica de pesquisa que reúne um pequeno grupo de pessoas para discutir um tema com um moderador, buscando compreender percepções e motivações, é o",
          "grupo focal, de natureza qualitativa.",
          ["survey com amostra probabilística, de natureza quantitativa.", "censo demográfico.", "pesquisa documental estatística.", "monitoramento de métricas de vaidade."],
          "O grupo focal é técnica qualitativa. Ele não busca generalização estatística.", PES),
        Q("Em uma pesquisa quantitativa, quando se aumenta o tamanho de uma amostra bem selecionada, em geral a margem de erro",
          "diminui.",
          ["aumenta.", "permanece sempre igual.", "se torna infinita.", "deixa de existir por completo."],
          "Amostras maiores e bem selecionadas reduzem a margem de erro, embora não a eliminem.", PES),
        Q("Na análise de mídia, a classificação das matérias como positivas, neutras ou negativas em relação à organização é chamada de",
          "valência.",
          ["alcance.", "frequência.", "mailing.", "sangria."],
          "A valência indica o tom das menções.", PES),
        Q("O número de releases enviados e de posts publicados em um mês é um indicador de",
          "produto (output), e não do efeito da comunicação sobre o público.",
          ["impacto institucional.", "mudança de comportamento do público.", "reputação medida em pesquisa.", "resultado financeiro direto."],
          "Outputs medem a produção. Efeitos e impacto exigem pesquisa de percepção ou de comportamento.", PES),
    ]),
    L("cri-l1", "Gestão de crises e comunicação de risco", 10, [
        "Crise é um evento que ameaça a reputação, a operação ou a legitimidade da organização e exige resposta rápida. Fases: pré-crise (prevenção), crise (resposta) e pós-crise (aprendizado e recuperação).",
        "Pré-crise: mapear riscos, ter plano e manual de gestão de crises, comitê de crise, lista de contatos, porta-vozes treinados e monitoramento de menções. O Estatuto da ABDI inclui os riscos de imagem e reputação na Política de Gestão de Riscos (art. 14, § 4º).",
        "Durante a crise: reunir o comitê, apurar os fatos, definir mensagens, falar rápido, com verdade e transparência, por meio de porta-voz único ou poucos, informar primeiro o público interno e acompanhar as redes. Evitar negar fatos, especular e o \"sem comentários\".",
        "Pós-crise: avaliar a atuação, corrigir causas, comunicar mudanças e reconstruir a reputação.",
        "Comunicação de risco informa o público sobre perigos e como se proteger, com linguagem clara, base técnica, orientações práticas e transparência sobre incertezas."
    ], [
        ("Fases da gestão de crises", "Pré-crise (prevenção), crise (resposta) e pós-crise (aprendizado e recuperação)."),
        ("Porta-voz na crise", "Preferencialmente um só, ou poucos e treinados, para garantir consistência."),
        ("Comunicação de risco", "Informar o público sobre perigos e formas de proteção, com clareza, base técnica e transparência sobre incertezas.")
    ], [
        Q("Entre as fases da gestão de crises, aquela em que se mapeiam riscos, elaboram-se planos e treinam-se porta-vozes é a",
          "pré-crise.",
          ["crise.", "pós-crise.", "briefing.", "mídia paga."],
          "A prevenção ocorre antes do evento crítico.", CRI),
        Q("Durante uma crise, a organização deve, em geral, comunicar de forma",
          "rápida, transparente e verdadeira, por meio de porta-voz único ou de poucos porta-vozes treinados.",
          ["lenta, para evitar erros, evitando qualquer posicionamento.", "ambígua, para proteger a imagem.", "por muitos porta-vozes, cada um com sua versão.", "somente depois de a imprensa publicar."],
          "Rapidez, verdade e consistência de mensagens reduzem boatos e danos à reputação.", CRI),
        Q("A comunicação de risco tem como objetivo",
          "informar o público sobre perigos e sobre como se proteger, com clareza e transparência sobre incertezas.",
          ["esconder informações para evitar pânico.", "promover os produtos da organização.", "ocultar incertezas técnicas.", "substituir a assessoria de imprensa."],
          "A comunicação de risco orienta o público com informação clara e confiável.", CRI),
        Q("Segundo o Estatuto Social da ABDI, a Política de Gestão de Riscos da Agência observará, entre outros, os riscos",
          "de imagem e reputação.",
          ["exclusivamente tributários.", "somente trabalhistas.", "apenas ambientais.", "só os de mercado de capitais."],
          "O art. 14, § 4º, I, do Estatuto inclui os riscos de imagem e reputação, ao lado de outros.", "Estatuto Social da ABDI (2024), art. 14, § 4º, I (abdi.com.br)"),
    ]),
    L("pub-l1", "Relacionamento com públicos de interesse e comunidades", 8, [
        "Stakeholders são os grupos que afetam ou são afetados pela organização: empregados, parceiros, governo, fornecedores, comunidade, imprensa, entre outros. A comunicação os mapeia e define abordagens diferentes para cada um.",
        "Matriz de poder e interesse: alto poder e alto interesse, gerenciar de perto; alto poder e baixo interesse, manter satisfeito; baixo poder e alto interesse, manter informado; baixo poder e baixo interesse, monitorar.",
        "Relacionamento com comunidades exige escuta ativa, diálogo, mapeamento de lideranças e canais acessíveis, respeito à cultura local e transparência sobre impactos.",
        "Relacionamento se constrói ao longo do tempo, com reuniões, eventos, canais de atendimento, pesquisa e prestação de contas. Para a ABDI, públicos estratégicos incluem governo, setor produtivo, parceiros, empregados e a sociedade."
    ], [
        ("Stakeholder", "Qualquer grupo ou pessoa que afeta ou é afetado pelas atividades da organização."),
        ("Alto poder e alto interesse", "Gerenciar de perto, com relacionamento próximo e frequente."),
        ("Baixo poder e alto interesse", "Manter informado.")
    ], [
        Q("O termo stakeholder designa",
          "qualquer grupo ou pessoa que afeta ou é afetado pelas atividades da organização.",
          ["apenas os acionistas da organização.", "somente os empregados.", "apenas os clientes.", "exclusivamente a imprensa."],
          "O conceito é amplo e inclui públicos internos e externos.", PUB),
        Q("Na matriz de poder e interesse, os públicos com alto poder e alto interesse devem ser",
          "gerenciados de perto.",
          ["apenas monitorados.", "ignorados.", "mantidos somente informados.", "contatados uma vez por ano."],
          "Públicos de alto poder e alto interesse exigem relacionamento próximo e frequente.", PUB),
        Q("Na matriz de poder e interesse, públicos com baixo poder e alto interesse devem ser",
          "mantidos informados.",
          ["gerenciados de perto, com prioridade máxima.", "excluídos dos canais de comunicação.", "monitorados apenas por pesquisa anual.", "tratados como inimigos."],
          "Mantê-los informados preserva o relacionamento e a legitimidade.", PUB),
        Q("No relacionamento com comunidades, uma prática recomendada é",
          "a escuta ativa, com diálogo, mapeamento de lideranças e canais acessíveis.",
          ["comunicar apenas por documentos técnicos.", "evitar contato direto.", "divulgar só informações positivas.", "tratar a comunidade apenas como destinatária de campanhas."],
          "A escuta ativa e a transparência constroem confiança de longo prazo.", PUB),
    ]),
], semente=3)

escrever("u-esp-legislacao-acessibilidade", "Ética e legislação, direito à informação, proteção de dados, acessibilidade e linguagem simples", "Específicos", "esp",
         ["esp-23", "esp-24", "esp-25", "esp-26"], [
    L("leg-l1", "Ética e legislação aplicadas à comunicação", 9, [
        "Constituição Federal, art. 5º: é livre a manifestação do pensamento, vedado o anonimato (IV); é assegurado o direito de resposta, proporcional ao agravo, além de indenização por dano material, moral ou à imagem (V); é livre a expressão da atividade intelectual, artística, científica e de comunicação, independentemente de censura ou licença (IX).",
        "São invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, com direito a indenização pela violação (art. 5º, X). É assegurado a todos o acesso à informação e resguardado o sigilo da fonte, quando necessário ao exercício profissional (art. 5º, XIV).",
        "Art. 220: a manifestação do pensamento, a criação, a expressão e a informação, sob qualquer forma, processo ou veículo, não sofrem restrição, observada a Constituição. Nenhuma lei conterá dispositivo que embarace a plena liberdade de informação jornalística (§ 1º), e é vedada toda censura política, ideológica e artística (§ 2º).",
        "Art. 37, § 1º: a publicidade dos órgãos públicos deve ter caráter educativo, informativo ou de orientação social, sem nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores.",
        "Na prática profissional, valem o compromisso com a verdade, o respeito à privacidade e à imagem, a correção de erros e a distinção clara entre informação, opinião e publicidade."
    ], [
        ("Direito de resposta (CF, art. 5º, V)", "Assegurado de forma proporcional ao agravo, além de indenização por dano material, moral ou à imagem."),
        ("Censura (CF, art. 220, § 2º)", "É vedada toda e qualquer censura de natureza política, ideológica e artística."),
        ("Publicidade de órgãos públicos (CF, art. 37, § 1º)", "Caráter educativo, informativo ou de orientação social, sem promoção pessoal de autoridades ou servidores.")
    ], [
        Q("De acordo com a Constituição Federal, é livre a manifestação do pensamento, sendo vedado o",
          "anonimato.",
          ["pseudônimo literário.", "direito de resposta.", "debate público.", "jornalismo investigativo."],
          "É o texto do art. 5º, IV.", CF + "art. 5º, IV"),
        Q("Segundo a Constituição Federal, o direito de resposta é assegurado",
          "de forma proporcional ao agravo, além da indenização por dano material, moral ou à imagem.",
          ["apenas a pessoas jurídicas.", "somente após condenação criminal.", "sem relação com o tamanho do agravo.", "apenas em jornais impressos."],
          "O art. 5º, V, estabelece o direito de resposta proporcional ao agravo e a indenização.", CF + "art. 5º, V"),
        Q("De acordo com o art. 220, § 2º, da Constituição Federal, é vedada",
          "toda e qualquer censura de natureza política, ideológica e artística.",
          ["a veiculação de publicidade.", "a atividade jornalística em órgãos públicos.", "a crítica a autoridades.", "a divulgação de pesquisas de opinião."],
          "O dispositivo veda a censura prévia de natureza política, ideológica e artística.", CF + "art. 220, § 2º"),
        Q("Segundo a Constituição Federal, são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado",
          "o direito a indenização pelo dano material ou moral decorrente de sua violação.",
          ["apenas o direito de resposta, sem indenização.", "somente a retratação voluntária.", "a perda da liberdade de expressão do autor.", "a censura prévia dos veículos."],
          "O art. 5º, X, protege esses direitos e assegura indenização.", CF + "art. 5º, X"),
        Q("A publicidade dos atos, programas, obras, serviços e campanhas dos órgãos públicos deverá ter, segundo a Constituição Federal, caráter",
          "educativo, informativo ou de orientação social, sem nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores.",
          ["comercial e de promoção do gestor.", "político-partidário.", "sigiloso.", "exclusivamente publicitário, com o nome da autoridade em destaque."],
          "É o art. 37, § 1º, da Constituição Federal.", CF + "art. 37, § 1º"),
    ]),
    L("leg-l2", "Direito à informação, transparência e acesso à informação", 9, [
        "CF, art. 5º, XXXIII: todos têm direito a receber dos órgãos públicos informações de seu interesse particular, ou de interesse coletivo ou geral, no prazo da lei, sob pena de responsabilidade, ressalvadas aquelas cujo sigilo seja imprescindível à segurança da sociedade e do Estado.",
        "Lei de Acesso à Informação (Lei 12.527/2011): regra é a publicidade e exceção é o sigilo (art. 3º, I). Os órgãos divulgam informações de interesse público independentemente de solicitações, ou seja, fazem transparência ativa (art. 3º, II, e art. 8º).",
        "Divulgação mínima (art. 8º, § 1º): competências e estrutura, endereços e telefones, repasses de recursos, despesas, licitações e contratos, dados para acompanhamento de programas e respostas a perguntas frequentes.",
        "Pedidos de acesso (arts. 10 e 11): qualquer interessado pode pedir, por qualquer meio legítimo, e não se pode exigir o motivo. O acesso é imediato se disponível. Do contrário, o prazo é de até 20 dias, prorrogável por 10, com justificativa.",
        "A LAI vale, no que couber, para entidades privadas sem fins lucrativos que recebam recursos públicos por contrato de gestão, convênios e instrumentos congêneres, quanto à parcela dos recursos recebida e à sua destinação (art. 2º). Informações pessoais têm acesso restrito por até 100 anos (art. 31)."
    ], [
        ("Regra geral da LAI", "Publicidade como preceito geral e sigilo como exceção (art. 3º, I)."),
        ("Transparência ativa", "Divulgação de informações de interesse público independentemente de solicitações (arts. 3º, II, e 8º)."),
        ("A LAI se aplica à ABDI?", "Sim, no que couber, por ser entidade privada sem fins lucrativos que recebe recursos públicos por contrato de gestão (art. 2º).")
    ], [
        Q("De acordo com a Lei de Acesso à Informação, a divulgação de informações de interesse público pelos órgãos e entidades, independentemente de solicitações, é chamada de",
          "transparência ativa.",
          ["transparência passiva.", "sigilo ativo.", "clipping institucional.", "publicidade mercadológica."],
          "A LAI manda divulgar informações de interesse público sem depender de pedidos (art. 3º, II, e art. 8º).", LAI + "arts. 3º, II, e 8º"),
        Q("A Lei 12.527/2011 estabelece, como diretriz, a observância da publicidade como preceito geral e do",
          "sigilo como exceção.",
          ["sigilo como regra e da publicidade como exceção.", "anonimato como regra geral.", "restrição de acesso como regra, com exceção para a imprensa.", "pagamento de taxa como regra."],
          "É o art. 3º, I.", LAI + "art. 3º, I"),
        Q("Entre as informações que devem constar, no mínimo, da divulgação a que se refere o art. 8º da LAI, estão",
          "registros de repasses, despesas, procedimentos licitatórios e contratos, e respostas a perguntas mais frequentes da sociedade.",
          ["apenas a lista de empregados com seus endereços residenciais.", "somente as atas reservadas dos conselhos.", "apenas fotos institucionais.", "somente as informações sigilosas classificadas."],
          "O art. 8º, § 1º, traz esse conteúdo mínimo, incluindo licitações, contratos, despesas e perguntas frequentes.", LAI + "art. 8º, § 1º"),
        Q("Quando não é possível conceder acesso imediato à informação solicitada, o órgão deve responder em prazo não superior a",
          "20 dias, prorrogável por mais 10 dias, mediante justificativa expressa.",
          ["5 dias, improrrogáveis.", "60 dias, sem prorrogação.", "90 dias, sem justificativa.", "2 dias úteis, sem prorrogação."],
          "O art. 11, §§ 1º e 2º, fixa 20 dias e permite prorrogação por mais 10, com justificativa.", LAI + "art. 11, §§ 1º e 2º"),
    ]),
    L("leg-l3", "Proteção de dados pessoais aplicada às atividades de comunicação", 9, [
        "A comunicação trata dados pessoais o tempo todo: mailing de imprensa, listas de e-mail, cadastros de eventos, imagens e vozes de pessoas, formulários e pesquisas. A LGPD (Lei 13.709/2018) se aplica a esse tratamento.",
        "Tratamento exige base legal (art. 7º), como consentimento do titular, cumprimento de obrigação legal, execução de política pública pela administração ou execução de contrato. Princípios do art. 6º: finalidade, adequação, necessidade, livre acesso, transparência, segurança, entre outros.",
        "Direitos do titular (art. 18): confirmação do tratamento, acesso, correção, anonimização, bloqueio ou eliminação de dados desnecessários ou excessivos, portabilidade e eliminação dos dados tratados com consentimento.",
        "O controlador indica um encarregado e divulga publicamente sua identidade e contato, preferencialmente no sítio eletrônico (art. 41). No Estatuto da ABDI, a DIREX aprova o relatório de impacto à proteção de dados pessoais e o plano de governança de dados e privacidade (art. 14, VI, c e d).",
        "Boas práticas em comunicação: coletar só o necessário, informar a finalidade, obter consentimento claro (opt-in), oferecer descadastro, proteger as informações e, em fotos de eventos, informar o uso das imagens."
    ], [
        ("Consentimento", "Uma das bases legais da LGPD para o tratamento de dados pessoais (art. 7º, I)."),
        ("Encarregado", "Pessoa indicada pelo controlador como canal de comunicação com titulares e com a ANPD. Seu contato é divulgado publicamente (art. 41)."),
        ("Princípio da necessidade", "Limita o tratamento ao mínimo necessário para atingir a finalidade.")
    ], [
        Q("Um setor de comunicação mantém uma lista de e-mails de interessados em receber a newsletter da instituição. Nessa atividade, os e-mails e nomes constituem",
          "dados pessoais, cujo tratamento deve observar a LGPD.",
          ["informações livres, que independem de qualquer base legal.", "dados anonimizados.", "informações classificadas como ultrassecretas.", "dados públicos, sem proteção legal alguma."],
          "Nome e e-mail identificam pessoa natural e são dados pessoais. O tratamento exige base legal e respeito aos princípios.", LGPD + "art. 5º, I"),
        Q("Entre as hipóteses legais que autorizam o tratamento de dados pessoais, previstas no art. 7º da LGPD, estão",
          "o consentimento do titular e o cumprimento de obrigação legal ou regulatória pelo controlador.",
          ["a conveniência do controlador, em qualquer caso.", "apenas a existência de um mailing já formado.", "o interesse comercial de terceiros, sempre.", "a ausência de objeção do titular, sempre."],
          "O art. 7º, I e II, traz esses exemplos. As demais opções não são, por si, bases legais.", LGPD + "art. 7º, I e II"),
        Q("O princípio da LGPD segundo o qual o tratamento deve se limitar ao mínimo necessário para atingir sua finalidade é o da",
          "necessidade.",
          ["transparência.", "livre acesso.", "não discriminação.", "responsabilização."],
          "O art. 6º, III, define a necessidade.", LGPD + "art. 6º, III"),
        Q("Quanto ao encarregado pelo tratamento de dados pessoais, a LGPD determina que sua identidade e informações de contato sejam divulgadas",
          "publicamente, de forma clara e objetiva, preferencialmente no sítio eletrônico do controlador.",
          ["apenas internamente, ao Conselho Fiscal.", "somente a órgãos de controle.", "somente por pedido judicial.", "em sigilo absoluto."],
          "É o art. 41, § 1º.", LGPD + "art. 41, § 1º"),
    ]),
    L("leg-l4", "Acessibilidade, inclusão e linguagem simples na comunicação", 10, [
        "Lei Brasileira de Inclusão (Lei 13.146/2015), art. 3º: acessibilidade é a possibilidade e a condição de alcance, com segurança e autonomia, de espaços, equipamentos, informação e comunicação, inclusive sistemas e tecnologias. Desenho universal é a concepção de produtos, ambientes e serviços para uso por todas as pessoas, sem necessidade de adaptação. Comunicação abrange Libras, textos, Braille, caracteres ampliados, dispositivos multimídia, linguagem simples, escrita e oral, entre outros.",
        "Art. 63: é obrigatória a acessibilidade nos sítios da internet mantidos por empresas com sede ou representação comercial no País ou por órgãos de governo, conforme as melhores práticas e diretrizes internacionais. Os sítios devem conter o símbolo de acessibilidade em destaque.",
        "Art. 67: os serviços de radiodifusão de sons e imagens devem permitir, entre outros recursos, a subtitulação por legenda oculta, a janela com intérprete de Libras e a audiodescrição.",
        "Lei 15.263/2025 (Política Nacional de Linguagem Simples): define linguagem simples como técnicas para transmitir informações de forma clara e objetiva, para que o cidadão encontre, compreenda e use a informação (art. 4º).",
        "Técnicas (art. 5º): frases em ordem direta e curtas, uma ideia por parágrafo, palavras comuns, explicar termos técnicos, nome completo antes das siglas, texto esquemático quando couber, informações mais importantes primeiro, voz ativa, evitar frases intercaladas e redundâncias, e testar a mensagem com o público-alvo. A comunicação oficial para comunidades indígenas deve ter, sempre que possível, versão na língua dos destinatários (art. 6º)."
    ], [
        ("Desenho universal", "Concepção de produtos, ambientes, programas e serviços para uso por todas as pessoas, sem necessidade de adaptação (LBI, art. 3º, II)."),
        ("Recursos de acessibilidade na radiodifusão (LBI, art. 67)", "Legenda oculta, janela com intérprete de Libras e audiodescrição."),
        ("Linguagem simples (Lei 15.263/2025, art. 4º)", "Técnicas para transmitir informações de modo claro e objetivo, de forma que o cidadão encontre, compreenda e use a informação.")
    ], [
        Q("Segundo a Lei Brasileira de Inclusão, a concepção de produtos, ambientes, programas e serviços a serem usados por todas as pessoas, sem necessidade de adaptação ou de projeto específico, é chamada de",
          "desenho universal.",
          ["adaptação razoável.", "tecnologia assistiva.", "barreira atitudinal.", "acessibilidade tarifária."],
          "O art. 3º, II, define o desenho universal.", LBI + "art. 3º, II"),
        Q("A Lei Brasileira de Inclusão estabelece que os serviços de radiodifusão de sons e imagens devem permitir, entre outros recursos,",
          "a subtitulação por legenda oculta, a janela com intérprete de Libras e a audiodescrição.",
          ["apenas a transmissão em preto e branco.", "somente a exibição de publicidade.", "apenas o uso de intérprete em programas religiosos.", "somente a transmissão em alta resolução."],
          "É a lista do art. 67, I a III.", LBI + "art. 67"),
        Q("De acordo com a Lei Brasileira de Inclusão, é obrigatória a acessibilidade nos sítios da internet mantidos",
          "por empresas com sede ou representação comercial no País ou por órgãos de governo, e eles devem conter o símbolo de acessibilidade em destaque.",
          ["apenas por organizações estrangeiras.", "somente por escolas públicas.", "apenas por veículos de imprensa.", "por pessoas físicas, em qualquer caso."],
          "O art. 63 e o § 1º tratam da obrigação e do símbolo de acessibilidade.", LBI + "art. 63, caput e § 1º"),
        Q("Entre as técnicas de linguagem simples previstas na Política Nacional de Linguagem Simples (Lei 15.263/2025) estão",
          "redigir frases curtas e em ordem direta, desenvolver uma ideia por parágrafo e redigir o nome completo antes das siglas.",
          ["usar frases longas com muitas intercalações.", "empregar jargões sem explicação.", "usar o máximo de palavras estrangeiras.", "deixar as informações mais importantes para o final."],
          "As técnicas do art. 5º incluem frases curtas e diretas, uma ideia por parágrafo, nome completo antes das siglas e informações importantes primeiro.", LS + "art. 5º"),
        Q("A Política Nacional de Linguagem Simples (Lei 15.263/2025) recomenda que a administração pública",
          "teste com o público-alvo se a mensagem está compreensível.",
          ["evite qualquer teste com cidadãos.", "use somente a linguagem técnica do órgão.", "dispense a explicação de termos técnicos.", "publique apenas em língua estrangeira."],
          "O art. 5º, XVIII, inclui testar a mensagem com o público-alvo.", LS + "art. 5º, XVIII"),
    ]),
], semente=4)
