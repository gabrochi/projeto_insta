# Projeto Insta Analytics — Automação de Análise de Seguidores

Automação em Python para baixar, organizar e analisar os dados de seguidores/seguindo exportados do Instagram, identificando quem você segue e não te segue de volta (e vice-versa).

## 🎯 O que o projeto faz

O fluxo automatiza o processo, do início ao fim:

1. **Exportação dos dados** (`exportar_info.py`) — navega até o Instagram, acessa a Central de Contas > Suas informações e permissões, configura a exportação (formato JSON, intervalo de datas, filtros) e confirma o pedido de exportação com a senha da conta.
2. **Organização dos arquivos antigos** (`excluir_antigos.py`) — limpa a pasta de destino antes de uma nova exportação, evitando misturar dados de exportações diferentes.
3. **Download e extração** (`deszipar.py`) — localiza o arquivo `.zip` mais recente baixado e extrai o conteúdo para a pasta `jsons/`.
4. **Comparação dos dados** (`comparar_arquivos.py`) — lê os arquivos `followers_1.json` e `following.json`, cruza as listas de usernames e mostra um menu interativo com três opções:
   - Quem você segue e te segue de volta
   - Quem te segue e você não segue de volta
   - Quem você segue e não te segue de volta
5. **Utilitário de apoio** (`posicao.py`) — captura as coordenadas do mouse na tela, usado para descobrir as posições de clique (x, y) ao construir os scripts de automação com PyAutoGUI.

## 🛠️ Tecnologias

- **Python 3**
- **PyAutoGUI** — automação de interface gráfica (cliques, digitação, scroll)
- **json** (biblioteca padrão) — leitura e manipulação dos dados exportados

## 📁 Estrutura esperada

```
projeto_insta/
├── jsons/
│   └── connections/
│       └── followers_and_following/
│           ├── followers_1.json
│           └── following.json
├── exportar_info.py
├── excluir_antigos.py
├── deszipar.py
├── comparar_arquivos.py
├── posicao.py
└── README.md
```

## ▶️ Como usar

1. Execute `excluir_antigos.py` para limpar exportações antigas.
2. Execute `exportar_info.py` para solicitar uma nova exportação de dados no Instagram (isso pode levar horas/dias — o Instagram processa e envia por e-mail/notificação).
3. Depois de baixar o `.zip`, execute `deszipar.py` para extraí-lo automaticamente na pasta correta.
4. Execute `comparar_arquivos.py` e use o menu interativo para ver as comparações.

## ⚠️ Limitações atuais

- Os scripts de automação de tela (`exportar_info.py`, `deszipar.py`, `excluir_antigos.py`) dependem de **coordenadas fixas de clique**, o que os torna frágeis: qualquer mudança de resolução de tela, layout do site, idioma do navegador ou versão do Windows quebra a automação.
- Não há tratamento de erros (ex: se um clique falhar ou uma tela demorar mais que o `time.sleep` previsto).
- A senha da conta está escrita diretamente no código-fonte de `exportar_info.py`, o que é um risco de segurança.

## 🚀 Próximos passos

- [ ] **Substituir a automação de tela por interações mais robustas.** O PyAutoGUI funciona por coordenadas fixas de tela, o que é muito manual e frágil. Vale pesquisar alternativas mais confiáveis, por exemplo:
  - **Playwright** ou **Selenium** para automatizar o navegador via DOM/seletores (em vez de clicar em posições x, y), o que tornaria o `exportar_info.py` muito mais estável.
  - **PyWinAuto** ou bibliotecas de automação nativas do Windows, para interações com o Explorador de Arquivos (`deszipar.py`, `excluir_antigos.py`) baseadas em elementos da interface, não em coordenadas.
  - Verificar se o Instagram oferece alguma **API oficial** (Graph API / Meta for Developers) que permita solicitar exportações de dados sem depender de automação de UI.
- [ ] **Remover senhas do código-fonte.** Usar variáveis de ambiente (`os.environ`) ou um arquivo `.env` (com `python-dotenv`) para armazenar credenciais fora do código.
- [ ] **Adicionar tratamento de erros e esperas dinâmicas** (ex: `WebDriverWait` do Selenium) em vez de `time.sleep` fixo, para tornar os scripts resilientes a variações de tempo de carregamento.
- [ ] **Automatizar o fluxo completo**, unindo os scripts em um único orquestrador (ex: `main.py`) que executa a limpeza, exportação, extração e análise em sequência.
- [ ] **Gerar relatórios visuais** (gráficos, exportação para Excel/CSV) além do menu de texto no terminal.
- [ ] **Detectar automaticamente** o arquivo `.zip` mais recente por data de modificação, em vez de depender de ordenação manual da tela.

## 📌 Observação

Este projeto foi feito para uso pessoal com fins de estudo/análise dos próprios dados do Instagram. Automatizar a extração de dados de terceiros ou o uso das credenciais de outras pessoas pode violar os Termos de Uso do Instagram.
