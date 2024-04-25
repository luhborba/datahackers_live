# Streamlit DataHackers

Este repositório é voltado para o projeto realizado aovivo na Live do Data Hackers sobre Streamlit.

## Stack Utilizada

- Python
- Pyenv
- Poetry
- Streamlit
- Matplotlib
- Plotly
- Mkdocs
- Taskipy

## Link Úteis

- Documentação do Projeto: [https://luhborba.github.io/datahackers_live/](https://luhborba.github.io/datahackers_live/)
- Repositório do Projeto: [https://github.com/luhborba/datahackers_live](https://github.com/luhborba/datahackers_live)
- Link da Live: [https://www.youtube.com/live/nj835HNVWvg?si=e0c-MJdzt81pbA-i](https://www.youtube.com/live/nj835HNVWvg?si=e0c-MJdzt81pbA-i)

## Como utilizar este projeto

1. Clonando Projeto
```bash
git clone https://github.com/luhborba/datahackers_live.git
cd datahackers_live
```

2. Rodando Projeto com Pyenv e Poetry 
```bash
pyenv install 3.12.1
pyenv local 3.12.1
poetry env use 3.12.1
poetry shell
poetry install
```
Você pode utilizar a versão do Python desejada.

3. Rodando Serviço do Streamlit
```bash
task run
```

4. Rodando Serviço de Documentação
```bash
task doc
```

4. Rodando Gerador de Dados
```bash
task gerar
```