# #
# #files , Exceptions

# # example = open(file='example.txt',mode='w')
# # #mode -> w,a,r

# # #w - write - qaytajaziw
# # #r - read - oqiw
# # #a - add - qosiw
# # example.write('Hello world')
# # example.close()

# # ex = open(file='example.txt',mode='a')
# # ex.write(',my name is Rasul')
# # ex.close()

# ex = open(file='example.txt',mode='r')
# copied = ex.read()
# ex.close()
# print(copied)

# malika = open(file='malika.txt',mode='w')
# malika.write(copied)
# malika.close()

# #parsing - parser
#text
#'10,2,4,67,asdsdghj'

# sanlar = open(file='example.txt',mode='r')
# copied = sanlar.read()
# print(copied)#string
# for i in copied:
#     print(int(i))

#split() - str -> list

# print(copied.split(','))#
# total = 0
# for i in copied.split(','):
#     total += int(i)
# print(total)#total - putin san - integer

# file = open(file='malika.txt',mode='w')
# file.write(str(total))
# file.close()


# names = ['Rasul', 'Alisher', 'Lamila', 'Indira', 'Malika', 'Nazira']
# file1 = open(file='file1.txt', mode='w')
# for name in names:
#     file1.write(name+'\n')
#     # file1.write('\n')

'''
#HOMETASK
#1
# mainfile = open(file='file1.txt', mode='w')
# mainfile.write('some text ')
# user = input('введи текст для добавления: ')
# mainfile.close()
# mainfile = open(file='file1.txt', mode='a')
# mainfile.write(user)
# mainfile.close()

# #2
# mainfile = open(file='file1.txt', mode='w')
# for i in range(1, 6):
#     mainfile.write(str(i)+' ')
# mainfile.close()

# user = input('введи цифры слитно - ')
# user = list(user)
# mainfile =  open(file='file1.txt', mode='w')
# mainfile.write(' '.join(user))
# mainfile.close()

# #3.	Попросите пользователя ввести название файла и некоторый текст.
# # Затем создайте новый файл с введенным названием и записью введенного текста.
# filename = input('введите название файла (без расширения - )')+'.txt'
# user_text = input('введите текст для содержания файла - ')
# file = open(file=filename, mode='w')
# file.write(user_text)
# file.close()

#4.	Создайте файл "quotes.txt" и запишите в него несколько любимых цитат.
# Напишите программу, которая открывает файл и выводит цитаты на экран.
quotes = ['Каждый глубокий мыслитель больше боится быть понятым, чем непонятым.',
          'Пока не покорила нас судьба, надобно водить ее за руку, как ребенка, и сечь ее; но если она нас покорила, то надобно стараться полюбить ее.',
          'Кто много мыслит, не годится в члены партии: он слишком быстро выйдет из нее своими мыслями.',
          'Скоро обед. Надо покушать']
q_file = open(file='q_file.txt', mode='w', encoding="utf-8")
q_file.write('\n'.join(quotes))
q_file.close()
q_file = open(file='q_file.txt', mode='r', encoding="utf-8")
copied = q_file.read()
print(copied)
q_file.close()

#5	Создайте файл "points.txt" и запишите в него координаты нескольких точек в формате (x, y).
# Попросите пользователя ввести новые координаты точки и добавьте их в конец файла.
coords = {'a':(1, 3),
          'b':(2, 4),
          'c':(3, 5)}
#zapis v file
points = open(file='points.txt', mode='w')
for key, (x, y) in coords.items():
    points.write(f'{key}:{x},{y}\n')
points.close()
#zapis novyx dannyx
new_x = int(input('новая координата x: '))
new_y = int(input('новая координата y: '))
points = open(file='points.txt', mode='a')
points.write(f'd:{new_x},{new_y}')
points.close()

#6.	Используйте файл "points.txt" из предыдущей задачи.
#  Попросите пользователя ввести новые координаты точек и перезапишите содержимое файла этими новыми координатами.

count = int(input("Сколько новых точек вы хотите записать? "))
new_coords = []
i = 0

while i < count:
    x = int(input(f"введите X для точки {i+1}: "))
    y = int(input(f"введите Y для точки {i+1}: "))
    new_coords.append((x, y))
    i += 1

# перезаписываем файл новыми координатами
q_file = open("points.txt", "w", encoding="utf-8")
i = 1

for coord in new_coords:
    x, y = coord
    q_file.write(f"n{i}: ({x}, {y})\n")
    i += 1

q_file.close()
print("файл points.txt перезаписан новыми координатами.")

#7.	Попросите пользователя ввести название файла и текст.
# Если файл с таким названием существует, добавьте введенный текст в конец файла.
# В противном случае создайте новый файл с введенным названием и записью текста.

#8
file = open(file='points.txt', mode='r')
copied = file.read()
print(copied)
file.close()



#10.	Создайте новый файл "new_points.txt" и попросите пользователя ввести координаты точек. 
# Запишите введенные координаты в файл.
i = 0
coords = []
while i<3:
    x = int(input(f'координата x{i+1}: '))
    y = int(input(f'координата y{i+1}: '))
    coords.append((x, y))
    i+=1
#zapis
new = open(file='new_points.txt', mode='w')
c = 1
for i in coords:
    x, y = i
    new.write(f"n{c}: ({x}, {y})\n")
    c+=1
new.close()

'''
