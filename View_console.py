import model
import ETL


frms_list = ETL.getAllMarkets()

while (True):

    command = input('Выберете действие:\n 1.Посмотреть все фермерские рынки\n 2.Поиск фермерского рынка\n 3.Оставить реценизию\n 4. Выход\n')

    if command == '1':
        print('Все фермерские рынки:')
        model.showAllMarkets(frms_list)

        print('\n\nВсе рецензии:')
        review_list = ETL.getAllReviews()
        if review_list == []:
            print('Рецензий еще нет\n')
        else:
            model.showAllReviews(review_list)

    elif command == '2':
        command_search = input('По каким параметрам вы хотите найти фермерские рынки:\n 1.По городу и штату\n 2.Почтовый индекс\n 3.На определенном растоянии от вас\n')

        if command_search == '1':
            city = input('Введите город:')
            state = input('Введите штат:')
            search_list = model.srchBycityandstate(frms_list, city, state)
            if search_list == []:
                print('Рынок не найден\n')
            else:
                model.showAllMarkets(search_list)

        elif command_search == '2':
            wanted_zip = input('Введите почтовый индекс:')
            search_list = model.srchByZip(frms_list, wanted_zip)
            model.showAllMarkets(search_list)
            if search_list == []:
                print('Рынок не найден\n')
            else:
                model.showAllMarkets(search_list)

        elif command_search == '3':
            R = int(input('Введите расстояние поиска в милях:'))
            x = -89.5
            y = 34.4
            search_list = model.srchByArea(frms_list, x, y, R)
            model.showAllMarkets(search_list)

        else:
            print('Такого метода поиска нет, выберите метод из предложенных\n')


        # want_more_info = input('Хотите больше информации о рынке (Да\Нет):')
        # if want_more_info == 'Да':
        #     for fmid in search_fmid:
        #         print(farmers[fmid])

    elif command == '3':
        review_fmid = int(input('Введите fmid интересуещего рынка: '))
        selectedFermMarket = model.fermerMarketCheck(frms_list, review_fmid)
        if selectedFermMarket != None:
            print('Такой ID существует')

            #     review_name = input('Введите свое имя:')
            #     review_surname = input('Введите свою фамилию:')
            #     rate = int(input('Введите рейтинг (от 1 до 5):'))
            #     review_rate = (lambda x: 5 if x > 5 else (1 if x < 1 else x))(rate)
            #     review_text = input('Напишите рецензию')
            #     reviews['fmid'].append(review_fmid)
            #     reviews['name'].append(review_name)
            #     reviews['surname'].append(review_surname)
            #     reviews['rate'].append(rate)
            #     reviews['text'].append(review_text)

        else:
            print('Такого ID не существует')

    elif command == '4':
        break

    else:
        print('Такой команды нет.')
