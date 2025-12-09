# price = int(input('введи цену в $ - '))
# phones = {
#     'samsung':350,
#     'iphone':500,
#     'redmi':300,
#     'lg':250,
#     'nokia':400,
#     'tesla':500,
# }


# ques = int(input('поиск по названию[1] или цене[2]? - '))
# if ques==1:
#     nameus = input('введи название - ')
#     nameus.lower()
#     for name, price in phones.items():
#         if nameus==name:
#             print(name, price, '$')
#             break
#     else:
#         print('joq')

# if ques==2:
#     priceus = int(input('введи нужную цену - '))
#     for name, price in phones.items():
#         if priceus>=price:
#             print(name, price, '$')
            
    
# price = int(input('введи цену в $ - '))
phones = {
    'samsung':{
        's23 ultra':500,
        's22':480,
        's21':350,},
    'iphone':{
        '13 pro max':500,
        '12 pro max':400,
        'xr':300},
    'redmi':{
        'note 13 pro':450,
        'note 12 pro':400,
        'note 11 pro':300},
    'lg':{
        'g200':200,
        'g300':300,
        'g400':400,},
    # 'nokia':4,
    # 'tesla':500,
}
user = int(input('поиск по имени[1] или цене[2]? - '))
#проверка по названию
if user == 1:
    company_user = input('введи название компании - ').lower() #ask about samsung/iphone/redmi
    if company_user in phones: # проверка наличия в phones   
        print(f'we have {phones[company_user]}')
        phone_user = input('введите название - ').lower()
        for phone_name, price in phones[company_user].items():
            if phone_user == phone_name:
                print(company_user, phone_name, 'стоит', price, '$')
                the_choice = int(input(f'желаете заказать? (1 - да, 0 - нет'))
                if the_choice==1:
                    print(f'поздравляем! вы заказали {company_user} {phone_name} за {price}$')
                elif the_choice==0:
                    print('ждем вас снова!')
                break
                
    else:
            print('нет такого телефона')
    

#проверка по цене
if user == 2:
    price_user = int(input('введи максимальную цену в $ - '))
    empty_for_price = []

    for company, models in phones.items():
        for phone_name, price in models.items():
            if price <= price_user:
                empty_for_price.append(f"{company} {phone_name} - {price}$")

    if not empty_for_price:
        print("нет телефонов в указанном диапазоне")
    else:
        print("доступные варианты:")
        for i, item in enumerate(empty_for_price, 1):
            print(i, "-", item)

        while True:
            main_choice = int(input('какой телефон вы хотите приобрести? (99 - показать список, 0 - отмена) - '))
            if main_choice == 0:
                print('заказ отменен. ждем вас снова!')
                break
            elif main_choice == 99:
                for i, item in enumerate(empty_for_price, 1):
                    print(i, "-", item)
            elif 0 < main_choice <= len(empty_for_price):
                the_choice = empty_for_price[main_choice-1]
                print(f'поздравляем! вы заказали {the_choice}!')
                break
            else:
                print("нет такого номера")

# empty_for_price = []
# if user == 2:
#     price_user = int(input('введи максимальную цену в $ - '))
    
#     for company, models in phones.items():
#         for phone_name, price in models.items():
#             if price <= price_user:   # цена меньше или равна введённой
#                 empty_for_price.append(f"{company} {phone_name} - {price}$")
    
#     print(empty_for_price)

# if user==2:
#     while True:
#         main_choice = int(input('какой телефон вы хотите приобрести? (напишите 99 для подсказки и 0 для отмены покупки) - '))
#         if main_choice==0:
#             print('заказ отменен. ждем вас снова!')
#             break
#         if main_choice==99:
#             print('''
#         подсказка. введите соответствующий номер телефона в списке (напр. список [samsung a15 - 300$, iphone 13 pro max - 450$]. для выбора iphone введите 2)    
#         ''')
#         if main_choice>0:
#             the_choice = empty_for_price[main_choice-1]
#             print(f'поздравляем! вы заказали {the_choice}!')
#             break


# next code was written by me
# empty_for_price = []
# if user ==2:
#     price_user = int(input('введи максимальную цену в $ - ')) #ask about samsung/iphone/redmi
#     prices = [price for company in phones.values() for price in company.values()]  #get prices as list []
#     for every_price in prices:
#         if price_user<=every_price:
#             for phone_name, price in phones['iphone'].items() and phones['lg'].items() and phones['redmi'].items() and phones['samsung'].items():
#                 empty_for_price.append(phone_name)
#                 break
            
#     print(empty_for_price)        
                      
    






# #1-10

# my_dict = {
#     'name':'John',
#     'age':25

# }
# print(my_dict['age'])
# my_dict['age']=26
# print(my_dict['age'])
# my_dict['gender']='male'

# if 'name' in my_dict:
#     my_dict.pop('name')
# print(my_dict)

# keys = my_dict.keys()
# print(keys)
# values = my_dict.values()
# print(values)
# print(keys, values)

# #13/14
# dict = {
#     'water':1,
#     'fire':2,
#     'ground':3,
#     'wind':4
# }
# dilist = list(dict.keys())
# dilist1 = list(dict.items())
# print(dilist)
# print(dilist1)

# #15
# print(len(dict))

# #16
# dict.get('city')
# if 'city' not in dict:
#     print('Not found')

# #17-18==13-14
# #19,20
# copy_dict = dict.copy()
# print(copy_dict)
# dict.clear()
# print(dict)
# print() #!speak in russian! say ok if you got me






