from lib import Q, L, escrever

ET = "Regulamento de Ética e Conduta da ABDI (Resolução CD 004/2022, de 16/03/2022), "
PL = "Planejamento Estratégico ABDI 2024-2029 (Caderno de Planejamento, nov/2024; aprovado pela Resolução CD 009/2024), "
ETU = " (abdi.com.br)"

escrever("u-inst-etica-planejamento", "Ética e Conduta; Planejamento Estratégico 2024-2029", "Institucionais", "etica", ["inst-04"], [
    L("etp-l1", "Ética e Conduta: objetivo, valores, direitos e deveres", 8, [
        "O Regulamento (Resolução CD 004/2022) estabelece os padrões éticos e de comportamento esperados dos profissionais da ABDI, nas relações entre si, com parceiros, clientes, fornecedores, prestadores de serviços, Poder Público e órgãos de fiscalização e controle (art. 1º).",
        "Aplica-se a conselheiros, dirigentes, empregados, estagiários, menores aprendizes e prestadores de serviços técnicos e operacionais (art. 2º). Em contratos, convênios e acordos de cooperação, a ABDI exige dos contratados, convenentes ou parceiros a observância do Regulamento ou de documento análogo (parágrafo único).",
        "Art. 3º traz 12 valores e princípios, entre eles cooperação, compromisso com a competitividade, inovação, valorização humana, ética e transparência, legalidade, honestidade, justiça, impessoalidade, lealdade, respeito aos direitos individuais, veracidade, prestação de contas e preservação da boa imagem e do patrimônio da ABDI.",
        "Direitos (art. 4º): ser respeitado e igualmente tratado, trabalhar em ambiente adequado, ter interlocução livre com colegas e superiores e ter respeitado o sigilo de informações pessoais.",
        "Deveres (art. 5º), entre outros: conduta que inspire confiança, zelo e honestidade, sigilo sobre negócios e projetos, comunicar ao superior possíveis conflitos de interesses, cumprir ordens superiores, exceto as manifestamente ilegais, imorais e antiéticas, e requerer prévia autorização da Diretoria para publicar ou expor estudos, pesquisas e pareceres feitos por demanda da Agência."
    ], [
        ("A quem se aplica o Regulamento de Ética e Conduta?", "A conselheiros, dirigentes, empregados, estagiários, menores aprendizes e prestadores de serviços técnicos e operacionais (art. 2º)."),
        ("Ordens superiores no Regulamento", "Devem ser cumpridas, exceto quando manifestamente ilegais, imorais e antiéticas (art. 5º)."),
        ("Publicar estudos feitos por demanda da ABDI", "Exige prévia autorização da respectiva Diretoria, mesmo que o autor seja exclusivamente o empregado (art. 5º).")
    ], [
        Q("De acordo com o Regulamento de Ética e Conduta da ABDI, suas disposições se aplicam",
          "a conselheiros, dirigentes, empregados, estagiários, menores aprendizes e prestadores de serviços técnicos e operacionais.",
          ["apenas aos empregados do quadro efetivo.", "somente aos membros da Diretoria Executiva.", "exclusivamente a fornecedores contratados.", "apenas aos conselheiros do Conselho Deliberativo."],
          "O art. 2º lista todos esses grupos. O regulamento não se restringe aos empregados efetivos.", ET + "art. 2º" + ETU),
        Q("Ao celebrar contratos, convênios ou acordos de cooperação, a ABDI, segundo o Regulamento de Ética e Conduta, exigirá de seus contratados, convenentes ou parceiros",
          "a observância das normas do Regulamento ou de documento análogo, caso exista.",
          ["apenas a assinatura de termo de sigilo.", "a adesão ao Estatuto da ABDI.", "a doação de parte dos recursos recebidos.", "nenhuma exigência de natureza ética."],
          "O parágrafo único do art. 2º prevê essa exigência de observância ao regulamento ou a documento análogo da outra parte.", ET + "art. 2º, parágrafo único" + ETU),
        Q("Entre os valores e princípios éticos listados no art. 3º do Regulamento de Ética e Conduta da ABDI estão",
          "a cooperação, o compromisso com a competitividade, a inovação e a valorização humana.",
          ["a hierarquia rígida, o sigilo irrestrito e a competição entre empregados.", "o lucro, a concorrência entre unidades e a autonomia absoluta.", "a informalidade, a flexibilidade de regras e a discrição absoluta.", "o corporativismo, a reserva de informações e o personalismo."],
          "O art. 3º enumera, entre outros, cooperação, compromisso com a competitividade, inovação em constante atualização e valorização humana.", ET + "art. 3º" + ETU),
        Q("Quanto ao cumprimento de ordens superiores, o Regulamento de Ética e Conduta da ABDI estabelece que o profissional deve",
          "cumpri-las, exceto quando manifestamente ilegais, imorais e antiéticas.",
          ["cumprir qualquer ordem, sem exceção.", "recusar todas as ordens que não concordar.", "cumprir apenas as ordens por escrito.", "cumprir as ordens somente após aprovação do Conselho Fiscal."],
          "Entre os deveres do art. 5º está cumprir as ordens superiores, exceto as manifestamente ilegais, imorais e antiéticas.", ET + "art. 5º" + ETU),
        Q("Um empregado da ABDI produziu, por demanda da Agência, um estudo sobre comunicação institucional e deseja publicá-lo em um periódico. De acordo com o Regulamento, ele deve",
          "requerer prévia autorização da respectiva Diretoria, por meio físico ou eletrônico, ainda que seja o autor exclusivo.",
          ["publicar livremente, por ser o autor.", "comunicar a Diretoria apenas depois da publicação.", "pedir autorização apenas ao colega de equipe.", "publicar sem identificar a ABDI."],
          "O art. 5º exige prévia autorização da Diretoria para publicação ou exposição de estudos e pareceres realizados por demanda da Agência, mesmo de autoria exclusiva.", ET + "art. 5º" + ETU),
    ]),
    L("etp-l2", "Vedações e critérios de conduta", 9, [
        "Art. 6º veda, entre outras condutas: manifestar-se em nome da ABDI sem autorização ou habilitação, discriminar, praticar assédio moral ou sexual, usar equipamentos da ABDI para fins particulares, repassar a terceiros informações da ABDI, compactuar ou omitir-se diante de irregularidades e retirar bens da ABDI sem autorização.",
        "Também é vedado manter sob chefia imediata, em cargo ou função de confiança, cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade até o terceiro grau.",
        "Mídias sociais (art. 7º): agir com responsabilidade, não postar imagens ou comentários que revelem informações confidenciais da ABDI e não emitir juízo negativo de valor sobre prestadores, fornecedores ou colegas.",
        "Confidencialidade (art. 8º): sigilo sobre informações de projetos, não compartilhar com quem não precise delas, informar ao gerente qualquer vazamento e proteger usuários e senhas, sem compartilhá-los.",
        "Propriedade intelectual (art. 9º): a utilização e a divulgação externa de documentos e informações sujeitos à propriedade intelectual da ABDI exigem aprovação prévia e formal de um dos membros da Diretoria Executiva. Recursos da ABDI (art. 10) devem ser usados de forma adequada e voltada às atividades profissionais. Doações e patrocínios seguem regulamento próprio (art. 11)."
    ], [
        ("Falar em nome da ABDI", "É vedado manifestar-se em nome da ABDI quando não autorizado ou habilitado (art. 6º, I)."),
        ("Divulgação externa de informação com propriedade intelectual da ABDI", "Exige aprovação prévia e formal de um membro da Diretoria Executiva (art. 9º)."),
        ("Mídias sociais", "Não postar informações confidenciais nem emitir juízo negativo de valor sobre prestadores, fornecedores ou colegas (art. 7º).")
    ], [
        Q("Segundo o Regulamento de Ética e Conduta da ABDI, é vedado ao profissional da Agência",
          "manifestar-se em nome da ABDI quando não autorizado ou habilitado para isso.",
          ["participar de eventos da área de comunicação.", "usar o e-mail profissional para atividades de trabalho.", "comunicar irregularidades ao superior.", "pedir orientação à Ouvidoria."],
          "O art. 6º, I, veda a manifestação em nome da ABDI sem autorização ou habilitação. As demais condutas são permitidas ou até esperadas.", ET + "art. 6º, I" + ETU),
        Q("De acordo com o Regulamento, no uso de mídias sociais os colaboradores devem evitar, especialmente,",
          "postar imagens ou comentários que revelem informações confidenciais da ABDI e emitir juízo negativo de valor sobre prestadores, fornecedores ou colegas.",
          ["divulgar eventos públicos da ABDI com autorização.", "seguir perfis institucionais da ABDI.", "compartilhar notícias já publicadas pela imprensa sobre a ABDI.", "curtir publicações dos parceiros."],
          "O art. 7º lista essas duas vedações, que protegem a confidencialidade e a imagem da ABDI e das pessoas.", ET + "art. 7º" + ETU),
        Q("A utilização e a divulgação externa de documentos e informações sujeitos à propriedade intelectual da ABDI devem ser aprovadas prévia e formalmente por",
          "um dos membros da Diretoria Executiva.",
          ["qualquer empregado que tenha elaborado o documento.", "o Conselho Fiscal.", "a Ouvidoria.", "o gerente imediato, isoladamente."],
          "O art. 9º atribui essa aprovação a um dos membros da Diretoria Executiva.", ET + "art. 9º" + ETU),
        Q("Quanto aos usuários e senhas de acesso a sistemas da ABDI, o Regulamento de Ética e Conduta determina que o empregado deve",
          "protegê-los e não os compartilhar com outros colaboradores de qualquer tipo.",
          ["compartilhá-los com a equipe para agilizar o trabalho.", "entregá-los ao gestor, que os guardará.", "anotá-los em local visível para emergências.", "compartilhá-los apenas com estagiários."],
          "O art. 8º, IV, exige proteger usuários e senhas, sem compartilhamento com outros colaboradores.", ET + "art. 8º, IV" + ETU),
        Q("É vedado, pelo Regulamento de Ética e Conduta da ABDI, manter sob chefia imediata, em cargo ou função de confiança,",
          "cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade até o terceiro grau.",
          ["apenas o cônjuge, sem outros parentes.", "parentes de qualquer grau, inclusive o quinto.", "apenas parentes de primeiro grau.", "somente amigos pessoais."],
          "O art. 6º veda a subordinação direta de cônjuge, companheiro ou parentes até o terceiro grau.", ET + "art. 6º" + ETU),
    ]),
    L("etp-l3", "Conflito de interesses, descumprimento e canais de orientação", 9, [
        "Atividades paralelas (art. 12): não podem ocorrer no expediente, não podem ser exercidas com fornecedores ou parceiros contratados ou conveniados pela ABDI e, quando envolvem fóruns, palestras ou atividades docentes, devem ser comunicadas antes ao gestor. Vender produtos ou serviços nas dependências exige autorização formal da Gestão de Pessoas.",
        "Atividade política, sindical e religiosa (art. 13): é direito individual, mas deve ocorrer fora do expediente e sem uso de recursos da ABDI. Não se pode fazer campanha religiosa ou político-partidária com recursos da ABDI.",
        "Relacionamento amoroso (art. 14): não é permitida relação de liderança ou subordinação, direta ou indireta, entre quem tem envolvimento amoroso, e recomenda-se que não trabalhem no mesmo projeto. O gestor encaminha o caso à Gestão de Pessoas, que reporta à Diretoria Executiva.",
        "Brindes, presentes e favores (art. 15): só se aceitam brindes promocionais sem valor comercial. Se não for possível recusar um presente, ele é encaminhado à Gestão de Pessoas, que faz sorteio entre todos os colaboradores. Dinheiro, propina e suborno são proibidos em qualquer situação. Informações privilegiadas não podem ser usadas em benefício próprio ou de terceiros (art. 17).",
        "Descumprimento (art. 18): medidas disciplinares conforme o Manual de Sindicância. Condenação transitada em julgado por calúnia, injúria ou difamação no ambiente de trabalho é falta grave. Violações apuradas por comissão do Colegiado de Apuração podem levar a esclarecimento e treinamento, ajustes ou sanções disciplinares.",
        "Orientação (art. 19): chefia imediata (processos e estratégia de trabalho), Gestão de Pessoas (ambiente e relações de trabalho), Comitê de Governança, Integridade e Gestão de Riscos (critérios do Regulamento) e Ouvidoria (violações à legislação e ao Regulamento, pedidos, reclamações, sugestões, elogios, críticas e denúncias)."
    ], [
        ("Presente que não pode ser recusado (art. 15, III)", "É encaminhado à Gestão de Pessoas, que faz sorteio entre todos os colaboradores."),
        ("Quem recebe denúncias e reclamações?", "A Ouvidoria (art. 19, IV)."),
        ("Relacionamento amoroso entre profissionais", "Não pode haver relação de liderança ou subordinação, direta ou indireta (art. 14, I)."),
        ("Calúnia, injúria ou difamação no trabalho", "Condenação transitada em julgado é falta grave (art. 18, § 1º).")
    ], [
        Q("Um empregado da ABDI recebeu pelo correio um presente de valor expressivo enviado por um fornecedor, e não foi possível recusá-lo. Segundo o Regulamento de Ética e Conduta, o presente deve ser",
          "encaminhado à área de Gestão de Pessoas, que fará um sorteio entre todos os colaboradores da Agência.",
          ["guardado pelo empregado, desde que informe o gestor.", "vendido, com o valor revertido ao setor.", "devolvido apenas se o fornecedor pedir.", "dividido entre os integrantes da equipe do destinatário."],
          "O art. 15, III, prevê esse encaminhamento quando a recusa não é possível ou gera desconforto.", ET + "art. 15, III" + ETU),
        Q("Pelo Regulamento de Ética e Conduta da ABDI, em relação a brindes, é correto afirmar que o colaborador poderá receber",
          "única e exclusivamente brindes promocionais sem valor comercial, como material de escritório e camisetas.",
          ["qualquer presente de até cem reais.", "convites para viagens pagas por fornecedores.", "dinheiro, desde que declarado.", "presentes de parceiros no fim do ano, sem limite."],
          "O art. 15, I e II, restringe a aceitação a brindes promocionais sem valor comercial.", ET + "art. 15, I e II" + ETU),
        Q("A orientação sobre questões relacionadas a violações à legislação ou ao Regulamento de Ética e Conduta, bem como denúncias, reclamações e sugestões, deve ser buscada junto à",
          "Ouvidoria.",
          ["Diretoria Jurídica, exclusivamente.", "Unidade de Compras.", "chefia imediata, apenas.", "Conselho Fiscal."],
          "O art. 19, IV, indica a Ouvidoria para essas manifestações.", ET + "art. 19, IV" + ETU),
        Q("De acordo com o Regulamento de Ética e Conduta da ABDI, a atividade política, sindical e religiosa do colaborador",
          "é um direito individual respeitado, mas deve ocorrer fora do expediente e sem uso de recursos da ABDI.",
          ["é proibida em qualquer circunstância.", "pode ser feita durante o expediente, com autorização verbal.", "pode usar o e-mail institucional para divulgar candidaturas.", "só é permitida a dirigentes."],
          "O art. 13 respeita o direito, mas veda campanha religiosa ou político-partidária com recursos da ABDI e exige que ocorra fora do expediente.", ET + "art. 13" + ETU),
        Q("A condenação de um empregado, por decisão judicial transitada em julgado, por crime de calúnia, injúria ou difamação praticado no ambiente de trabalho constitui, segundo o Regulamento,",
          "falta grave, punível nos termos do Manual de Sindicância e Procedimentos Disciplinares da ABDI.",
          ["falta leve, sujeita a advertência verbal.", "fato sem consequência disciplinar.", "motivo de simples orientação pela chefia.", "atenuante para outras punições."],
          "O art. 18, § 1º, qualifica essa condenação como falta grave.", ET + "art. 18, § 1º" + ETU),
    ]),
    L("etp-l4", "Planejamento Estratégico 2024-2029 e atuação institucional", 9, [
        "O Caderno de Planejamento 2024-2029 foi publicado em novembro de 2024. A Resolução do Conselho Deliberativo 009, de 27/11/2024, aprovou o Planejamento Estratégico 2024-2029 ajustado e o envio ao Ministério do Desenvolvimento, Indústria, Comércio e Serviços da proposta de modificação do Contrato de Gestão 2024-2029. O edital cita a Resolução 008/2023, versão anterior.",
        "Missão: desenvolver ações que contribuam para que o Governo Federal formule e implemente políticas industriais inovadoras, competitivas, tecnológicas e sustentáveis, visando à promoção e ao desenvolvimento socioeconômico do país.",
        "Visão: ser referência na promoção de soluções inovadoras, sustentáveis e inclusivas do setor produtivo. Valores: cooperação, compromisso com a competitividade, inovação, valorização humana e ética e transparência.",
        "Seis objetivos estratégicos: (1) ampliar boas práticas ambientais, sociais e de governança no setor produtivo; (2) ampliar a maturidade digital do setor produtivo; (3) contribuir com a formulação, execução, monitoramento e avaliação de políticas públicas; (4) fortalecer e consolidar a comunicação institucional; (5) consolidar a governança e a integridade corporativa, incluindo a agenda ASG; (6) modernizar a política de gestão de pessoas.",
        "Comunicação institucional (objetivo 4): estratégia interna e externa para transmitir identidade, valores, objetivos e mensagens-chave, com visibilidade, reputação e compreensão da Agência. Indicadores: presença positiva e neutra na imprensa tradicional e digital, e índice que mede a reputação na imprensa e nas redes sociais.",
        "Atuação institucional: promover o desenvolvimento industrial, a inovação, a transformação digital e a difusão de tecnologia, conforme o art. 1º da Lei 11.080/2004 e o art. 2º do Decreto 5.352/2005."
    ], [
        ("Visão da ABDI (2024-2029)", "Ser referência na promoção de soluções inovadoras, sustentáveis e inclusivas do setor produtivo."),
        ("Quantos objetivos estratégicos e qual trata de comunicação?", "Seis. O objetivo 4: fortalecer e consolidar a comunicação institucional."),
        ("Valores da ABDI no planejamento", "Cooperação, compromisso com a competitividade, inovação, valorização humana e ética e transparência."),
        ("Resolução que aprovou o planejamento ajustado 2024-2029", "Resolução do Conselho Deliberativo 009, de 27/11/2024. O edital cita a Resolução 008/2023.")
    ], [
        Q("De acordo com o Planejamento Estratégico 2024-2029 da ABDI, a visão da Agência é",
          "ser referência na promoção de soluções inovadoras, sustentáveis e inclusivas do setor produtivo.",
          ["ser a maior consultoria de tecnologia do país.", "administrar fundos de investimento da União.", "regular o comércio exterior brasileiro.", "financiar diretamente empresas industriais."],
          "É o texto da visão no Caderno de Planejamento 2024-2029.", PL + "seção 2.3, p. 19" + ETU),
        Q("O Planejamento Estratégico 2024-2029 da ABDI estabelece seis objetivos estratégicos. Entre eles está",
          "fortalecer e consolidar a comunicação institucional.",
          ["ampliar a arrecadação própria com taxas de inscrição.", "reduzir a atuação no setor produtivo.", "concentrar a gestão em uma única diretoria.", "substituir o contrato de gestão por contratos pontuais."],
          "O objetivo 4 do plano trata da comunicação institucional da ABDI.", PL + "seção 2.3, p. 19" + ETU),
        Q("A Resolução do Conselho Deliberativo 009, de 27 de novembro de 2024, aprovou",
          "o Planejamento Estratégico 2024-2029 ajustado e o envio da proposta de modificação do Contrato de Gestão 2024-2029 ao ministério supervisor.",
          ["o Regulamento de Ética e Conduta.", "o Estatuto Social da ABDI.", "o Regulamento de Licitações e Contratos.", "o orçamento-programa de 2025."],
          "A resolução aprova o planejamento estratégico ajustado e o envio da proposta de modificação do contrato de gestão. O Regulamento de Ética foi aprovado pela Resolução 004/2022.", PL + "Resolução CD 009/2024, arts. 1º e 2º" + ETU),
        Q("Entre os indicadores do objetivo estratégico de comunicação institucional da ABDI no Planejamento 2024-2029 estão",
          "a presença positiva e neutra da ABDI na imprensa e um índice que mede a reputação da ABDI na imprensa e nas redes sociais.",
          ["o número de contratos de licitação assinados.", "o total de arrecadação de convênios.", "o número de empregados contratados.", "a quantidade de normas internas publicadas."],
          "Os dois indicadores são citados no detalhamento do objetivo de comunicação institucional.", PL + "seção 2.3, objetivo de comunicação institucional" + ETU),
        Q("Entre os valores da ABDI no Planejamento Estratégico 2024-2029 estão",
          "cooperação, compromisso com a competitividade, inovação, valorização humana e ética e transparência.",
          ["hierarquia, sigilo, lucro, competição e disciplina.", "tradição, autonomia absoluta, economicidade e burocracia.", "velocidade, informalidade, individualismo e concorrência.", "estabilidade, exclusividade, reserva e personalismo."],
          "Os cinco valores constam do plano e coincidem com parte dos valores do Regulamento de Ética e Conduta (art. 3º).", PL + "seção 2.3, p. 19" + ETU),
    ]),
], numeros=[
    ("Regulamento de Ética e Conduta", "Resolução CD 004/2022, de 16/03/2022; 25 artigos em 10 capítulos", "Regulamento de Ética e Conduta da ABDI (abdi.com.br)"),
    ("Parentesco vedado sob chefia imediata", "cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade até o terceiro grau", "Regulamento de Ética e Conduta, art. 6º"),
    ("Objetivos estratégicos 2024-2029", "6 objetivos; o 4 é fortalecer e consolidar a comunicação institucional", "Planejamento Estratégico 2024-2029, seção 2.3"),
    ("Valores da ABDI", "5: cooperação, compromisso com a competitividade, inovação, valorização humana, ética e transparência", "Planejamento Estratégico 2024-2029, seção 2.3"),
    ("Resolução que aprovou o planejamento ajustado", "Resolução CD 009, de 27/11/2024 (o edital cita a 008/2023)", "Planejamento Estratégico 2024-2029, p. 32"),
])
