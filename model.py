class FarmerMarket():

    def __init__(self, data):
        
        self.columnName = ["FMID","MarketName","Website","Facebook","Twitter","Youtube","OtherMedia","street","city","\
        County","State","zip","Season1Date","Season1Time","Season2Date","Season2Time","Season3Date","Season3Time","\
        Season4Date","Season4Time","x","y","Location","Credit","WIC","WICcash","SFMNP","SNAP","Organic","Bakedgoods","Cheese","\
        Crafts","Flowers","Eggs","Seafood","Herbs","Vegetables","Honey","Jams","Maple","Meat","Nursery","Nuts","Plants","Poultry","\
        Prepared","Soap","Trees","Wine","Coffee","Beans","Fruits","Grains","Juices","Mushrooms","PetFood","Tofu","WildHarvested","updateTime"]

        self.columnNameMain = ["FMID","MarketName","city","County","State","zip","x","y"]

        # function for processing farmer's market products
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
        return f'({self.FMID} , {self.MarketName} , {self.Website} , {self.Facebook} , {self.Twitter} , {self.Youtube} , {self.OtherMedia} , \
{self.street} , {self.city} , {self.County} , {self.State} , {self.zip} , {self.Season1Date} , {self.Season1Time} , {self.Season2Date} , \
{self.Season2Time} , {self.Season3Date} , {self.Season3Time} , {self.Season4Date} , {self.Season4Time} , {self.x} , {self.y} , {self.Location} , \
{self.Credit} , {self.WIC} , {self.WICcash} , {self.SFMNP} , {self.SNAP} , {self.Organic} , {self.Bakedgoods} , {self.Cheese} , \
{self.Crafts} , {self.Flowers} , {self.Eggs} , {self.Seafood} , {self.Herbs} , {self.Vegetables} , {self.Honey} , {self.Jams} , \
{self.Maple} , {self.Meat} , {self.Nursery} , {self.Nuts} , {self.Plants} , {self.Poultry} , {self.Prepared} , {self.Soap} , \
{self.Trees} , {self.Wine} , {self.Coffee} , {self.Beans} , {self.Fruits} , {self.Grains} , {self.Juices} , {self.Mushrooms} , \
{self.PetFood} , {self.Tofu} , {self.WildHarvested} , {self.updateTime})'

    def main_info(self):
        return f'({self.FMID} , {self.MarketName} , {self.city} , {self.County} , {self.State} , {self.zip} , {self.x} , {self.y})'


class review():

    def __init__(self, fmid, authid, rate, comment=""):
        self.fmid = fmid
        self.authorid = authid
        self.rate = rate
        self.comm = comment

    def __str__(self):
        return f'fmid = {self.fmid}, authorid = {self.authorid}, rate = {self.rate}, comment = {self.comm}'

    def add_to_DB(self, cur, db):
        sql = "INSERT INTO reviews (rate, review, authorId, FMID) VALUES (%s, %s, %s, %s)"
        val = (self.rate, self.comm, self.authorid, self.fmid)
        cur.execute(sql, val)
        db.commit()


class user():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def add_to_DB(self, cur, db):
        sql = "INSERT INTO author (name, surname) VALUES (%s, %s)"
        val = (self.name, self.surname)
        cur.execute(sql, val)
        db.commit()

    def get_author_id(self, cur):
        sql = "SELECT a.authorId FROM author a WHERE a.name = %s and a.surname = %s"
        val = (self.name, self.surname)
        cur.execute(sql, val)
        return cur.fetchone()[0]


def srchBycityandstate(fermers_list: FarmerMarket, city, state):
    temp_list = []
    for i in range(len(fermers_list)):
        if fermers_list[i].city == city and fermers_list[i].State == state:
            temp_list.append(fermers_list[i])
    return temp_list

def srchByZip(fermers_list: FarmerMarket, zip):
    temp_list = []
    for i in range(len(fermers_list)):
        if fermers_list[i].zip == zip:
            temp_list.append(fermers_list[i])
    return temp_list

def srchByArea(fermers_list: FarmerMarket, x, y, R):
    temp_list = []
    for i in range(len(fermers_list)):
        if ((fermers_list[i].x - x) ** 2 + (fermers_list[i].y - y) ** 2) <= R ** 2:
            temp_list.append(fermers_list[i])
    return temp_list

def showAllMarkets(fermers_list: FarmerMarket):
    for elem in fermers_list:
        print(elem.main_info())

def showAllReviews(review_list: review):
    for elem in review_list:
        print(elem)

def fermerMarketCheck(fermers_list: FarmerMarket, fmid):
    for i in range(len(fermers_list)):
        if fermers_list[i].FMID == fmid:
            return fermers_list[i]
    return None

def reviewCheck(review_list: review, fmid):
    temp_reviews_list = []
    for i in range(len(review_list)):
        if review_list[i].fmid == fmid:
            temp_reviews_list.append(review_list[i])
    return temp_reviews_list