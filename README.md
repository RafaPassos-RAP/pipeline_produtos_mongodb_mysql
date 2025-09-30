# Pipeline de Dados - MongoDB e MySQL

Este projeto implementa um pipeline de dados que:

- Extrai dados de uma API
- Armazena no MongoDB
- Trata os dados
- Insere no MySQL

## Como rodar

1. Clone o repositório
2. Crie um `.env` com as variáveis:
   - `MONGODB_URI=...`
   - `DB_HOST=...`
   - etc.
3. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

4. Instale as dependências:
    pip install -r requirements.txt

5. Estrutura:
    scripts/ – scripts Python do pipeline e tratamento
    notebooks/ – scripts Python do pipeline e tratamento em ipynb
    data/ – arquivos CSV gerados (não versionados)
