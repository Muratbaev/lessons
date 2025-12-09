import random
# угадай число
sec=random.randint(1, 100)
print(sec)

for i in range(1,7):
    user = int(input('san taw:'))
    if user>sec:
        print('odan az')
    elif user<sec:
        print('odan kop')
    if user ==sec:
        print('tawdin))')
        break
        
else:
    print('tawalmadin')

#камень ножницы бумага 
gad=random.randint(1,3)
if gad == 1:
    gad = 'камень'
elif gad == 2:
    gad = 'ножницы'
elif gad==3:
    gad='бумага'
print(f'выпал:{gad}')
pop = int(input('сколько попыток? - '))
for i in range(1, pop):
    user = input('что выпало? - ')
    if user==gad:
        print('нашел')
else:
    print('не нашел. игра окончена')

# for  i in range(1,10):
#     user = int(input('san jaz:'))
#     if user==5:
#         break
# else:
#     print('tawalmadin')

#           HOMETASK

#1 print 1-10
for i in range(1, 10+1):
    print(i)

#2 sum 1-100
a = 0
for i in range(1, 100+1):
    a = a+i
print(a)

#3 print a%2==0
for i in range(1, 20+1):
    if i%2==0:
        print(i)

#4 1*2*3*...*10
a = 1
for i in range(1, 10+1):
    a = a*i
print(a)

#5 print 10-1
for i in range(10,1-1, -1):
    print(i)

#6
a = int(input('a = '))
b = int(input('b = '))
c = 0
for i in range(a, b+1):
    c = c+i
print(c)

#7 don't print a%7==0 1-100
for i in range(1, 100+1):
    if i%7==0:
        continue
    print(i)

#8
for i in range(1, 100+1):
    if i%13==0:
        break
    print(i)

#9
for i in range(1, 50+1):
    print(i)
else:
    print("Цикл завершен")

#10
a = 5
for i in range(1, 11):
    b = a*i
    print(f'5*{i}={b}')


#DOC2
#           TESTS
def pretty_table(data, cell_sep=' | ', header_separator=True) -> str:
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [str(data[row][col]) for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    lines = []

    for i, row in enumerate(range(rows)):
        result = []
        for col in range(cols):
            item = str(data[row][col]).rjust(col_width[col])
            result.append(item)

        lines.append(cell_sep.join(result))

        if i == 0 and header_separator:
            lines.append(separator)

    return '\n'.join(lines)

#data for chart (my answers for the test)

data = [
    ["вопрос", "ответ"],
    {"1": "A", "2": "B", "3": "B", "4": "B", "5": "B", "6": "A", "7": "B", "8": "B", "9": "B", "10": "B"}
]
rows = [
    data[0]
]
rows += [(k, v) for k, v in data[1].items()]
print(pretty_table(rows))

#           PRACTICAL EXS

#1 skip a%5==0
a = 0
for i in range(1, 101):
    if i%5==0:
        continue
    a = a+i
print(a)

#2
for i in ('Python'):
    if  i =='o':
        continue
    print(i)

#3
a = ['apple', 'banana', 'cherry']
for i in(a):
    print(i.upper()) #сам написал

#4
a = input('введи текст - ')
for i in(a):
    if i=='a':
        print('@')
        continue
    print(i)

#5
a = 0
for i in range(1, 51):
    if i%2==1:
        continue
    a = a+i
print(a)

#6
pop = 0
number = 1
while pop < 5:
    if number % 7 == 0:
        print(number)
        pop += 1
    number += 1

#7
word = input('введи слово - ')
for i in reversed(word):
    if i=='a' or i=='e':
        continue
    print(i) #узнал как делать reversed text

#8
a = 1
for i in range(1, 11):
    if i%2==0:
        continue
    a = a*i
print(a)

#9
ekol = 0
text = input('введи строку - ')
low = text.lower()
for i in(low):
    if i=='e':
        ekol = ekol+1
else:
    print(f'количество буквы "e": {ekol}')

#10
for i in range(1, 21):
    if i==13:
        break
else:
    print('magic, bro')

print('that\'s the end')