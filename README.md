# Base Fullstack Template

Este repositório é um template base fullstack para projetos futuros. A ideia é que um clone deste repositório seja usado como base para qualquer outro projeto. Ele inclui uma estrutura de backend em Python, frontend em JavaScript e configuração de infraestrutura para facilitar novos desenvolvimentos.

O ambiente recomendado de utilização deste projeto é o codespace do github, uma vez que ele já possui um terminal linux com diversos programas úties instalados como git, docker, python... Além disso, já existe uma conexão com o repositório github em questão.

A seguir detalhamos partes individuais do sistema. Posteriormente seguem comentarios de conexão entre eles.

## Frontend

Desenvolvido com Node.js com o framework Next. A versão do Next é definida no arquivo `.nvmrc`. Para instalar a versão especificada use:

```bash
cd frontend && nvm install
```

Os pacotes utilizados (dependências) neste projeto estão listados no arquivo `package.json` na chave "dependencies". Para instalar use:

```bash
cd frontend && npm install
```

## Backend

Desenvolvido em python com o framework FastAPI. Primeiro é necessário instalar o pacote de gerenciamento `uv` do python:

```bash
cd backend && pip install uv
```

A versão do python é definida no arquivo `.python-version`. Para instalar a versão especificada use:

```bash
cd backend && uv python install
```

Os pacotes utilizados (dependências) neste projeto estão listados no arquivo `pyproject.toml`. Para instalar use:

```bash
cd frontend && uv sync
```