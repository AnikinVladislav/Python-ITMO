import MySQLdb
import model
import ETL


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="000000",     # your password
                     db="farmers")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Create table for review authors
# cur.execute("CREATE TABLE IF NOT EXISTS author (authorId INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL)")

# Create table for reviews
# cur.execute("CREATE TABLE IF NOT EXISTS reviews (rate TINYINT UNSIGNED NOT NULL, review TEXT, authorId INT NOT NULL, FMID INT UNSIGNED NOT NULL, FOREIGN KEY(authorId) REFERENCES author(authorId), FOREIGN KEY(FMID) REFERENCES frms_markets(FMID) ) ")

db.close()


# test_user = model.user('Ivan','Ivanov')
#
# id = test_user.get_author_id()
# print(id)

# name = ETL.get_User_Name_Surname('11')
# print(name)

reviews = ETL.getReviewsByFmid('1000368')
for i in reviews:
    print(i)
