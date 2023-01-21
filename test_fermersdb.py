import MySQLdb
import model


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="000000",     # your password
                     db="farmers")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Create table for review authors
cur.execute("CREATE TABLE IF NOT EXISTS author (authorId INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL)")

# Create table for reviews
cur.execute("CREATE TABLE IF NOT EXISTS reviews (rate TINYINT UNSIGNED NOT NULL, review TEXT, authorId INT NOT NULL, FMID INT UNSIGNED NOT NULL, FOREIGN KEY(authorId) REFERENCES author(authorId), FOREIGN KEY(FMID) REFERENCES frms_markets(FMID) ) ")


frms_list = model.readAllMarkets(cur)

# for elem in frms_list:
#      print(elem.main_info())

model.showAllMarkets(frms_list)




db.close()

