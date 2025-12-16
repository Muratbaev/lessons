import random
import math
#3
def random_num():
    a = random.randint(1, 10)
    return a

#4
def get_pi():
    p = math.pi
    return p


#7
def is_even(a):
    if a%2==0:
        print(True)
    else:
        print(False)

#9
def calc_area(s=1):
    r = int(input('радиус - '))
    s=r*r*3.14
    return s

#12
def get_power(a, b=2):
    return a**b 
#13
def user_data(username, usersname, userage:int):
    userd = {}
    userd['имя']=username
    userd['фамилия']=usersname
    userd['возраст']=userage
    return userd   

# print(user_data(username=input('имя - '),
#     usersname=input('фамилия - '),
#     userage=int(input('возраст - '))))

#11
def calc_dis(tov, dis=0):
    return tov-(tov*dis/100)

#14
# def calc_ship(w, v, cost):


#15
def adressf(name, country, city, street, house, comm='нету'):
    return f'''{name} живет в {country} в городе {city} на улице {street}, дом {house}
дополнительные комментарии по адресу: {comm}
'''
# adressf(name=input('имя'), country=input('страна'), city=input('город'), street=input('улица'), house=input('дом'), comm=input('доп комментарии по адресу'))

#16
def tovsum():
    tovary={}
    for i in range(3):
        name = input(f'товар {i+1}: ')
        price = int(input('цена: '))
        tovary[name]=price
    return sum(tovary.values())
print(tovsum())
