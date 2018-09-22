## Visão Lógica

###	Visão Geral: Pacotes e Camadas

O framework Django organiza os projetos em apps, que são pastas que contêm uma funcionalidade independente do restante da aplicação. Além disso, existem arquivos de configuração e arquivos estáticos globais. A figura a seguir mostra a organização de pastas de um app.

![Diagrama de Pacotes](http://uploaddeimagens.com.br/images/001/384/521/original/DiagramaPacotes.png?1524419574)

* **apps**: cada app tem uma pasta com as suas models, views, formulários, testes, templates e arquivos estáticos. Além disso, também há um arquivo URLs que será incluso no URLs global.

    - **migrations** : pasta com as migrações para o banco de dados.

    - **static** : pasta com arquivos CSS, JavaScript e imagens.

    - **tests** : arquivos de testes refente ao app.

    - **templates** : arquivos html do app.

    - **locale** : traduções referentes ao app.

    - **models** : arquivos de models do app.

    - **views** : arquivos de views do app.

    - **forms** : arquivos de formulários do app.

    - **admin** : arquivo de conexão do app com o admin.

    - **urls.py** : arquivo que mapeia as as views com templates de cada app

    - **\__init\__** : arquivo que transforma o app em um pacote python.

    - **apps** : mapeia a pasta que o contém como um app.

    - **utils** : arquivos de validação dos apps.


* **config** : pasta com as configurações do projeto Django.

    - **urls.py** : inclui todos os URLs.py dos apps.

    - **\__init\__** : arquivo que transforma as configurações em um pacote python.

    - **settings** : arquivos com as configurações básicas da aplicação.

    - **wsgi** : especificação para uma interface simples e universal entre servidores web e aplicações web.

- **manage.py** : arquivo criado automaticamente pelo Django para gerênciamento de comandos.

- **docs** : documentação da aplicação.

- **compose** : pasta com arquivos do docker.

- **utility** : arquivos para o auxílio na instalação do software.

- **requirements** : organiza todos os pacotes/componentes que a aplicação utiliza em arquivos.
