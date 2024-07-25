import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'database.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'teste'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

""" SQL"""
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()
cursor.close()
connection.close()