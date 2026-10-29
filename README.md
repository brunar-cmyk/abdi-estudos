# Estudos ABDI 2026

App de estudos no estilo Duolingo para o processo seletivo da ABDI (banca FGV, perfil API - Comunicação e Marketing). Lições curtas, XP, sequência de dias, revisão espaçada, caderno de erros, simulado com cronômetro de 3h30 e painel de progresso. Funciona no computador e no celular, sem login, e o progresso fica salvo no próprio aparelho.

## Como rodar no computador

O Node.js 20 está instalado em `~/.local/node` (não mexi no seu `.zshrc`). Para o terminal enxergar o Node, rode uma vez por janela de terminal:

```bash
export PATH="$HOME/.local/node/bin:$PATH"
```

Se quiser deixar isso permanente, acrescente essa mesma linha ao arquivo `~/.zshrc`.

Depois, dentro da pasta do projeto (`~/Desktop/App.Abdi`):

```bash
npm install      # só na primeira vez
npm run dev
```

O terminal mostra dois endereços. Abra o `Local` (`http://localhost:5173/`) no navegador do computador.

## Como abrir no celular (mesma rede Wi-Fi)

1. Com `npm run dev` rodando, procure no terminal a linha `Network`, por exemplo `http://192.168.0.182:5173/`.
2. Digite esse endereço no navegador do celular, conectado ao mesmo Wi-Fi.
3. Se não abrir, confira se o Mac não está bloqueando conexões de entrada (Ajustes do Sistema, Rede, Firewall).

Atenção: nesse modo o app funciona, mas **não instala nem roda offline no celular**. O modo offline (PWA) exige endereço seguro (HTTPS). Para usar offline no celular, publique o app (próxima seção) e abra o endereço publicado.

O progresso fica salvo por aparelho e por endereço. O que você estuda no computador não aparece no celular sozinho. Para levar de um para o outro, use Ajustes, Exportar JSON e depois Importar JSON no outro aparelho.

## Como publicar de graça

Primeiro gere a versão final:

```bash
npm run build
```

Isso cria a pasta `dist` com o app pronto.

**Vercel (mais simples)**
1. Crie uma conta gratuita em vercel.com e instale a CLI com `npm install -g vercel`, ou use o site arrastando o projeto.
2. Dentro da pasta do projeto, rode `vercel` e aceite as opções padrão. Se o Vercel pedir, use `npm run build` como comando de build e `dist` como pasta de saída.
3. No celular, abra o endereço que o Vercel gerar e use "Adicionar à tela de início". Depois do primeiro acesso, o app abre offline.

**GitHub Pages**
1. Crie um repositório no GitHub e envie o projeto (a pasta `node_modules` já está no `.gitignore`).
2. Em Settings, Pages, escolha publicar a partir de uma branch e aponte para uma branch que contenha o conteúdo da pasta `dist`. O app usa caminhos relativos e funciona em subpasta.
3. Abra o endereço `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/` no celular.

Observação: o conteúdo das lições vai junto no site publicado. Não coloque nada pessoal nos arquivos de `content/`.

## Como o conteúdo é organizado (você edita sem mexer no app)

Tudo fica em `content/`:

| Arquivo | O que é |
| --- | --- |
| `syllabus.json` | 52 tópicos do Anexo II do edital, com texto literal, bloco e peso |
| `dates.json` | datas e prazos do processo |
| `schedule.json` | trilha por semana (Semana 1 como revisão) |
| `units/*.json` | uma unidade por arquivo, com lições, flashcards, questões e pacote de números (29 unidades, 90 lições, 430 questões) |
| `sources.json` | fontes consultadas, com data e versão |
| `pendencias.md` | o que não foi confirmado e não entrou no app |

Cada lição tem de 3 a 6 tópicos de resumo, 2 a 4 flashcards e 4 a 8 questões de 5 alternativas, com uma correta (`correta` é o índice de 0 a 4), explicação e fonte. Dica: não cite letras de alternativas na explicação, porque o app mostra a ordem escrita no JSON.

Para criar uma unidade nova, copie um arquivo de `content/units/`, troque o `id` (o nome do arquivo precisa ser igual ao `id`) e liste o id dela na semana certa em `schedule.json`.

## Como o conteúdo foi gerado

As unidades de `content/units/` foram geradas pelos scripts de `tools/authoring/` (`python3 tools/authoring/port.py`, `rl.py`, `info.py`, `etica.py`, `conv.py`, `lic.py`, `esp1.py`, `esp2.py`). Neles, cada questão é escrita com a alternativa certa em primeiro lugar, e o script embaralha as alternativas de forma equilibrada. Em `rl.py`, as respostas de Raciocínio Lógico são provadas por cálculo antes de gerar o JSON. As unidades de Específicos 1 a 6 e de Institucionais iniciais (Lei, Decreto, Estatuto) foram escritas direto em JSON. Se você editar um JSON à mão, não rode de novo o script daquela unidade, ou ele sobrescreve a sua edição.

## Conferir o conteúdo e rodar os testes

```bash
npm run validate         # confere todo o conteúdo
npm run validate:strict  # também exige que todo tópico do syllabus tenha lição
npm test                 # testes de pontuação, revisão espaçada, sequência, simulado e ações
```

O `validate` confere: 5 alternativas por questão, exatamente 1 correta, explicação e fonte, tamanhos de resumo, flashcards e questões por lição, ids únicos, e a sua regra de estilo (sem travessão, emoji ou seta nos textos). A cobertura de tópicos sem lição aparece como aviso enquanto o conteúdo está sendo escrito, e vira erro no `validate:strict`.

## Como funciona

- **Pontuação do simulado:** 0,3 por questão em Gerais e Institucionais, 0,65 em Específicos, 25 pontos no total. Aprovação com pelo menos 50% de acertos e sem zerar nenhum bloco (edital, item 9.5). Questão em branco vale zero.
- **Revisão espaçada:** algoritmo SM-2. Questão errada vai ao caderno e volta no dia seguinte. Ela sai do caderno depois de 2 acertos seguidos na revisão.
- **XP e sequência:** lição nova rende 10 XP mais 5 por acerto. Um dia conta para a sequência quando o XP do dia atinge a meta (30 por padrão, configurável). O escudo cobre automaticamente um dia perdido por semana (de segunda a domingo).
- **Armazenamento:** IndexedDB, com localStorage como alternativa e aviso na tela se nada puder ser salvo.

## Estrutura do código

```
src/lib      regras (pontuação, SM-2, sequência, armazenamento, simulado)
src/ui       telas (trilha, lição, revisão, simulado, progresso, ajustes)
scripts      validate.mjs
tools        gen_syllabus.py (gera syllabus.json a partir do texto do edital)
```
