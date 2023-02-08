import model
import MySQLdb

def getAllMarkets():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                        user="root",         # your username
                        passwd="000000",     # your password
                        db="farmers")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need

    cur = db.cursor()

    # # Create table for review authors
    # cur.execute("CREATE TABLE IF NOT EXISTS author (authorId INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL)")
    # # Create table for reviews
    # cur.execute("CREATE TABLE IF NOT EXISTS reviews (rate TINYINT UNSIGNED NOT NULL, review TEXT, authorId INT NOT NULL, FMID INT UNSIGNED NOT NULL, FOREIGN KEY(authorId) REFERENCES author(authorId), FOREIGN KEY(FMID) REFERENCES frms_markets(FMID) ) ")

    frms_list = []
    cur.execute("SELECT * FROM frms_markets")
    for row in cur.fetchall():
        temp = model.FarmerMarket(row)
        frms_list.append(temp)
    db.close()
    return frms_list


def getAllReviews():
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="000000",  # your password
                         db="farmers")  # name of the data base

    cur = db.cursor()
    reviews_list = []
    cur.execute("SELECT * FROM reviews")
    for row in cur.fetchall():
        temp = model.review(row[3], row[2], row[0], row[1])
        reviews_list.append(temp)
    db.close()
    return reviews_list


def add_User(name, surname):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="000000",  # your password
                         db="farmers")  # name of the data base

    cur = db.cursor()
    sql = "INSERT INTO author (name, surname) VALUES (%s, %s)"
    val = (name, surname)
    cur.execute(sql, val)
    db.commit()
    db.close()

def get_User_id(name, surname):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="000000",  # your password
                         db="farmers")  # name of the data base

    cur = db.cursor()
    sql = "SELECT a.authorId FROM author a WHERE a.name = %s and a.surname = %s"
    val = (name, surname)
    cur.execute(sql, val)
    return cur.fetchone()

def add_Review(rate, comm, authorid, fmid):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="000000",  # your password
                         db="farmers")  # name of the data base

    cur = db.cursor()
    sql = "INSERT INTO reviews (rate, review, authorId, FMID) VALUES (%s, %s, %s, %s)"
    val = (rate, comm, authorid, fmid)
    cur.execute(sql, val)
    db.commit()
    db.close()


def get_User_Name_Surname(id):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="000000",  # your password
                         db="farmers")  # name of the data base

    cur = db.cursor()
    sql = "SELECT a.name, a.surname FROM author a WHERE a.authorId = %s"
    val = (id,)
    cur.execute(sql, val)
    return cur.fetchone()