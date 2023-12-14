import sqlite3 as sql

con = sql.connect ('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS events')

sql = '''CREATE TABLE "events" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "USUARIO" TEXT,
    "NOME_EVENTO" TEXT,
    "LOCAL" TEXT,
    "DATA" SMALLDATETIME
    )'''

cur.execute(sql)
con.commit()
con.close()