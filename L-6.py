#if elif else

# color = input('ren jaz:')
# color1 = color.lower()
# if color1=='jasil' or color1=='зеленый' or color1=='green':
#     print('juredi')
# elif color1=='sari' or color1 == 'yellow' or color1=='желтый':
#     print('tayarlanadi')
# elif color1=='qizil' or color1=='red' or color1=='красный':
#     print('toqtaydi')
# else:
#     print('basqa ren jazba!')



# a = int(input('san = '))

# if a>0:
#     a = a+100
# elif a<0:
#     a = a+10
# elif a==0:
#     a = 5
# print(a)

#1
a = int(input('a = '))
if a ==5:
    print('Число = 5')
else:
    print('число не равно 5')

#2
a = int(input('a = '))
b = int(input('b = '))
if a>b:
    print('a>b')
else:
    print('a<=b')

#3
x = int(input('x = '))
if x>0:
    print('положиительное')
elif x<0:
    print('отрицательное')
else:
    print('ноль')

#4
a = int(input('a = '))
if a%2==0:
    print('четное')
else:
    print('нечетное')

#5
a = int(input('a = '))
b = int(input('b = '))
if a==10 and b==20:
    print('оба условия выполнены')
else:
    print('Одно или оба условия не выполнены')

#6
x = int(input('x - '))
if x>100:
    print('x больше 100')
elif 50<x<100:
    print('от 50 до 100')
else:
    print('меньше 50')

#7
text = input('текст - ')
if text == 'Python':
    print('отличный выбор')
else:
    print('попробуйте снова')

#8
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a>b>c:
    print('упорядочены по убыванию')
else:
    print('не упорядочены')

#9
x = int(input('x - '))
if x == 0 or x<-10:
    print('особый случай')
else:
    print('обычное число')
#10
password = input('пароль - ')
if password=='admin':
    print('доступ разрешен')
else:
    print('неверный пароль')


#           HOMETASK 1

#1
m = int(input('m = '))
n = int(input('n = '))
if n==0:
    print('m на n не делится')
else:
    print(m/n)

#2
n = int(input('n = '))
if n%2==1:
    n = n+1
else:
    n = n+2
print(n)

#3
n = int(input('n = '))
a1 = n//10 #1 цифра
a2 = n%10 #2 цифра
if n<10:
    print('введи двузначное число')
elif n>=100:
    print('введи двузначное число')


if a1>a2:
    print('первая цифра больше второй')
elif a2>a1:
    print('вторая цифра больше первой')
elif a1==a1:
    print('цифры числа одинаковы')

#4
n = int(input('n = '))
n1 = n%10
if n1==0:
    print(True)
elif n1==1:
    print(False)

#5
a = int(input('a = '))
b = int(input('b = '))
if a%b==0:
    print('a делитель b')
elif b%a==0:
    print('b делитель а')

#6
a = int(input('a = '))
if -5<a<3:
    print(True)
else:
    print(False)

#7
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a<b<c:
    print(True)
elif b>a>c:
    print(True)

#8
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a==b==c:
    print(True)
else:
    print(False)

#9
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a>0:
    print(a**2)
elif b>0:
    print(b**2)
elif c>0:
    print(c**2)
else:
    print(False)

#10
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a>b>c:
    print(b*c)
elif a>c>b:
    print(c*b)
elif b>a>c:
    print(a*c)
elif c>b>a:
    print(b*a)

#           HOMETASK 2
#1
a = int(input('число - '))
if a%2==1:
    print('нечетное')
elif a%2==0:
    print('четное')

#2
age = int(input('возраст - '))
if age>=18:
    print('совершеннолетний')
else:
    print('мелкий ещё')

#3
a = int(input('число 1 - '))
b = int(input('число 2 - '))
if a>b:
    print('число 1 больше')
else:
    print('число 2 больше')

#4
a = int(input('число - '))
if a>0:
    print('положительное')
elif a==0:
    print(a)
elif a<0:
    print('отрицательное')

#5
name = input('имя - ').lower()
if name.startswith('a'):
    print('начинается на А')
else:
    print('не начинается на А')

#6
num = int(input('целое число - '))
if num%3==0:
    print('число кратно 3')
elif num%5==0:
    print('число кратно 5')
elif num%3==0 and num%5==0:
    print('число кратно 3 и 5')
else:
    print('число не кратно 3 и не кратно 5')

#7
h = float(input('рост в м - '))
w = float(input('вес в кг - '))
imt = w/h**2

if 18.5<=imt<=24.9:
    print('ваш вес в норме')
elif imt<18.5:
    print('веса не хватает')
elif imt>24.9:
    print('перевес')

#8
a = int(input('a = '))
b = int(input('b = '))
if a>0 and b>0:
    print(a+b)
else:
    print('нельзя складывать положительные числа')

#9
yr = int(input('год рождения - '))
if (yr%4==0 and yr%100!=0) or yr%400==0:
    print('год високосный')
else:
    print('год не високосный')


print('that\'s the end')