farmers = {}
reviews = {'fmid': [], 'name': [], 'surname': [], 'rate': [], 'text': []}

with open('Export.csv', 'r') as f:
    for data in f:
        data_row = data.strip().split(',')
        # print(data_row)
        # data_row[8] - City; data_row[10] - State; data_row[11] - zip_data
        farmers[data_row[0]] = data_row[1:]

while(True):
    command = int(input('Выберете действие:\n 1.Посмотреть все фермерские рынки\n 2.Поиск фермерского рынка\n 3.Отставить реценизию\n 4. Выход\n'))
    if command < 1 or command > 4:
        print('Такой команды нет.')
    
    if command == 1:
        print('Все фермерские рынки:')
        for farm in farmers:
            print(farmers[farm])

        print('\n\nВсе рецензии:')
        if reviews == {}:
            print('Реценизий еще нет.\n\n')
        else:
            for review in reviews:
                print(review)
    
    if command == 2:
        command_search = int(input('По каким параметрам вы хотите найти фермерские рынки:\n 1.По городу и штату\n 2.Почтовый индекс\n'))
        if command < 1 or command > 2:
            print('Такого метода поиска нет, выберите метод из предложенных.')

        if command_search == 1:
            city = input('Введите город:')
            state = input('Введите штат:')
            search_fmid = []
            for fmid in farmers:
                market = farmers[fmid]
                market_porj = [market[0], market[7], market[9], market[10], market[19], market[20]]
                if market_porj[1] == city and market_porj[2] == state:
                    search_fmid.append(fmid)
                    print(f'\nID рынка:{fmid} Название рынка:{market_porj[0]} Город и штат рынка:{market_porj[1], market_porj[2]} Почтовый индекс:{market_porj[3]} Координаты:({market_porj[4]}, {market_porj[5]})')
            
        if command_search == 2:
            wanted_fmid = input('Введите почтовый индекс:')
            search_fmid = []
            for fmid in farmers:
                market = farmers[fmid]
                market_porj = [market[0], market[7], market[9], market[10], market[19], market[20]]
                if market_porj[3] == wanted_fmid:
                    search_fmid.append(fmid)
                    print(f'\nID рынка:{fmid} Название рынка:{market_porj[0]} Город и штат рынка:{market_porj[1], market_porj[2]} Почтовый индекс:{market_porj[3]} Координаты:({market_porj[4]}, {market_porj[5]})')

        if search_fmid == [] and (command_search == 1 or command_search == 2):
            print('Рынок не найден')
        else:
            want_more_info = input('Хотите больше информации о рынке (Да\Нет):')
            if want_more_info == 'Да':
                for fmid in search_fmid:
                    print(farmers[fmid])

    if command == 3:
            review_fmid = input('Введите fmid инетерисуемого рынка')    
            if review_fmid not in farmers.keys():
                print('Такого ID не существует')
            else:
                review_name = input('Введите свое имя:')
                review_surname = input('Введите свою фамилию:')
                rate = int(input('Введите рейтинг (от 1 до 5):'))
                review_rate = (lambda x: 5 if x > 5 else(1 if x < 1 else x))(rate)
                review_text = input('Напишите рецензию')
                reviews['fmid'].append(review_fmid)
                reviews['name'].append(review_name)
                reviews['surname'].append(review_surname)
                reviews['rate'].append(rate)
                reviews['text'].append(review_text)
    
    if command == 4:
        break




    
 
 

