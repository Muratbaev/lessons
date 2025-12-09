# break, continue
#1
import turtle
#kvadrat
start = 1
stop = 4
# turtle.color('blue')
# turtle.pensize(3)

while start<=stop:
    turtle.forward(100)
    turtle.right(90)
    start+=1
turtle.done()


#triangle
start = 1
stop = 3
while start<=stop:
    turtle.forward(100)
    turtle.right(120)
    start+=1

#прямоугольник
start = 1
end = 2
while start<=end:
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    start+=1
turtle.done()

# circle
turtle.circle(100)

#3
digit = int(input('число - '))
start = 1
stop = digit
result = 1
while start<=stop:
    result*=start
    start+=1
print(result)

#5
start = 10
stop = 30
while start<=stop:
    if start!=15 and start!=20 and start!=25:
        print(start)
    start+=1

#6
start = 1
stop = 30
while start<=stop:
    if start<=10:
        print(start)
    start+=1

#7
start = 1
stop = 20
while start<=stop:
    if start%2==0:
        print(start)
    start+=1

#8
start = 1
stop = 10
a = ""
while start<=stop:
    user = input('ваше имя: ')
    a+=user + ', '
    start+=1
print(f'приглашенные: {a}')


#9
a = int(input('ввести число: '))
while a<5:
    a = int(input('введи число: '))
    if a>5:
        print(f'последнее число: {a}')


#10
a = input('кого пригласить? - ')
b = 0
while a!='все':
    a = input('еще кого-то? - ')
    b+=1
print(f'всего приглашено {b} челов')

#11
a = int(input('число: '))

while a>=10 or a<=20:
    a = int(input('число: '))
    if a<10:
        print('too small. try again')
    elif a>20:
        print('too big. try again')

