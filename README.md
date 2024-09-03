# :snake::computer: API Flask 

<!-- Sections -->

## :link: Seção

<!--ts-->

- [Estrutura de pastas](#estrutura-pastas)
- [Requisitos](#requisitos)
- [Instalação](#instacalao)
- [Feedback](#feedback)
- [Autores](#autores)
- [Lincença](#license)

<!--te-->

<!-- end Sections -->

<!-- Folder Structure -->

## :open_file_folder: Estrutura Pastas 

```sh
.
├── .routes
│   ├── characters
│   ├── episodes
│   └── locations
├── templates
│   ├── characters
│   |   |   details.html
│   |   └── list.html
│   ├── episodes
│   |   |   details.html
│   |   └── list.html
│   └── locations
│   |   |   details.html
│   |   └── list.html
├── utils
│   └── config.py
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

### Sobre a organização das pastas
- Criamos uma pasta ```routes``` onde teremos para cada rota um arquivo .py para facilitar a organização.
- Criamos uma pasta ```templates``` onde estará todos os templates (arquivos.html) que utilizamos para renderizar a página html.
- Criamos uma pasta  ```utils``` ela ficará todas as funções que acharmos necessários para compartilhamento e uso geral do projeto. Ex: criamos a  ```api_url``` para facilitar a chamada da URL base da API que utilizamos.
- Temos um arquivo ```.env``` onde fica nossas variáveis de sistema 

<!-- end Folder Structure -->

<!-- Requeriments -->

## Requisitos

- [Python](https://www.python.org/downloads/)

<!-- end Requeriments -->

## Instalação

> obs: executar os seguintes comandos no terminal (cmd)

```sh
#clonar o projeto na sua máquina
git clone https://github.com/squad-hedy-lamar/api-flask

# entrar na pasta do projeto
cd api-flask

# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual (Windows)
.venv\Scripts\activate

# ou Ative o ambiente virtual (Unix/macOS:)
source .venv/bin/activate

# Instale as dependências
# todas as bibliotecas utilizadas nesse projeto estão nesse arquivo
pip install -r requirements.txt

# Rodando o projeto
# acessar a porta padrão no navegador -> Running on http://127.0.0.1:5000
flask --app main run
```

<!-- Feedback -->

## Feedback

Se você tiver algum comentário, entre em contato conosco em @squad-hedy-lamar :purple_heart:.

<!-- end Feedback -->

<!-- Authors -->

## Authors

- [@Daniela2319](https://github.com/Daniela2319)
- [@emanoelados](https://github.com/emanoelados)
- [@helen-13](https://github.com/helen-13)
- [@jadefigueredo](https://github.com/jadefigueredo)
- [@karenyov](https://www.github.com/karenyov)
- [@marianasouzar](https://github.com/marianasouzar)
- [@natachabkr1](https://github.com/natachabkr1)
- [@SATRbytes](https://github.com/SATRbytes)
- [@soubabx](https://github.com/soubabx)

<!-- end Authors -->

<!-- License -->

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

<!-- end License -->