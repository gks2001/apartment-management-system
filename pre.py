import sqlite3

conn = sqlite3.connect('apt.db')
c = conn.cursor()

c.execute("CREATE TABLE apt_tran (months integer, dates integer, years integer, details text, amt real, c_d text)")
c.execute("CREATE TABLE apt_def (aptno integer, months integer, years integer,details text, paid text)")
c.execute("CREATE TABLE apt_det (size text, cost real")


conn.commit()
conn.close()