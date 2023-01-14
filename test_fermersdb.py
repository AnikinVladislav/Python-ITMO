import MySQLdb

class FarmerMarket():

    def __init__(self, data):
        # FMID,MarketName,Website,Facebook,Twitter,Youtube,OtherMedia,street,city,\
        # County,State,zip,Season1Date,Season1Time,Season2Date,Season2Time,Season3Date,Season3Time,\
        # Season4Date,Season4Time,x,y,Location,Credit,WIC,WICcash,SFMNP,SNAP,Organic,Bakedgoods,Cheese,\
        # Crafts,Flowers,Eggs,Seafood,Herbs,Vegetables,Honey,Jams,Maple,Meat,Nursery,Nuts,Plants,Poultry,\
        # Prepared,Soap,Trees,Wine,Coffee,Beans,Fruits,Grains,Juices,Mushrooms,PetFood,Tofu,WildHarvested,updateTime

        def preprocess(parametr):
            if parametr == 'Y':
                return 1
            elif parametr == 'N':
                return 0
            else:
                return 2


        self.FMID = data[0]
        self.MarketName = data[1]
        self.Website = data[2]
        self.Facebook = data[3]
        self.Twitter = data[4]
        self.Youtube = data[5]
        self.OtherMedia = data[6]
        self.street = data[7]
        self.city = data[8]
        self.County = data[9]
        self.State = data[10]
        self.zip = data[11]
        self.Season1Date = data[12]
        self.Season1Time = data[13]
        self.Season2Date = data[14]
        self.Season2Time = data[15]
        self.Season3Date = data[16]
        self.Season3Time = data[17]
        self.Season4Date = data[18]
        self.Season4Time = data[19]
        self.x = data[20]
        self.y = data[21]
        self.Location = data[22]
        self.Credit = preprocess(data[23])
        self.WIC = preprocess(data[24])
        self.WICcash = preprocess(data[25])
        self.SFMNP = preprocess(data[26])
        self.SNAP = preprocess(data[27])
        self.Organic = preprocess(data[28])
        self.Bakedgoods = preprocess(data[29])
        self.Cheese = preprocess(data[30])
        self.Crafts = preprocess(data[31])
        self.Flowers = preprocess(data[32])
        self.Eggs = preprocess(data[33])
        self.Seafood = preprocess(data[34])
        self.Herbs = preprocess(data[35])
        self.Vegetables = preprocess(data[36])
        self.Honey = preprocess(data[37])
        self.Jams = preprocess(data[38])
        self.Maple = preprocess(data[39])
        self.Meat = preprocess(data[40])
        self.Nursery = preprocess(data[41])
        self.Nuts = preprocess(data[42])
        self.Plants = preprocess(data[43])
        self.Poultry = preprocess(data[44])
        self.Prepared = preprocess(data[45])
        self.Soap = preprocess(data[46])
        self.Trees = preprocess(data[47])
        self.Wine = preprocess(data[48])
        self.Coffee = preprocess(data[49])
        self.Beans = preprocess(data[50])
        self.Fruits = preprocess(data[51])
        self.Grains = preprocess(data[52])
        self.Juices = preprocess(data[53])
        self.Mushrooms = preprocess(data[54])
        self.PetFood = preprocess(data[55])
        self.Tofu = preprocess(data[56])
        self.WildHarvested = preprocess(data[57])
        self.updateTime = data[58]
    

    def __str__(self):
        return f'({self.FMID } , {self.MarketName } , {self.Website } , {self.Facebook } , {self.Twitter } , {self.Youtube } , {self.OtherMedia } , \
{self.street } , {self.city } , {self.County } , {self.State } , {self.zip } , {self.Season1Date } , {self.Season1Time } , {self.Season2Date } , \
{self.Season2Time } , {self.Season3Date} , {self.Season3Time } , {self.Season4Date } , {self.Season4Time } , {self.x } , {self.y } , {self.Location } , \
{self.Credit } , {self.WIC } , {self.WICcash } , {self.SFMNP } , {self.SNAP } , {self.Organic } , {self.Bakedgoods } , {self.Cheese } , \
{self.Crafts } , {self.Flowers } , {self.Eggs } , {self.Seafood } , {self.Herbs } , {self.Vegetables } , {self.Honey } , {self.Jams } , \
{self.Maple } , {self.Meat } , {self.Nursery } , {self.Nuts } , {self.Plants } , {self.Poultry } , {self.Prepared } , {self.Soap } , \
{self.Trees } , {self.Wine } , {self.Coffee } , {self.Beans } , {self.Fruits } , {self.Grains } , {self.Juices } , {self.Mushrooms } , \
{self.PetFood } , {self.Tofu } , {self.WildHarvested } , {self.updateTime })'


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="000000",     # your password
                     db="farmers")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM frms_markets")

frms_list = []

# print all the first cell of all the rows
for row in cur.fetchall():
    temp = FarmerMarket(row)
    frms_list.append(temp)
    print(row)

db.close()

print(frms_list[5])