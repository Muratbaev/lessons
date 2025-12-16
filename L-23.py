# #1
# def hello():
#     return 'привет'
# #2
# def h(user):
#     return f'привет {user}'
# # print(h(user = input('ваше имя - ')))
# #3
# def dif(a, b):
#     return a-b
# #4
# def find_max(numbers):
#     if not numbers:
#         return None
#     sorted_nums = sorted(numbers)
#     return sorted_nums[-1]
# #5
# def digs(ls):
#     for i in range(1, 51):
#         print(i)
# #6
# def summ(a, b, c):
#     return a+b+c+100
# #7
# def leg(word):
#     ls = 0
#     for i in word:
#         ls+=1
#     return ls
# # print(leg(word=input('введи слово- ')))
# #8 : Функция принимает число и сообщает, найдено ли оно в диапазоне 1–100 
# def search(char:int):
#     if char in range(1, 100):
#         return f'число {char} есть в списке'
#     else:
#         print('не найдено')
# #9 Создай функцию, которая принимает список имён и возвращает первое имя.
# def names_1(names='start'):
#     nm = []
#     times = int(input('сколько имен записать? - '))
#     for i in range(times):
#         name = input('имя - ')
#         nm.append(name)
#     return nm[0]
# # print(names_1())
# #10
# def password():
#     pass_1 = input('введи пароль - ')
#     if len(pass_1)<6:
#         print('slabo')
#     elif 6<=len(pass_1)<=10:
#         print('norm')
#     elif len(pass_1)>10:
#         print('silno')

#second file
#1
def sum10(a, b, c, d, e, f, g,h,i, j):
    return a+b+c+d+e+f+g+h+i+j
#2
def dele(a, b):
    return a/b
#3
def sayhello1():
    return 'Hello world'
def sayhello2(a):
    a='Hello world'
    return a
#4
def summ(a, b, c=5):
    return a+b+c
#5
def chet(a):
    a=int(input('a= '))
    if a%2==0:
        return 'chetnoye'
    else:
        return 'nechetnoye'
#6
def trex(a):
    a=int(input('a='))
    if a//1000>=1:
        return 'chislo trexznach'
    else:
        return 'chislo ne trexznach'
    
#7
def mi():
    a=int(input('a= '))
    b=int(input('b= '))
    c=int(input('c= '))
    return max(a, b, c)

#8
def us(user):
    user=input('user- ')
    if '@' in user:
        return 'succesfully'
    else:
        return 'error'