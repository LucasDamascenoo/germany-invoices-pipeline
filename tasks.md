# Projeto de Engenharia de Dados: Faturas da Alemanha

## ✨ Nome do Projeto:

**germany-invoices-pipeline** ou **de-invoice-etl-pipeline**

---

## ♻ Projeto de Engenharia de Dados: Faturas da Alemanha

### 🌟 Objetivo:

Construir um pipeline de dados que extrai, transforma, valida e armazena faturas cuja origem seja a Alemanha e total ≥ 2.0.

---

## ✅ **Etapas do Projeto **

---

### 🟠 1. **Ingestão de Dados**

**Dia 1**

- Carregar os dados da base SQLite original.
- Converter esses dados em CSV ou JSON.
- Armazenar o arquivo em um diretório local simulado como `landing_zone`.

---

### 🟡 2. **Validação e Limpeza**

**Dia 2**

- Remover registros com `Total` nulo ou menor que 0.
- Padronizar o campo `BillingCountry` (remover espaços, usar capitalização correta).
- Salvar dados limpos em `bronze_zone`.

---

### 🟢 3. **Transformação**

**Dia 3**

- Filtrar somente faturas com `BillingCountry = 'Germany'` e `Total >= 2.0`.
- Adicionar coluna `HighValue` (Total > 100 → True).
- Salvar o resultado em `silver_zone`.

---

### 🔹 4. **Carga (Armazenamento Estruturado)**

**Dia 4**

- Salvar os dados finais (gold) em:
  - Formato Parquet (simulando uso em Data Lake)
  - Banco de dados local SQLite ou PostgreSQL (simulando um DWH)
- Criar uma tabela chamada `germany_invoices`

---

### ⚙️ 5. **Orquestração Local**

**Dia 5**

- Criar um script principal (ex: `main.py`) que executa todas as etapas.
- Organizar os módulos em:

  ```
  ├── 1_landing_zone/
  ├── 2_bronze_zone/
  ├── 3_silver_zone/
  ├── 4_gold_zone/
  ├── src/
  │   ├── ingest.py
  │   ├── clean.py
  │   ├── transform.py
  │   └── load.py
  └── main.py
  ```

- Adicionar logging básico com `loguru` ou `logging`.

---

### 💡 Extra (opcional)

- Criar um DAG no Airflow com essas 4 tarefas.
- Criar um dashboard no Superset com total de faturas por mês na Alemanha.
