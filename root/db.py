import micropg as p

conn=p.connect(user="postgres", password="postgres", host="128.197.176.151", port="5432", database="dvdrental")
cur = conn.cursor()
cur.execute('select title from film')
print(cur.fetchall())
cur.close()
