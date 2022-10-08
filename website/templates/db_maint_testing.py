import sqlite3
import pandas as pd

def to_csv():
    db = sqlite3.connect(r"C:\Users\brent\Desktop\flask web app\website\database.db")
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)
    db.close()

to_csv()