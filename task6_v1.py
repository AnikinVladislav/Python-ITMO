farmers = {}
reviews = {}


with open('Export.csv', 'r') as f:
    for data in f:
        data_row = data.strip().split(',')
        # print(data_row)
        # data_row[8] - City; data_row[10] - State; data_row[11] - zip_data
        farmers[data_row[0]] = data_row[1:]
# print(farmers)
print(farmers['1019863'][9])
city = input('Введите город:')
state = input('Введите штат:')
frm_interests = []
for fmid in farmers:
    market = farmers[fmid]
    market_porj = [market[0], market[7], market[9], market[10], market[19], market[20]]
    if market_porj[1] == city and market_porj[2] == state:
        frm_interests.append(fmid)

want_review = input('Хотите оставить рецензию на эти рынки (Да\Нет):')

if want_review.capitalize() == 'Да':
    reviews['name'] = input('Введите свое имя:')
    reviews['surname'] = input('Введите свою фамилию:')
    reviews['markerts_fmid'] = frm_interests
    print('Реценизруемые рынки:\n')
    for frm_interest in frm_interests:
        market_rev_porj = [farmers[frm_interest][0], farmers[frm_interest][7], farmers[frm_interest][9], farmers[frm_interest][10], farmers[frm_interest][19], farmers[frm_interest][20]]
        print(market_rev_porj)
    rate = int(input('Введите рейтинг (от 1 до 5):'))
    reviews['rate'] = (lambda x: 5 if x > 5 else(1 if x < 1 else x))(rate)
print(reviews)