from lib import Q, L, escrever

BASE = "Referência conceitual: fundamentos de informática (conteúdo estável, sem dependência de versão)"
SEG = "Referência conceitual: segurança da informação (tríade CIA e boas práticas)"
NIST = "Referência conceitual: NIST SP 800-145, The NIST Definition of Cloud Computing (2011)"
LAI = "Lei 12.527/2011 (planalto.gov.br)"
MCI = "Lei 12.965/2014 (planalto.gov.br)"
LGPD = "Lei 13.709/2018 (planalto.gov.br)"
CP = "Código Penal, art. 154-A, acrescentado pela Lei 12.737/2012 e com redação da Lei 14.155/2021 (planalto.gov.br, del2848compilado)"

# ------------------------------------------------------------------ conceitos, Windows, atalhos
escrever("u-info-conceitos", "Conceitos de informática, Windows 10 e 11, atalhos e acessibilidade", "Gerais", "info",
         ["info-01", "info-02", "info-10"], [
    L("icon-l1", "Hardware, software e armazenamento", 7, [
        "Hardware é a parte física (processador, memórias, discos, periféricos). Software é a parte lógica: sistema operacional, aplicativos e utilitários.",
        "Memória RAM é volátil: perde os dados quando o computador é desligado. ROM e dispositivos de armazenamento (HD, SSD) guardam dados de forma permanente. O SSD não tem partes móveis.",
        "Unidades: 1 byte tem 8 bits. Os múltiplos (KB, MB, GB, TB) crescem de 1.024 em 1.024 nas provas de concurso.",
        "Periféricos de entrada: teclado, mouse, scanner. De saída: monitor, impressora. De entrada e saída: tela sensível ao toque, impressora multifuncional. Extensões: .docx e .odt (texto), .xlsx e .ods (planilha), .pptx e .odp (apresentação), .pdf, .jpg, .png, .mp3, .zip."
    ], [
        ("Qual memória é volátil?", "A memória RAM: perde o conteúdo quando o equipamento é desligado."),
        ("Quantos bits tem um byte?", "8 bits."),
        ("Extensões de documentos do LibreOffice", ".odt (Writer), .ods (Calc) e .odp (Impress).")
    ], [
        Q("Sobre a memória RAM de um computador, é correto afirmar que ela é",
          "volátil, pois perde seu conteúdo quando o computador é desligado.",
          ["permanente, pois armazena arquivos mesmo desligada.", "somente de leitura, e não pode ser alterada.", "um dispositivo de entrada de dados.", "exclusiva de computadores antigos."],
          "A RAM guarda temporariamente os programas e dados em uso. Para guardar de forma permanente, usam-se HD, SSD e outras mídias.", BASE),
        Q("Um byte é formado por",
          "8 bits.",
          ["4 bits.", "10 bits.", "16 bits.", "1.024 bits."],
          "Por definição, 1 byte equivale a 8 bits.", BASE),
        Q("Um scanner é classificado como periférico de",
          "entrada.",
          ["saída.", "processamento.", "armazenamento volátil.", "alimentação."],
          "O scanner converte documentos em imagens digitais que entram no computador.", BASE),
        Q("Um arquivo com extensão .ods foi criado, por padrão, no aplicativo",
          "Calc, do LibreOffice (planilha).",
          ["Writer, do LibreOffice (texto).", "Impress, do LibreOffice (apresentação).", "Word, do Microsoft 365.", "PowerPoint, do Microsoft 365."],
          "A extensão .ods identifica planilhas no formato OpenDocument, usado pelo Calc.", BASE),
    ]),
    L("icon-l2", "Windows 10 e 11: arquivos, pastas e recursos", 8, [
        "O Explorador de Arquivos organiza arquivos e pastas (atalho Win+E). Nomes de arquivos não podem conter os caracteres \\ / : * ? \" < > |.",
        "Ao excluir um arquivo do disco local, ele vai para a Lixeira e pode ser restaurado. Shift+Delete exclui sem passar pela Lixeira. Arquivos excluídos de pen drive ou de unidade de rede também não vão para a Lixeira.",
        "Gerenciador de Tarefas: Ctrl+Shift+Esc. Configurações: Win+I. Bloquear a sessão: Win+L. O Windows 11 mantém essas funções e traz o menu Iniciar centralizado e layouts de janelas.",
        "A barra de tarefas mostra programas abertos e fixados. A área de trabalho exibe atalhos. Pesquisa e compartilhamento (inclusive via OneDrive) estão integrados ao sistema."
    ], [
        ("Excluir sem passar pela Lixeira", "Shift+Delete."),
        ("Abrir o Gerenciador de Tarefas", "Ctrl+Shift+Esc."),
        ("Caracteres proibidos em nomes de arquivos do Windows", "\\ / : * ? \" < > |")
    ], [
        Q("Para excluir um arquivo do disco local do Windows sem enviá-lo à Lixeira, o usuário deve selecioná-lo e pressionar",
          "Shift+Delete.",
          ["Ctrl+Delete.", "Alt+Delete.", "Ctrl+Z.", "Win+Delete."],
          "A combinação Shift+Delete exclui permanentemente, com confirmação.", BASE),
        Q("Qual dos nomes abaixo é inválido para um arquivo no Windows?",
          "relatorio?final.docx",
          ["relatorio_final.docx", "relatorio-final.docx", "relatorio final 2026.docx", "relatorio.final.docx"],
          "O ponto de interrogação é um dos caracteres proibidos em nomes de arquivos.", BASE),
        Q("O atalho que abre diretamente o Gerenciador de Tarefas do Windows é",
          "Ctrl+Shift+Esc.",
          ["Ctrl+Alt+F4.", "Win+T.", "Alt+Tab.", "Ctrl+Shift+N."],
          "Ctrl+Shift+Esc abre o Gerenciador de Tarefas, útil para encerrar programas que não respondem.", BASE),
        Q("Sobre arquivos excluídos de um pen drive no Windows, é correto afirmar que",
          "não passam pela Lixeira e são removidos diretamente.",
          ["sempre vão para a Lixeira do computador.", "são enviados à nuvem automaticamente.", "são copiados para a área de trabalho.", "só podem ser excluídos pelo administrador."],
          "Mídias removíveis e unidades de rede não usam a Lixeira do disco local.", BASE),
    ]),
    L("icon-l3", "Atalhos, acessibilidade e produtividade", 7, [
        "Atalhos gerais: Ctrl+C copiar, Ctrl+X recortar, Ctrl+V colar, Ctrl+Z desfazer, Ctrl+Y refazer, Ctrl+A selecionar tudo, Ctrl+F localizar, Alt+Tab alternar janelas, F2 renomear, F5 atualizar, Alt+F4 fechar.",
        "Win+D mostra a área de trabalho, Win+L bloqueia, Win+Shift+S abre a captura de tela por recorte, Print Screen captura a tela inteira.",
        "Acessibilidade: Lupa (Win e sinal de mais), Narrador (Win+Ctrl+Enter), alto contraste, teclado virtual e teclas de aderência (ativadas ao pressionar Shift cinco vezes).",
        "Digitalização converte papel em arquivo digital. O OCR (reconhecimento óptico de caracteres) transforma a imagem de um texto em texto editável."
    ], [
        ("Bloquear a tela do Windows", "Win+L."),
        ("Renomear o arquivo selecionado", "F2."),
        ("OCR", "Reconhecimento óptico de caracteres: converte imagens de texto em texto editável.")
    ], [
        Q("O atalho Win+L no Windows serve para",
          "bloquear a sessão do usuário.",
          ["abrir a Lixeira.", "mostrar a área de trabalho.", "abrir a Lupa.", "fechar todos os programas."],
          "Win+L bloqueia a sessão, exigindo autenticação para voltar. A área de trabalho é exibida com Win+D.", BASE),
        Q("Para renomear um arquivo selecionado no Explorador de Arquivos, usa-se a tecla",
          "F2.",
          ["F1.", "F5.", "F10.", "F12."],
          "F2 coloca o nome do arquivo em modo de edição. F5 atualiza a janela.", BASE),
        Q("O recurso de acessibilidade do Windows que lê em voz alta o conteúdo da tela é o",
          "Narrador.",
          ["Lupa.", "Teclado virtual.", "Alto contraste.", "Teclas de aderência."],
          "O Narrador é o leitor de tela do Windows (Win+Ctrl+Enter). A Lupa amplia partes da tela.", BASE),
        Q("A tecnologia que transforma a imagem digitalizada de um documento impresso em texto que pode ser editado é o",
          "OCR.",
          ["CAPTCHA.", "firewall.", "backup.", "DNS."],
          "OCR significa reconhecimento óptico de caracteres.", BASE),
    ]),
], semente=0)

# ------------------------------------------------------------------ pacote de escritório
escrever("u-info-office", "Microsoft 365 e LibreOffice: texto, planilhas e apresentações", "Gerais", "info",
         ["info-03", "info-04"], [
    L("ioff-l1", "Editores de texto: Word e Writer", 7, [
        "Estilos de título permitem criar sumário automático e navegar pelo documento. Formatar à mão não gera sumário automático.",
        "Controle de alterações (aba Revisão) registra as edições e permite aceitar ou rejeitar. Comentários servem para observações sem alterar o texto.",
        "Mala direta combina um documento-modelo com uma lista de dados (nomes, endereços) para gerar cartas ou etiquetas personalizadas.",
        "O Word salva por padrão em .docx, e o Writer, em .odt. Ambos exportam para PDF. Cabeçalhos e rodapés repetem informações nas páginas. Quebras de seção permitem formatações diferentes no mesmo documento."
    ], [
        ("Para que servem os estilos de título?", "Padronizam a formatação e permitem gerar sumário automático."),
        ("Controle de alterações", "Registra as edições para que outras pessoas aceitem ou rejeitem."),
        ("Formato padrão do Writer", ".odt (OpenDocument Text).")
    ], [
        Q("Para gerar um sumário automático em um documento do Word ou do Writer, o usuário deve aplicar aos títulos",
          "estilos de título.",
          ["negrito e sublinhado manualmente.", "fonte maior que o corpo do texto.", "cores diferentes em cada título.", "quebras de página antes de cada título."],
          "O sumário automático é montado a partir dos estilos de título aplicados no documento.", BASE),
        Q("O recurso que registra as modificações feitas por revisores e permite aceitá-las ou rejeitá-las é o",
          "controle de alterações.",
          ["verificador ortográfico.", "mala direta.", "quebra de seção.", "tabela dinâmica."],
          "O controle de alterações mostra o que foi inserido, excluído ou formatado, e quem fez.", BASE),
        Q("Para enviar uma carta com o mesmo conteúdo, mas com nome e endereço diferentes para cada destinatário, usa-se",
          "a mala direta.",
          ["o controle de alterações.", "o sumário automático.", "a proteção de documento.", "a quebra de página."],
          "A mala direta mescla um modelo com uma fonte de dados.", BASE),
        Q("O formato de arquivo padrão do aplicativo Writer, do LibreOffice, é",
          ".odt.",
          [".docx.", ".ods.", ".xlsx.", ".pdf."],
          "O Writer usa o formato OpenDocument Text (.odt). O .docx é o padrão do Word.", BASE),
    ]),
    L("ioff-l2", "Planilhas e apresentações: Excel, Calc, PowerPoint e Impress", 8, [
        "Fórmulas começam com o sinal de igual. Em português do Brasil, os argumentos das funções são separados por ponto e vírgula: =SOMA(A1:A3), =MÉDIA(B1:B4), =SE(B2>=7;\"Aprovado\";\"Reprovado\").",
        "Referência relativa (A1) muda ao copiar a fórmula. Absoluta ($A$1) não muda. Mista (A$1 ou $A1) fixa só a linha ou a coluna.",
        "Outras funções: MÁXIMO, MÍNIMO, CONT.SE, SOMASE e PROCV (procura vertical). Planilhas usam .xlsx (Excel) e .ods (Calc).",
        "Apresentações: o slide mestre define o padrão visual. Transições são efeitos entre slides, e animações atuam sobre objetos. F5 inicia a apresentação do primeiro slide, e Shift+F5, do slide atual. Formatos: .pptx e .odp."
    ], [
        ("Referência absoluta", "$A$1: não muda quando a fórmula é copiada."),
        ("Função SE", "Testa uma condição e retorna um valor se verdadeira e outro se falsa: =SE(teste;se_verdadeiro;se_falso)."),
        ("Iniciar apresentação do início", "F5. Shift+F5 inicia a partir do slide atual.")
    ], [
        Q("Se as células A1, A2 e A3 contêm os valores 2, 3 e 5, o resultado da fórmula =SOMA(A1:A3) é",
          "10",
          ["5", "8", "15", "30"],
          "A função soma os valores do intervalo: 2 + 3 + 5 = 10.", BASE),
        Q("Se a célula B2 contém 6,5, o resultado da fórmula =SE(B2>=7;\"Aprovado\";\"Reprovado\") é",
          "Reprovado",
          ["Aprovado", "7", "6,5", "#VALOR!"],
          "A condição B2>=7 é falsa, então a função retorna o terceiro argumento.", BASE),
        Q("Ao copiar uma fórmula que contém a referência $A$1 para outra célula, essa referência",
          "permanece a mesma, pois é absoluta.",
          ["muda para a célula vizinha.", "muda apenas a coluna.", "muda apenas a linha.", "gera um erro de referência."],
          "O cifrão fixa coluna e linha, tornando a referência absoluta.", BASE),
        Q("Em PowerPoint e em Impress, a tecla que inicia a apresentação a partir do primeiro slide é",
          "F5.",
          ["F2.", "F7.", "F11.", "F12."],
          "F5 inicia a apresentação do começo. Shift+F5 inicia a partir do slide selecionado.", BASE),
    ]),
], semente=1)

# ------------------------------------------------------------------ internet, e-mail, nuvem
escrever("u-info-internet", "Internet, correio eletrônico e computação em nuvem", "Gerais", "info",
         ["info-05", "info-06", "info-08"], [
    L("inet-l1", "Internet, intranet, navegadores e busca", 7, [
        "Internet é a rede mundial de computadores. Intranet é uma rede privada que usa as mesmas tecnologias, restrita à organização. Extranet libera parte da intranet a parceiros.",
        "HTTPS é o HTTP com criptografia, e o cadeado do navegador indica conexão segura (não garante que o site seja confiável). O DNS traduz nomes de sites em endereços IP.",
        "Cookies guardam informações de navegação. A janela anônima ou privada não grava histórico, cookies e dados de formulários no aparelho ao ser fechada, mas não impede que o site ou o provedor registrem o acesso.",
        "Operadores de busca: aspas buscam a frase exata, o sinal de menos exclui um termo, site: restringe a um domínio e filetype: restringe a um tipo de arquivo."
    ], [
        ("Intranet", "Rede privada de uma organização, que usa as tecnologias da internet."),
        ("O que faz o DNS?", "Traduz nomes de domínio em endereços IP."),
        ("Operador site:", "Restringe a busca a um domínio, por exemplo: site:abdi.com.br relatório.")
    ], [
        Q("Uma rede interna de uma organização, que usa as tecnologias da internet, mas é acessível apenas aos seus empregados, é chamada de",
          "intranet.",
          ["extranet pública.", "darknet.", "rede mundial.", "blockchain."],
          "Intranet é a rede privada corporativa. A extranet abre parte dela a parceiros.", BASE),
        Q("O serviço que traduz nomes de domínio (como www.exemplo.com.br) em endereços IP é o",
          "DNS.",
          ["DHCP.", "SMTP.", "FTP.", "VPN."],
          "O DNS (Domain Name System) faz a resolução de nomes em endereços.", BASE),
        Q("Sobre a navegação em janela anônima de um navegador, é correto afirmar que ela",
          "não guarda histórico e cookies no aparelho ao ser encerrada, mas não impede o registro do acesso pelo site ou pelo provedor.",
          ["torna o usuário totalmente invisível na internet.", "impede que o provedor de internet saiba os sites visitados.", "protege o computador contra qualquer vírus.", "criptografa todos os dados transmitidos."],
          "O modo anônimo evita que o navegador salve dados locais, mas não esconde a navegação de sites, provedores ou administradores de rede.", BASE),
        Q("Para restringir uma busca aos resultados de um domínio específico, usa-se o operador",
          "site:",
          ["filetype:", "intitle:", "related:", "cache:"],
          "O operador site: limita os resultados ao domínio informado. O filetype: limita ao tipo de arquivo.", BASE),
    ]),
    L("inet-l2", "Correio eletrônico", 7, [
        "Campos do e-mail: Para (destinatários principais), Cc (cópia visível a todos) e Cco (cópia oculta: os demais destinatários não veem quem está em Cco).",
        "Protocolos: SMTP envia mensagens. POP3 baixa as mensagens para o computador. IMAP mantém as mensagens no servidor e sincroniza entre dispositivos.",
        "Responder a todos envia a resposta ao remetente e aos demais destinatários dos campos Para e Cc. Quem está em Cco não é alcançado.",
        "Anexos aumentam o tamanho da mensagem e são via comum de golpes. Calendários e contatos fazem parte dos clientes de e-mail, como o Outlook."
    ], [
        ("Cc x Cco", "Cc: cópia visível a todos. Cco: cópia oculta, ninguém vê os destinatários em Cco."),
        ("SMTP, POP3 e IMAP", "SMTP envia. POP3 e IMAP recebem; o IMAP mantém as mensagens no servidor e sincroniza."),
        ("Anexos de origem desconhecida", "São risco de segurança; não devem ser abertos sem verificação.")
    ], [
        Q("Ao enviar uma mensagem com vários destinatários, o campo que permite ocultar do restante dos destinatários quem recebeu a cópia é o",
          "Cco.",
          ["Cc.", "Para.", "Assunto.", "Responder a todos."],
          "Cco (cópia oculta) não é mostrado aos demais destinatários.", BASE),
        Q("O protocolo utilizado principalmente para o envio de mensagens de correio eletrônico é o",
          "SMTP.",
          ["IMAP.", "POP3.", "HTTP.", "DNS."],
          "O SMTP envia. IMAP e POP3 são usados para acessar mensagens recebidas.", BASE),
        Q("Entre os protocolos de recebimento de e-mail, o que mantém as mensagens no servidor e as sincroniza entre diversos dispositivos é o",
          "IMAP.",
          ["SMTP.", "POP3, sempre.", "FTP.", "SNMP."],
          "O IMAP trabalha com a caixa de correio no servidor. O POP3 tipicamente baixa as mensagens para um único dispositivo.", BASE),
        Q("Maria recebeu uma mensagem em que o remetente colocou Ana no campo Para, Carlos em Cc e Paula em Cco. Se Maria (que estava em Para) usar \"Responder a todos\", a resposta será enviada a",
          "o remetente, Ana e Carlos, mas não a Paula.",
          ["apenas o remetente.", "o remetente, Ana, Carlos e Paula.", "apenas Ana e Carlos.", "apenas Paula."],
          "Responder a todos atinge o remetente e os demais destinatários visíveis nos campos Para e Cc. Quem está em Cco não aparece para Maria.", BASE),
    ]),
    L("inet-l3", "Computação em nuvem", 7, [
        "Segundo o NIST, a nuvem tem cinco características: autoatendimento sob demanda, amplo acesso por rede, agrupamento de recursos, elasticidade rápida e serviço medido.",
        "Modelos de serviço: IaaS (infraestrutura: máquinas virtuais, armazenamento, rede), PaaS (plataforma para desenvolver e executar aplicações) e SaaS (software pronto, usado pelo navegador, como e-mail e editores online).",
        "Modelos de implantação: nuvem pública, privada, comunitária e híbrida (combinação de duas ou mais).",
        "Sincronização mantém arquivos iguais em vários dispositivos, e a colaboração permite editar o mesmo documento ao mesmo tempo. Armazenar na nuvem não substitui uma política de backup."
    ], [
        ("IaaS, PaaS, SaaS", "Infraestrutura, plataforma e software como serviço."),
        ("Elasticidade", "Capacidade de aumentar ou reduzir recursos rapidamente conforme a demanda."),
        ("Nuvem híbrida", "Combinação de nuvem pública e privada (ou mais de um modelo).")
    ], [
        Q("Um editor de texto e planilhas usado diretamente no navegador, sem instalação, ilustra o modelo de serviço de nuvem",
          "SaaS.",
          ["IaaS.", "PaaS.", "DaaS apenas para hardware.", "nenhum, pois exige instalação local."],
          "SaaS entrega o software pronto como serviço.", NIST),
        Q("Quando uma organização contrata máquinas virtuais, armazenamento e redes de um provedor, sem comprar servidores físicos, ela utiliza o modelo",
          "IaaS.",
          ["SaaS.", "PaaS.", "intranet.", "extranet."],
          "IaaS oferece infraestrutura de computação como serviço.", NIST),
        Q("A capacidade de a nuvem aumentar ou reduzir rapidamente os recursos contratados conforme a demanda é chamada de",
          "elasticidade.",
          ["persistência.", "criptografia.", "latência.", "redundância apenas."],
          "A elasticidade rápida é uma das características essenciais da computação em nuvem.", NIST),
        Q("Uma nuvem que combina recursos de nuvem pública e de nuvem privada é chamada de",
          "nuvem híbrida.",
          ["nuvem comunitária.", "nuvem exclusiva.", "rede privada virtual.", "intranet."],
          "A nuvem híbrida integra dois ou mais modelos de implantação.", NIST),
    ]),
], semente=2)

# ------------------------------------------------------------------ segurança e IA
escrever("u-info-seguranca-ia", "Segurança da informação e inteligência artificial", "Gerais", "info", ["info-07", "info-09"], [
    L("iseg-l1", "Segurança da informação", 8, [
        "Princípios: confidencialidade (só acessa quem pode), integridade (dados não alterados indevidamente) e disponibilidade (acesso quando necessário). Também se citam autenticidade e não repúdio.",
        "Malwares: vírus (depende da execução de um hospedeiro), worm (se replica sozinho pela rede), cavalo de troia (disfarçado de programa legítimo), ransomware (criptografa os dados e exige resgate), spyware e keylogger (espionam), backdoor (acesso oculto).",
        "Phishing é engenharia social: mensagens falsas que imitam instituições para obter dados ou instalar códigos maliciosos.",
        "Defesas: antivírus, firewall (filtra o tráfego de rede), atualizações, senhas fortes, autenticação multifator e backup. A regra 3-2-1 manda manter 3 cópias, em 2 tipos de mídia, com 1 cópia fora do local."
    ], [
        ("Tríade da segurança", "Confidencialidade, integridade e disponibilidade."),
        ("Ransomware", "Criptografa os dados da vítima e exige pagamento para liberá-los."),
        ("Regra 3-2-1 de backup", "3 cópias, 2 tipos de mídia, 1 cópia fora do local.")
    ], [
        Q("O código malicioso que criptografa os arquivos do usuário e exige pagamento de resgate para liberá-los é chamado de",
          "ransomware.",
          ["spyware.", "adware.", "worm.", "bootloader."],
          "O ransomware sequestra os dados por criptografia.", SEG),
        Q("Garantir que as informações não sejam alteradas de forma indevida corresponde ao princípio da",
          "integridade.",
          ["confidencialidade.", "disponibilidade.", "obsolescência.", "redundância."],
          "A integridade assegura a exatidão e a completude dos dados.", SEG),
        Q("Uma mensagem que imita um banco e pede que o usuário clique em um link para \"atualizar seus dados\" é um exemplo típico de",
          "phishing.",
          ["backup.", "firewall.", "criptografia simétrica.", "compactação."],
          "Phishing usa engenharia social e mensagens falsas para roubar dados.", SEG),
        Q("A estratégia de backup conhecida como 3-2-1 recomenda manter",
          "3 cópias dos dados, em 2 tipos de mídia, com 1 cópia fora do local.",
          ["3 cópias no mesmo disco, em 2 pastas e 1 arquivo.", "2 cópias na nuvem e 1 no computador de uso diário.", "1 cópia em 2 locais e 3 mídias iguais.", "3 cópias no mesmo local, em 2 computadores e 1 nuvem."],
          "A regra combina quantidade, diversidade de mídia e uma cópia em local distinto, para resistir a falhas e desastres.", SEG),
    ]),
    L("iseg-l2", "Inteligência artificial no ambiente de trabalho", 8, [
        "IA generativa cria conteúdo novo (texto, imagem, áudio, código) a partir de padrões aprendidos em grandes volumes de dados. Os modelos de linguagem são um exemplo.",
        "Limitações: podem gerar \"alucinações\" (respostas plausíveis, mas falsas), reproduzir vieses dos dados de treinamento e não ter acesso a informações recentes.",
        "Uso responsável: revisar e verificar o resultado, citar fontes, respeitar direitos autorais e não inserir dados pessoais ou sigilosos em ferramentas não autorizadas, em respeito à LGPD.",
        "Um bom pedido (prompt) traz contexto, objetivo, público, formato esperado e restrições. Resultados dependem da qualidade das instruções."
    ], [
        ("O que são alucinações da IA?", "Respostas plausíveis, mas incorretas ou inventadas."),
        ("Cuidado com dados em ferramentas de IA", "Não inserir dados pessoais ou sigilosos em ferramentas sem autorização; aplica-se a LGPD."),
        ("Boas práticas de prompt", "Informar contexto, objetivo, público, formato e restrições.")
    ], [
        Q("Chama-se \"alucinação\", no contexto da IA generativa, o fenômeno em que o sistema",
          "produz respostas plausíveis, mas incorretas ou inventadas.",
          ["deixa de funcionar por falta de energia.", "apaga os dados de treinamento.", "cobra automaticamente pelo uso.", "bloqueia o acesso do usuário."],
          "A alucinação é uma limitação comum: o modelo gera conteúdo convincente sem base factual.", BASE),
        Q("Um servidor pretende usar uma ferramenta pública de IA generativa para resumir um documento que contém dados pessoais sensíveis de cidadãos. A conduta mais adequada é",
          "não inserir os dados na ferramenta sem autorização institucional e sem respaldo na LGPD.",
          ["inserir, pois a ferramenta é gratuita.", "inserir apenas o nome dos cidadãos.", "inserir e depois apagar o histórico.", "inserir, desde que o texto esteja em português."],
          "O uso de dados pessoais por terceiros exige base legal e controle institucional. A gratuidade ou o idioma não alteram essa exigência.", LGPD),
        Q("Entre os pedidos abaixo a uma ferramenta de IA generativa, o que tende a produzir resultado mais útil é",
          "\"Elabore um resumo de 5 linhas, em tom formal, para o público interno, sobre as mudanças do regulamento, com base no texto abaixo.\"",
          ["\"Escreva alguma coisa.\"", "\"Resumo.\"", "\"Faça melhor.\"", "\"Texto sobre o regulamento.\""],
          "O pedido informa tamanho, tom, público, finalidade e fonte, o que orienta a resposta.", BASE),
        Q("A característica que distingue a IA generativa de um sistema que apenas classifica dados é que ela",
          "gera conteúdo novo a partir dos padrões aprendidos.",
          ["só funciona sem conexão à internet.", "dispensa qualquer treinamento.", "nunca comete erros.", "só trabalha com números."],
          "Em vez de apenas classificar ou prever, a IA generativa cria textos, imagens e outros conteúdos.", BASE),
    ]),
], semente=3)

# ------------------------------------------------------------------ legislação (item 11 do Anexo II)
escrever("u-info-legislacao", "Legislação: LAI, delitos informáticos, Marco Civil e LGPD", "Gerais", "info", ["info-11"], [
    L("ileg-l1", "Lei de Acesso à Informação (Lei 12.527/2011)", 9, [
        "Art. 3º: a publicidade é a regra e o sigilo, a exceção. Os órgãos divulgam informações de interesse público independentemente de solicitações (transparência ativa) e fomentam a cultura de transparência e o controle social.",
        "Art. 2º: aplica-se, no que couber, a entidades privadas sem fins lucrativos que recebam recursos públicos por contrato de gestão, convênios e instrumentos congêneres. A publicidade refere-se à parcela dos recursos públicos recebidos e à sua destinação (parágrafo único).",
        "Art. 8º: divulgação mínima em local de fácil acesso: competências e estrutura, repasses, despesas, licitações e contratos, dados de programas e respostas a perguntas frequentes.",
        "Arts. 10 e 11: qualquer interessado pode pedir informação, com identificação e especificação do pedido, e não se podem exigir os motivos. O acesso é imediato se a informação estiver disponível. Caso contrário, o prazo é de até 20 dias, prorrogável por mais 10 dias, com justificativa.",
        "Art. 24: classificação do sigilo: ultrassecreta (25 anos), secreta (15 anos) e reservada (5 anos). Art. 31: informações pessoais têm acesso restrito por até 100 anos, independentemente de classificação."
    ], [
        ("Regra geral da LAI", "Publicidade como regra e sigilo como exceção (art. 3º, I)."),
        ("Prazo de resposta a pedido de informação", "Imediato, se disponível. Senão, até 20 dias, prorrogável por mais 10 com justificativa (art. 11, §§ 1º e 2º)."),
        ("Prazos máximos de sigilo", "Ultrassecreta: 25 anos. Secreta: 15 anos. Reservada: 5 anos (art. 24, § 1º).")
    ], [
        Q("Segundo a Lei de Acesso à Informação, o prazo para o órgão responder a um pedido de acesso, quando não é possível conceder o acesso imediato, é de até",
          "20 dias, prorrogável por mais 10 dias, mediante justificativa expressa.",
          ["5 dias úteis, sem possibilidade de prorrogação.", "10 dias, prorrogável por mais 20.", "30 dias corridos, improrrogáveis.", "60 dias, prorrogável por mais 30."],
          "O art. 11, § 1º, fixa o prazo de 20 dias e o § 2º permite prorrogação por mais 10 dias, com justificativa expressa.", LAI),
        Q("Os prazos máximos de restrição de acesso à informação classificada como ultrassecreta, secreta e reservada são, respectivamente,",
          "25, 15 e 5 anos.",
          ["15, 10 e 5 anos.", "30, 20 e 10 anos.", "50, 25 e 10 anos.", "25, 20 e 10 anos."],
          "O art. 24, § 1º, estabelece 25 anos (ultrassecreta), 15 (secreta) e 5 (reservada).", LAI),
        Q("De acordo com a Lei 12.527/2011, ao apresentar um pedido de acesso a informações de interesse público, o requerente",
          "não pode ser obrigado a informar os motivos da solicitação.",
          ["deve justificar o interesse por escrito.", "deve comprovar vínculo com o órgão.", "só pode pedir se for pesquisador.", "deve pagar taxa de análise em todos os casos."],
          "O art. 10, § 3º, veda exigências relativas aos motivos determinantes da solicitação de informações de interesse público.", LAI),
        Q("A Lei de Acesso à Informação se aplica, no que couber, a entidades privadas sem fins lucrativos que recebam recursos públicos por meio, por exemplo, de",
          "contrato de gestão ou convênios, com publicidade relativa à parcela de recursos recebida e à sua destinação.",
          ["qualquer doação privada, em qualquer valor.", "empréstimos bancários comuns, apenas.", "contratos de trabalho de seus empregados.", "tributos pagos pela entidade."],
          "O art. 2º inclui entidades privadas sem fins lucrativos que recebam recursos públicos por contrato de gestão, convênios e instrumentos congêneres. O parágrafo único limita a publicidade à parcela dos recursos públicos e à sua destinação.", LAI),
    ]),
    L("ileg-l2", "Delitos informáticos (Lei 12.737/2012) e Marco Civil da Internet (Lei 12.965/2014)", 9, [
        "Lei 12.737/2012: acrescentou ao Código Penal o art. 154-A (invasão de dispositivo informático). Na redação atual, dada pela Lei 14.155/2021, o crime é invadir dispositivo informático de uso alheio, conectado ou não à rede, com o fim de obter, adulterar ou destruir dados ou informações sem autorização expressa ou tácita do usuário, ou de instalar vulnerabilidades para obter vantagem ilícita. Pena: reclusão de 1 a 4 anos e multa. O texto original de 2012 exigia violação de mecanismo de segurança; isso não consta mais.",
        "Mesma pena para quem produz, oferece, distribui, vende ou difunde programa para permitir a invasão (§ 1º). A pena aumenta de 1/3 a 2/3 se há prejuízo econômico (§ 2º). É qualificado, com reclusão de 2 a 5 anos e multa, se a invasão obtém conteúdo de comunicações privadas, segredos comerciais ou industriais, informações sigilosas ou permite controle remoto não autorizado (§ 3º). Aumenta-se a pena se há divulgação a terceiros (§ 4º).",
        "Marco Civil (Lei 12.965/2014), art. 3º: princípios como liberdade de expressão, proteção da privacidade, proteção dos dados pessoais, neutralidade de rede e responsabilização dos agentes.",
        "Registros: o provedor de conexão guarda os registros de conexão por 1 ano, em sigilo (art. 13). É vedado ao provedor de conexão guardar registros de acesso a aplicações (art. 14). O provedor de aplicações que seja pessoa jurídica com fins econômicos guarda os registros de acesso por 6 meses (art. 15).",
        "Responsabilidade: o provedor de conexão não responde por conteúdo de terceiros (art. 18). O art. 19 condicionava a responsabilidade do provedor de aplicações ao descumprimento de ordem judicial específica. Em 26/06/2025, o STF decidiu que o art. 19 é parcialmente inconstitucional (RE 1.037.396, Tema 987, e RE 1.057.258, Tema 533). Cenas de nudez ou de atos sexuais privados divulgadas sem autorização geram responsabilidade subsidiária após notificação do participante (art. 21).",
        "Tese do STF, conforme a cobertura do julgamento: até que haja nova lei, o provedor responde civilmente, nos termos do art. 21 (notificação), por danos de conteúdo de terceiros em casos de crime ou atos ilícitos, sem prejuízo do dever de remoção, e a mesma regra vale para contas denunciadas como inautênticas. Para crimes graves (como atos antidemocráticos, terrorismo, induzimento ao suicídio, incitação à discriminação, crimes graves contra crianças e adolescentes e tráfico de pessoas), responde se não promover a indisponibilização imediata. Os provedores devem ter autorregulação (sistema de notificações, devido processo e relatórios anuais de transparência), canais de atendimento e sede e representante no Brasil. A decisão é prospectiva. Oito ministros viram o art. 19 como parcial ou totalmente inconstitucional, e três votaram pela sua validade."
    ], [
        ("Art. 154-A do Código Penal (Lei 12.737, com a Lei 14.155/2021)", "Invadir dispositivo informático de uso alheio, conectado ou não à rede, com o fim de obter, adulterar ou destruir dados ou instalar vulnerabilidades. Reclusão de 1 a 4 anos e multa."),
        ("Guarda de registros no Marco Civil", "Registros de conexão: 1 ano, pelo provedor de conexão. Registros de acesso a aplicações: 6 meses, por provedor de aplicações pessoa jurídica com fins econômicos."),
        ("Art. 19 do Marco Civil e o STF", "Julgado em 26/06/2025: parcialmente inconstitucional. Até nova lei, responsabilização nos termos do art. 21 (notificação) em casos de crime ou ato ilícito, e dever de remoção imediata em crimes graves.")
    ], [
        Q("O art. 154-A do Código Penal, acrescentado pela Lei 12.737/2012 e com a redação atual dada pela Lei 14.155/2021, tipifica a conduta de",
          "invadir dispositivo informático de uso alheio, conectado ou não à rede, com o fim de obter, adulterar ou destruir dados ou informações sem autorização do usuário.",
          ["enviar mensagem eletrônica não solicitada em massa.", "utilizar rede sem fio aberta sem autorização.", "divulgar a própria senha a terceiros.", "usar software sem licença em computador próprio."],
          "A invasão é punida mesmo que o dispositivo não esteja conectado à rede. A redação atual não exige mais a violação indevida de mecanismo de segurança, que constava do texto original de 2012.", CP),
        Q("A pena prevista no caput do art. 154-A do Código Penal (invasão de dispositivo informático), na redação da Lei 14.155/2021, é de",
          "reclusão, de 1 a 4 anos, e multa.",
          ["detenção, de 3 meses a 1 ano, e multa.", "reclusão, de 2 a 5 anos, e multa.", "detenção, de 6 meses a 2 anos, apenas.", "multa, sem pena privativa de liberdade."],
          "O caput prevê reclusão de 1 a 4 anos e multa. A detenção de 3 meses a 1 ano era a pena do texto original de 2012, e a reclusão de 2 a 5 anos é a do § 3º (forma qualificada).", CP),
        Q("De acordo com o Marco Civil da Internet, o provedor de conexão deve manter os registros de conexão, sob sigilo, em ambiente controlado e de segurança, pelo prazo de",
          "1 ano.",
          ["6 meses.", "2 anos.", "5 anos.", "90 dias."],
          "O art. 13 fixa 1 ano para os registros de conexão. Os 6 meses do art. 15 se referem aos registros de acesso a aplicações de internet.", MCI),
        Q("Pelo art. 14 do Marco Civil da Internet, na provisão de conexão, onerosa ou gratuita, é vedado ao provedor",
          "guardar os registros de acesso a aplicações de internet.",
          ["guardar os registros de conexão.", "cobrar pela conexão.", "informar o usuário sobre o regime de proteção dos registros.", "cumprir ordem judicial."],
          "O provedor de conexão guarda os registros de conexão (art. 13), mas não os de acesso a aplicações (art. 14).", MCI),
        Q("Em junho de 2025, o Supremo Tribunal Federal julgou o art. 19 do Marco Civil da Internet (que condicionava a responsabilidade civil do provedor de aplicações ao descumprimento de ordem judicial específica) e decidiu que esse dispositivo é",
          "parcialmente inconstitucional.",
          ["totalmente constitucional, sem ressalvas.", "totalmente inconstitucional e revogado desde 2014.", "constitucional, mas aplicável apenas a provedores de conexão.", "inaplicável a conteúdos ilícitos de qualquer natureza."],
          "O STF, em 26/06/2025, nos RE 1.037.396 (Tema 987) e RE 1.057.258 (Tema 533), declarou a inconstitucionalidade parcial do art. 19. O texto oficial da tese não foi conferido; o conteúdo exato das hipóteses de responsabilização deve ser estudado na decisão.", "STF, RE 1.037.396 (Tema 987) e RE 1.057.258 (Tema 533), julgamento de 26/06/2025, conforme resumos de machadomeyer.com.br e bmalaw.com.br; texto oficial da tese não conferido"),
        Q("Segundo a tese fixada pelo STF em 26/06/2025 sobre o art. 19 do Marco Civil da Internet, conforme noticiada, até que haja nova legislação o provedor de aplicações responde civilmente, nos termos do art. 21, por danos decorrentes de conteúdo de terceiros em casos de",
          "crime ou atos ilícitos, sem prejuízo do dever de remoção do conteúdo.",
          ["qualquer opinião crítica a autoridades, sem exceção.", "descumprimento de ordem judicial específica, em todas as hipóteses, como antes.", "conteúdo de natureza exclusivamente política, apenas.", "nenhuma hipótese, pois o art. 19 permaneceu integralmente em vigor."],
          "A tese deslocou o regime geral para a responsabilização nos termos do art. 21 (notificação), em casos de crime ou ato ilícito. A exigência de ordem judicial, que era a regra do art. 19, deixou de ser a única via.", "STF, RE 1.037.396 (Tema 987) e RE 1.057.258 (Tema 533), tese lida em 26/06/2025, conforme Conjur (conjur.com.br, 26/06/2025); o texto oficial do acórdão não foi conferido"),
        Q("A tese do STF sobre o art. 19 do Marco Civil determinou que os provedores de aplicações editem autorregulação que abranja, necessariamente,",
          "sistema de notificações, devido processo e relatórios anuais de transparência sobre notificações extrajudiciais, anúncios e impulsionamentos.",
          ["cobrança de taxa dos usuários e relatórios mensais de lucro.", "nomeação de um ministro como fiscal de cada plataforma.", "exclusão automática de qualquer conteúdo crítico.", "dispensa de sede e de representante no Brasil."],
          "Segundo a cobertura do julgamento, a tese exige autorregulação com essas três partes, canais de atendimento acessíveis e sede e representante no país.", "STF, RE 1.037.396 (Tema 987) e RE 1.057.258 (Tema 533), tese lida em 26/06/2025, conforme Conjur (conjur.com.br, 26/06/2025); o texto oficial do acórdão não foi conferido"),
    ]),
    L("ileg-l3", "Lei Geral de Proteção de Dados (Lei 13.709/2018)", 10, [
        "Art. 2º: fundamentos incluem respeito à privacidade, autodeterminação informativa, liberdade de expressão, inviolabilidade da intimidade, honra e imagem, desenvolvimento econômico e tecnológico, livre iniciativa e direitos humanos.",
        "Art. 5º: dado pessoal é informação relacionada a pessoa natural identificada ou identificável. Dado pessoal sensível trata de origem racial ou étnica, convicção religiosa, opinião política, filiação sindical, saúde, vida sexual, dado genético ou biométrico. Titular é a pessoa a quem os dados se referem. Controlador decide sobre o tratamento. Operador trata os dados em nome do controlador. Encarregado é o canal de comunicação entre controlador, titulares e a ANPD.",
        "Art. 6º: boa-fé e princípios de finalidade, adequação, necessidade, livre acesso, qualidade dos dados, transparência, segurança, prevenção, não discriminação e responsabilização e prestação de contas.",
        "Art. 7º: o tratamento só pode ocorrer nas hipóteses legais, como consentimento do titular, cumprimento de obrigação legal, execução de políticas públicas pela administração, estudos por órgão de pesquisa, execução de contrato e exercício regular de direitos em processos.",
        "Art. 18: direitos do titular, como confirmação do tratamento, acesso, correção, anonimização, bloqueio ou eliminação de dados desnecessários, portabilidade e eliminação dos dados tratados com consentimento. Art. 41: o controlador indica um encarregado e divulga publicamente sua identidade e contato. Art. 52: sanções incluem advertência, multa simples de até 2% do faturamento, limitada a R$ 50 milhões por infração, e multa diária.",
        "Atenção a mudanças recentes: a Lei 15.352, de 25/02/2026 (conversão da MP 1.317/2025), alterou o art. 55-A. A ANPD passou a ser a Agência Nacional de Proteção de Dados, autarquia de natureza especial vinculada ao Ministério da Justiça e Segurança Pública, com autonomia funcional, técnica, decisória, administrativa e financeira. A redação original a descrevia como órgão da Presidência da República e usava o nome Autoridade Nacional."
    ], [
        ("Dado pessoal x dado pessoal sensível", "Pessoal: informação sobre pessoa identificada ou identificável. Sensível: origem racial ou étnica, religião, opinião política, filiação sindical, saúde, vida sexual, dado genético ou biométrico."),
        ("Controlador, operador e encarregado", "Controlador decide sobre o tratamento. Operador trata em nome do controlador. Encarregado é o canal com titulares e ANPD."),
        ("Teto da multa simples da LGPD (art. 52, II)", "Até 2% do faturamento da pessoa jurídica no Brasil, limitada a R$ 50 milhões por infração."),
        ("Princípios do art. 6º", "Finalidade, adequação, necessidade, livre acesso, qualidade dos dados, transparência, segurança, prevenção, não discriminação e responsabilização e prestação de contas.")
    ], [
        Q("Segundo a LGPD, o dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política ou saúde, quando vinculado a uma pessoa natural, é classificado como",
          "dado pessoal sensível.",
          ["dado anonimizado.", "dado público.", "dado estatístico.", "banco de dados."],
          "O art. 5º, II, define dado pessoal sensível e lista essas categorias, entre outras.", LGPD),
        Q("Na LGPD, a pessoa natural ou jurídica, de direito público ou privado, a quem competem as decisões referentes ao tratamento de dados pessoais é o",
          "controlador.",
          ["operador.", "titular.", "encarregado.", "usuário final."],
          "O art. 5º, VI, define o controlador. O operador trata dados em nome do controlador, e o titular é a pessoa a quem os dados se referem.", LGPD),
        Q("O princípio da LGPD que exige que o tratamento seja limitado ao mínimo necessário para a realização de suas finalidades é o da",
          "necessidade.",
          ["finalidade.", "livre acesso.", "transparência.", "qualidade dos dados."],
          "O art. 6º, III, define a necessidade como a limitação do tratamento ao mínimo necessário, com dados pertinentes, proporcionais e não excessivos.", LGPD),
        Q("De acordo com o art. 52 da LGPD, a multa simples aplicável aos agentes de tratamento é de até",
          "2% do faturamento da pessoa jurídica no Brasil no último exercício, limitada a R$ 50 milhões por infração.",
          ["10% do faturamento global, sem limite.", "R$ 5 milhões por titular afetado.", "5% do patrimônio líquido, limitada a R$ 1 milhão.", "1% do faturamento, limitada a R$ 100 milhões."],
          "O art. 52, II, prevê multa simples de até 2% do faturamento, excluídos os tributos, limitada a R$ 50.000.000,00 por infração.", LGPD),
        Q("Na redação do art. 55-A da LGPD dada pela Lei 15.352/2026, a ANPD é",
          "a Agência Nacional de Proteção de Dados, autarquia de natureza especial vinculada ao Ministério da Justiça e Segurança Pública, com autonomia funcional, técnica, decisória, administrativa e financeira.",
          ["órgão integrante da Presidência da República, sem autonomia.", "empresa pública federal com fins lucrativos.", "conselho consultivo vinculado ao Congresso Nacional.", "fundação privada mantida por associações empresariais."],
          "A Lei 15.352/2026, que converteu a MP 1.317/2025, transformou a ANPD em autarquia de natureza especial. A descrição como órgão da Presidência da República era a da redação anterior.", "Lei 15.352/2026, que altera o art. 55-A da Lei 13.709/2018 (planalto.gov.br)"),
    ]),
], semente=4)
