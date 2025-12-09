# list1 = [94, 23, 65, 23, 8734, 23]
# list2 = []
# a = int(input('какое число убрать из списка? - '))
# print(list1)
# for i in list1:
#     if i!=a:
#         list2.append(i)

# list2.append(a)
# list2.sort()
# print(list2)


# # Исходный список
# my_list = [4, 2, 5, 2, 3, 4, 1]
# # Создаем второй список с уникальными элементами
# unique_list = []
# for i in my_list:
#     if i not in unique_list:
#         unique_list.append(i)
# # Сортируем второй список
# unique_list.sort()
# print("Исходный список:", my_list)
# print("Список без повторов:", unique_list)
# my_dict = {'a':'ankara', 'b':'berlin', 'c':'capital'}
# value = my_dict.pop('b')
# print(my_dict)

phones = {
    'samsung':{
        's23 ultra':500,
        's22':480,
        's21':350,},
    'iphone':{
        '13 pro max':500,
        '12 pro max':400,
        'xr':300
    },
    'redmi':{
        'note 13 pro':450,
        'note 12 pro':400,
        'note 11 pro':300
    },
    'lg':{
        'g200':200,
        'g300':300,
        'g400':400,
    },
    # 'nokia':4,
    # 'tesla':500,
}

def choose():
    user = int(input('поиск по имени[1] или цене[2]? - '))
    if user == 1:
            company_user = input('введи название компании - ').lower() #ask about samsung/iphone/redmi
            if company_user in phones: # проверка наличия в phones   
                print(f'we have {phones[company_user]}')
                phone_user = input('введите название - ').lower()
                for phone_name, price in phones[company_user].items():
                    if phone_user == phone_name:
                        print(phone_name, 'стоит', price, '$')
                        break
            else:
                print('нет такого телефона')
    if user ==2:
        company_user = input('введи название компании - ').lower() #ask about samsung/iphone/redmi
        if company_user in phones: # проверка наличия в phones   
            print(f'we have {phones[company_user]}')
            phone_user = input('введите название - ').lower()
            for phone_name, price in phones[company_user].items():
                if phone_user == phone_name:
                    print(phone_name, 'стоит', price, '$')
                    break
        else:
                print('нет такого телефона')
    return
    
prices = [price for company in phones.values() for price in company.values()]


