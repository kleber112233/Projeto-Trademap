# Projeto-Trademap

Este projeto foi desenvolvido para extrair dados de uma tabela disponibilizada em um site, onde os dados podem ser filtrados por critérios específicos, como países, grupos de países e produtos. A solução permite ao usuário selecionar filtros personalizados diretamente pelo terminal, gerando URLs com os parâmetros escolhidos, acessando o site, extraindo os dados da tabela e formatando-os para exportação em formatos compatíveis para análise.

## Objetivo do Projeto

O objetivo principal deste projeto é facilitar a coleta de dados filtrados de forma automatizada, sem a necessidade de interação manual no navegador para aplicar cada filtro. Com essa solução, o usuário pode especificar os critérios de filtragem desejados, obtendo uma tabela completa e estruturada para análise.

## Funcionalidades

- **Seleção de Filtros pelo Terminal**: O usuário pode escolher países, grupos de países e produtos através de uma interface no terminal.
- **Geração Dinâmica de URLs**: A URL é modificada automaticamente com base nos filtros selecionados, simulando a aplicação de filtros diretamente no site.
- **Extração e Formatação de Dados**: A tabela é extraída como HTML e, em seguida, formatada para facilitar o armazenamento e a visualização.
- **Exportação para CSV e HTML**: Os dados extraídos são salvos em um arquivo CSV, que pode ser facilmente utilizado para análises adicionais em ferramentas externas, além de uma visualização em HTML.

## Ferramentas Utilizadas

- **Python**: Linguagem principal utilizada para a automação e manipulação de dados.
- **Selenium**: Usado para acessar o site, aplicar os filtros e extrair o conteúdo da tabela.
- **BeautifulSoup**: Empregado para processar o HTML da tabela extraída e organizá-lo em um formato estruturado.
- **Pandas**: Biblioteca utilizada para organizar a tabela extraída em um `DataFrame`, facilitando a exportação para CSV.

## Estrutura do Projeto

1. **Interface de Seleção de Filtros**:
   - O usuário interage pelo terminal para selecionar países, grupos de países e produtos.
   - As escolhas são feitas de forma interativa, com o código validando as entradas para evitar erros.

2. **Geração de URL com Parâmetros**:
   - A URL do site é modificada automaticamente de acordo com os filtros escolhidos, economizando tempo ao evitar cliques manuais.

3. **Extração e Processamento de Dados**:
   - O Selenium acessa a página com os filtros aplicados, extrai a tabela completa, e o BeautifulSoup processa o HTML para melhor organização dos dados.

4. **Exportação dos Dados**:
   - Os dados são exportados para um arquivo CSV, pronto para análise em ferramentas externas, e também visualizados em HTML para revisão rápida.

## Como Executar o Projeto

1. **Instale as Dependências**:
   - Certifique-se de ter Python e as bibliotecas necessárias instaladas. Para instalar as dependências, execute:
     ```bash
     pip install selenium beautifulsoup4 pandas webdriver-manager
     ```
   
2. **Configure o Selenium**:
   - Instale o WebDriver apropriado (ex.: ChromeDriver para Google Chrome) e configure o caminho para o driver, se necessário.

3. **Execute o Script**:
   - Inicie o script no terminal e siga as instruções para selecionar os filtros desejados.
   - O script guiará o usuário através das opções de países, grupos de países e produtos, gerando a URL com os filtros escolhidos.

4. **Visualize e Exporte os Dados**:
   - Após a execução, o arquivo CSV estará disponível na pasta do projeto, juntamente com a versão em HTML para visualização.

## Desafios e Aprendizados

- **Interatividade e Simplicidade**: Manter a interação intuitiva apenas pelo terminal foi um desafio, exigindo um design cuidadoso para que o processo fosse claro e funcional.
- **Otimização da Extração de Dados**: Para evitar processos lentos, foi adotada uma abordagem que extrai a tabela completa como HTML, processando-a com BeautifulSoup e evitando capturas linha a linha.
- **Flexibilidade e Modularidade**: A estrutura do código permite fácil adaptação para outras necessidades de filtro e formatação, facilitando possíveis expansões e manutenções.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou novas funcionalidades, sinta-se à vontade para fazer um fork do repositório e enviar um pull request.

---

