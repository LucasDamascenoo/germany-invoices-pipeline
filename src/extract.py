
import pandas as pd
import sqlite3
import os
from sqlalchemy import create_engine
from datetime import date
from pathlib import Path


db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/data.db'))

query = """

SELECT * FROM invoices

"""


conexao = sqlite3.connect(db_file)

data = pd.read_sql(query,conexao)



data_hoje = date.today()


csv = f'/home/ubuntao/dev/germany-invoices-pipeline/1_landing_zone/dados_full_invoices_{data_hoje}.csv'
json = f'/home/ubuntao/dev/germany-invoices-pipeline/1_landing_zone/dados_full_invoices_{data_hoje}.json'

data.to_csv(csv)
data.to_json(json)
