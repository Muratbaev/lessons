#islower isupper isdigit isalnum isalpha
#boolean - True, False
# text = input('text to test: ')
# print(text.isupper())
# print(text.islower())
# print(text.isdigit()) #numbers
# print(text.isalnum()) #alphabet+numbers
# print(text.isalpha()) #alphabet

# print(text.startswith('a'))
# print(text.endswith('a'))

# print('' in text)

#1
print(10==5)
print(3<=3)
print(-7<0)
print(0>0)
print(7%2==0)
print(15%2==1)
a = "hello"
print(a.startswith('h'))
b = "world"
print(b.endswith("d"))
c = "Hello"
print(c.endswith("lo"))
d = "123345"
print(d.isdigit())

e = "Hello"
d = len(e)
print(d>3)

f = "HELLO"
print(f.isupper())

g = 'hello'
print(g.islower())

h = "a"
print(h.isalpha())

i = '7'
print(i.isdigit())

j = 10*5
print(j==50)

k = 8/2
print(k>2)

#       HOMETASK abramyan
#1
a = int(input('digit: '))
print(a>0)

#2
a = int(input('digit: '))
print(a%2==0)

#3
a = int(input('digit: '))
print(a%2==1)

#4
a = int(input('digit1: '))
b = int(input('digit2: '))
print(a>2 and b<=3)

#5
a = int(input('digit1: '))
b = int(input('digit2: '))
print(a>=0 and b<-2)

#6
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a<b<c)

#7
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a>b>c)

#8
a = int(input('digit1: '))
b = int(input('digit2: '))
print(a%2 ==1 and b%2==1)

#9
a = int(input('digit1: '))
b = int(input('digit2: '))
print(a%2 ==1 or b%2==1)

#10
a = int(input('digit1: '))
b = int(input('digit2: '))
print(a%2 ==1 or b%2==1)

#11
a = int(input('digit1: '))
b = int(input('digit2: '))
print(a%2 ==0 and b%2==0)

#12
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a>0 and b>0 and c>0)

#13
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a>0 or b>0 or c>0)

#14
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a>0 or c>0 or b>0)

#15
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a>0 and b>0 or a>0 and c>0 or b>0 and c>0)

#16
a = int(input('digit1: '))
print(a//10>1 and a%2==0)

#17
a = int(input('digit1: '))
print(a//100>1 and a%2==1)

#18
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a==b or b==c or a==c)

#19
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
print(a*b==1 or a*c==1 or b*c==1)

#20
a = int(input('трехзначное число: '))
sto = a//100
last = a%100%10
mid = a%100//10
print(sto!=last and sto!=mid and last!=mid)

#21
a = int(input('трехзначное число: '))
sto = a//100
last = a%100%10
mid = a%100//10
print(sto>last and sto>mid and last>mid)

#22
a = int(input('трехзначное число: '))
sto = a//100
last = a%100%10
mid = a%100//10
print((sto>last and sto>mid and last>mid) or (sto<last and sto<mid and last<mid))

#23
a = int(input('четырехзначное число: '))
first = a//1000
second = a%1000//100
third = a%1000%100//10
last = a%1000%100%10
print(first==last and second==third)

#24
a = int(input('digit1: '))
b = int(input('digit2: '))
c = int(input('digit3: '))
D = b**2+4*a*c
if D <0:
    print(False)
else:
    print(True)

#25
x = int(input('x: '))
y = int(input('y: '))
print(x<0 and y>0)

#26
x = int(input('x: '))
y = int(input('y: '))
print(x>0 and y<0)

#27
x = int(input('x: '))
y = int(input('y: '))
print(x<0 and y>0 or x<0 and y<0)

#28
x = int(input('x: '))
y = int(input('y: '))
print(x>0 and y>0 or x<0 and y<0)

#29
x = int(input('x: '))
y = int(input('y: '))
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
print((x2>x>x1) and (y1>y>y2) or (x1>x>x2) and (y2>y>y1))

#30
a = int(input('сторона1: '))
b = int(input('сторона2: '))
c = int(input('сторона3: '))
print(a==b==c)

#31
a = int(input('сторона1: '))
b = int(input('сторона2: '))
c = int(input('сторона3: '))
print(a==b or b==c or a==c)

#32
a = int(input('сторона1: '))
b = int(input('сторона2: '))
c = int(input('сторона3: '))
print(a==b==c)

#33
a = int(input('сторона1: '))
b = int(input('сторона2: '))
c = int(input('сторона3: '))
print((a**2+b**2)==c**2)

#34
x = int(input('coordinate 1: '))
y = int(input('coordinate 2: '))
if x>0 and y>0 and x<=8 and y<=8 and (x%2==1 and y%2==1):
    print(True)
else:
    print(False)

#35
x1 = int(input('coordinate x1: '))
y1 = int(input('coordinate y1: '))
x2 = int(input('coordinate x2: '))
y2 = int(input('coordinate y2: '))

result = (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8) and (
    (x1 % 2 == y1 % 2) == (x2 % 2 == y2 % 2)
)

print(result)

#36 ладья ходит по горизонтали или по вертикали прямо
x1 = int(input('coordinate x1: '))
y1 = int(input('coordinate y1: '))
x2 = int(input('coordinate x2: '))
y2 = int(input('coordinate y2: '))

result = (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8) and ((x1!=x2) and (y1!=y2)) and (x1==x2 or y1==y2)
print(result)

#37 король может ходить на соседнюю клетку вокруг себя
x1 = int(input('coordinate x1: '))
y1 = int(input('coordinate y1: '))
x2 = int(input('coordinate x2: '))
y2 = int(input('coordinate y2: '))
can = (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8) and ((x1!=x2) and (y1!=y2))
xmove = (x1 - x2 <= 1) and (x1 - x2 >= -1)
ymove = (y1 - y2 <= 1) and (y1 - y2 >= -1)
result = can and xmove and ymove
print(result)

#38 слон ходит по диагонали
x1 = int(input('coordinate x1: '))
y1 = int(input('coordinate y1: '))
x2 = int(input('coordinate x2: '))
y2 = int(input('coordinate y2: '))

can = (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8) and ((x1!=x2) and (y1!=y2))
xmove = x1 - x2
ymove = y1 - y2

result = can and ((xmove==ymove) or (xmove==-ymove))
print(result)

#39 ферзь это микс слона и ладьи
x1 = int(input('coordinate x1: '))
y1 = int(input('coordinate y1: '))
x2 = int(input('coordinate x2: '))
y2 = int(input('coordinate y2: '))

can1 = (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8) and ((x1!=x2) and (y1!=y2))
vert = (y1==y2)
goriz = (x1==x2)
xmove = x1 - x2
ymove = y1 - y2

diagonal = (xmove==ymove) or (xmove==-ymove)
can2 = vert or goriz or diagonal

result = can1 and can2
print(result)

#40 конь ходит в форме Г 
x1 = int(input('coordinate x1: '))
y1 = int(input('coordinate y1: '))
x2 = int(input('coordinate x2: '))
y2 = int(input('coordinate y2: '))

can1 = (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8) and ((x1 != x2) or (y1 != y2))
xmove = x1 - x2
ymove = y1 - y2

variant1 = ((xmove == 1) or (xmove == -1)) and ((ymove == 2) or (ymove == -2))
variant2 = ((xmove == 2) or (xmove == -2)) and ((ymove == 1) or (ymove == -1))
can2 = variant1 or variant2

result = can1 and can2
print(result)


print('that\'s all')