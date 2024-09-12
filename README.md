# Playwright Python
Repositorio de Teste automatizado

## Requisitos
- Python ^3.10
- Poetry 
- Docker
- Docker compose

## SETUP INICIAL

Criação do ambiente Virtual

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Instalação das dependências do projeto

```sh
poetry install
```

Após instalado as dependencias ativar o ambiente

```sh
poetry shell
```

Após ativação do ambiente instale os navegadores do Playwright

```sh
playwright install
```

