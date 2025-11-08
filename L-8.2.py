#              HOMETASK 1
#1
start = 0
stop = int(input('a = '))

while start<=stop:
    print(start)
    start+=1

#2
start = int(input('a = '))
stop = 0
while start>=stop:
    print(start)
    start-=1

#3
start = int(input('начало = '))
stop = int(input('конец = '))
while start<=stop:
    print(start)
    start+=1

#4
start = 1
stop = int(input('конец - '))
total = 0

while start<=stop:
    total  = total + start
    start = start + 1

print(total)

# 5, 6 and 10 skip

#8
a = 'it\'s an infinitive loop'
while a == a:
    print(a)

#9
start = 1
finish = 5
text = 'I love python'
while start<=finish:
    print(text)
    start+=1

#11
start = 0
finish = 100
while start<=finish:
    print(start) 
    start+=10

#12
text = input('your text - ')
start = 2
finish = len(text) - 1
while start<=finish:
    print(text[start])
    start+=1

#              HOMETASK 2
#TEST
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
    {"1": "B", "2": "B", "3": "C", "4": "D", "5": "B", "6": "B", "7": "B", "8": "D"}
]
rows = [
    data[0]
]
rows += [(k, v) for k, v in data[1].items()]
print(pretty_table(rows))

#          PRACTICAL EXS
#1
start = 10
stop = 1
while start>=stop:
    print(start)
    start-=1

#2
start = int(input('a = '))
stop = int(input('b = '))
while start<=stop:
    if start%2==0:
        print(start)
    start+=1

#3
start  = 1
stop = 10
total = 0
while start<=stop:
    total  = total + start
    start = start + 1
print(total)

#4
text = 'python is fun!'
start = 1
stop = 5
while start<=5:
    print(text)
    start+=1

#5
start = 1
finish = 10
digit = int(input('число - '))
while start<=finish:
    print(f'{digit}*{start}={digit*start}')
    start+=1

#6
start = 1
end = 50
while start<=end:
    if start%2!=0:
        print(start)
    start+=1

#7 факториал числа
digit = int(input('число - '))
start = 1
stop = digit
result = 1
while start<=stop:
    result*=start
    start+=1
print(result)

#8 стопать цикл если юзер ввел число <0
text = int(input('введи число - '))
while text>=0:
    # print(text)
    text = int(input('введи число - '))
print('program stopped niha')

#9 вывод из 5х данных чисел только %3==0
count = 0
total = 5
while count < total:
    digit = int(input(f'число {count + 1} - '))
    if digit % 3 == 0:
        print(digit)
    count += 1

#10
text = 'hello world'
count = int(input('how many times? - '))
while count>=1:
    print(text)
    count-=1

print('that\'s the end')