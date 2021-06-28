import micropg as p

conn=p.connect(user="postgres", password="postgres", host="128.197.176.151", port="5432", database="dvdrental")
cur = conn.cursor()
cur.execute('select title from film')

allMovies = cur.fetchall()
#cur.execute('truncate table selectedMovies restart identity')
for movie in allMovies:
        print("looking at", movie[0])
        if (movie[0][0] == 'B'):
                cur.execute('insert into selectedMovies(name) values(\''+movie[0]+'\')')
conn.commit()
cur.close()

cur = conn.cursor()
cur.execute('select * from selectedMovies')
print(cur.fetchall())
cur.close()

