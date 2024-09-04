# :snake::computer: API Flask 

<!-- Sections -->

## :link: Seção

<!--ts-->

- [Estrutura de pastas](#estrutura-pastas)
- [Requisitos](#requisitos)
- [Instalação](#instacalao)
- [Endpoints](#endpoints)
- [Feedback](#feedback)
- [Autores](#autores)
- [Lincença](#licença)

<!--te-->

<!-- end Sections -->

<!-- Folder Structure -->

## :open_file_folder: Estrutura Pastas 

```sh
.
├── .routes
│   ├── characters.py
│   ├── episodes.py
│   └── locations.py
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
│   └── base.html
├── utils
│   └── config.py
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

### Sobre a organização das pastas

#### Rotas

- Criamos uma pasta ```/routes``` onde teremos para cada rota um arquivo .py para facilitar a organização.
- Criamos uma pasta ```/templates``` onde estará todos os templates (arquivos.html) que utilizamos para renderizar a página html.
- Criamos uma pasta  ```/utils``` ela ficará todas as funções que acharmos necessários para compartilhamento e uso geral do projeto. Ex: criamos a  ```api_url``` para facilitar a chamada da URL base da API que utilizamos.

#### Configuração

- Temos um arquivo ```.env``` onde fica nossas variáveis de sistema .

#### Template

- Criado o arquivo ```base.html``` que servirá como base de template dos arquivos em html, nele já temos configurado o bootstrap 5.

#### API

Para o consumo dos dados utilizamos a The Rick and Morty API

> doc: https://rickandmortyapi.com/documentation/


<!-- end Folder Structure -->

<!-- Requeriments -->

## Requisitos

- [Python](https://www.python.org/downloads/)

<!-- end Requeriments -->

## Instalação

> obs: executar os seguintes comandos no terminal (cmd)

```sh
# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual (Windows)
.venv\Scripts\activate

# ou Ative o ambiente virtual (Unix/macOS)
source .venv/bin/activate

# Instale as dependências
# como boa prática criamos o requirements.txt que contém todas as todas as bibliotecas utilizadas
pip install -r requirements.txt

# Rodando o projeto
# acessar a porta padrão no navegador -> Running on http://127.0.0.1:5000
# Lembrando que para acessar o projeto ele precisará ficar rodando no seu terminal
flask --app main run
```

<!-- Endpoint -->

## Endpoint

> Ex: http://127.0.0.1:5000/characters

## GET
| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `GET`    | `/characters`                            | Listagem de todos os personagens.        |
| `GET`    | `/characters/23`                         | Retorna o personagem de id #23.          |
| `GET`    | `/episodes`                              | Listagem de todos os episódios.          |
| `GET`    | `/episodes/28`                           | Retorna o episódio de id #28.            |
| `GET`    | `/locations`                             | Listagem de todas as localizações.       |
| `GET`    | `/locations/28`                          | Retorna a localização de id #28.         |

<!-- end Endpoint -->

<!-- Feedback -->

## Feedback

Se você tiver algum comentário, entre em contato conosco em @squad-hedy-lamar :purple_heart:.

<!-- end Feedback -->

<!-- Authors -->

## Autores

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