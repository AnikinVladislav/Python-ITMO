import model
import MySQLdb
def getAllMarkets():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                        user="root",         # your username
                        passwd="000000",     # your password
                        db="farmers")        # name of the data base
    cur = db.cursor()
    frms_list = model.readAllMarkets(cur)
    db.close()
    return frms_list