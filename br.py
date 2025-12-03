import sqlite3

conn1 = sqlite3.connect(f"bd/Eddy_bd.db")
cur1 = conn1.cursor()
cur1.execute(f"SELECT * FROM Eddy")
raws=cur1.fetchall()
print(f"{raws}=raw")