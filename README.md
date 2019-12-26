# ae_scraping

## Instalação de requisitos (NECESSÁRIO:Python 3.6.0+ e pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça um clone do projeto: `git clone https://github.com/Luanlpg/ae_scraping.git`

- Acesse o repositório: `cd ae_scraping/`

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Rodando o server

- Acesse o projeto django: `cd api/`

- Rode as migrações do projeto: `python manage.py migrate`

- Rode o servidor local com: `python manage.py runserver`

## Navegando pela api

- GET `localhost:8000/parse`: lista logs de requisições de scraping

- POST `localhost:8000/parse`: requisiciona scraping
