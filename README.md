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

Caso os pytest nao funcionar local crie um arquivo "pytest.ini" na raiz do projeto e passe o seguinte codigo 
```sh
[pytest]
pythonpath = .
```

## Primeiro Teste

Para fazer um primeiro teste do playwright rode o comando
```sh
pytest app/tests/crmdev/login.py
```


