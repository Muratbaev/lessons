
#17
a = int(input('число 1 - '))
b = int(input('число 2 - '))
c = int(input('число 3 - '))
if a>b>c or c>b>a:
    a=2*a
    b=2*b
    c=2*c
else:
    a=-a
    b=-b
    c=-c
print(a,b,c)

#18
a = int(input('число 1 - '))
b = int(input('число 2 - '))
c = int(input('число 3 - '))
if a==b:
    print('3')
elif a==c:
    print('2')
elif b==c:
    print('1')

#19
a = int(input('число 1 - '))
b = int(input('число 2 - '))
c = int(input('число 3 - '))
d = int(input('число 4 - '))
if a==b==c:
    print('4')
elif a==b==d:
    print('3')
elif a==c==d:
    print('2')
elif b==c==d:
    print('1')

#20
a = float(input('точка A - '))
b = float(input('точка B - '))
c = float(input('точка C - '))
if abs(a-c)<abs(b-c):
    print('точка A ближе к точке C')
elif abs(a-c)>abs(b-c):
    print('точка B ближе к точке C')
else:
    print('A==B')

#21
x = float(input('координата x1 - '))
y = float(input('координата y1 - '))
if x==0 and y==0:
    print('0')
elif x==0 and y>0:
    print('1')
elif x>0 and y==0:
        print('2')
elif x>0 and y>0:
        print('3')

#22
# I четверть: x>0 и y>0
# II четверть: x<0 и y>0
# III четверть: x<0 и y<0
# IV четверть: x>0 и y<0
x = float(input('координата x1 - '))
y = float(input('координата y1 - '))
if x>0 and y>0:
    print('I четверть')
elif x<0 and y>0:
    print('II четверть')
elif x<0 and y<0:
    print('III четверть')
elif x>0 and y<0:
    print('IV четверть')
   
#23
x1 = float(input('координата x1 - '))
y1 = float(input('координата y1 - '))
x2 = float(input('координата x2 - '))
y2 = float(input('координата y2 - '))
x3 = float(input('координата x3 - '))
y3 = float(input('координата y3 - '))
# x-координатa
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1
# y-координатa
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1
print('координаты четвертой точки: (', x4, ';', y4, ')')

#24
import math

x = float(input("Введите x: "))
if x > 0:
    y = 2 * math.sin(x)
else:
    y = 6 - x
print("f(x) =", y)

#25
x = float(input("Введите x: "))
if x<-2 or x>2:
    y = 2*x
else:
    y = -3*x
print("f(x) =", y)

#26
x = float(input("Введите x: "))
if x<=0:
    y = -x
elif 0<x<2:
    y = x**2
elif x>=2:
    y = 4
print("f(x) =", y)

#27
x = float(input("Введите x: "))

if x <= 0:
    y = 0
elif int(x) % 2 == 0:  # если целая часть числа ЧЁТНАЯ
    y = 1
else:
    y = -1

print("f(x) =", y)

#28
yr = int(input('год - '))
if (yr%4==0 and yr%100!=0) or yr%400==0:
    print('366 дней')
else:
    print('365 дней')

#29
n = int(input("Введите целое число: "))

if n < 0:
    n = -n  # if the digit is negatuve
if n >= 0 and n <= 9:
    print("однозначное число")
elif n >= 10 and n <= 99:
    print("двузначное число")
elif n >= 100 and n <= 999:
    print("трехзначное число")
else:
    print("многозначное число")

#30
n = int(input("Введите целое число: "))

if n < 0:
    n = -n  # if the digit is negatuve
if n >= 0 and n <= 9:
    print("однозначное число")
elif n >= 10 and n <= 99:
    print("двузначное число")
elif n >= 100 and n <= 999:
    print("трехзначное число")

print('that\'s the end')





