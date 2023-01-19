import MySQLdb

conn = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="000000",     # your password
                     db="imdb")        # name of the data base

cur = conn.cursor()


cur.execute("""SELECT
   a2.id, a2.name, a2.surname 
FROM 
   actors a 
   , movieroles mr   -- movies with KB 
   , movieroles mr1  -- actors in movies for mr1 
   , actors a1 
   , movieroles mr2  -- actors in movies for mr1 
   , actors a2 
WHERE 
   a.id = mr.actorid 
   and a.name = 'Kevin (I)' 
   and a.surname = 'Bacon'  
   and mr1.movieid = mr.movieid 
   and mr1.actorid = a1.id 
   and mr1.actorid <> a.id 
   and mr2.movieid = mr1.movieid 
   and mr2.actorid = a2.id
   and a2.id not in (mr1.actorid);""")

res = cur.fetchall()
k = 0
for record in res:
    print(' '.join([str(x) for x in record]))
    k = k+1

print(k)