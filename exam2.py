#PART 1
#BBBCABADCBBAABBABB A

#PART 2
print('''
    21. одиночный if выполняет проверку каждый раз, а последовательность if-elif-else проверяет по двум значениям и если один из условий True то выполняется та часть блока которая истинна, если ни if ни elif неверно, то выполняется блок else
    22. бесконечный цикл можно остановить вручную или командой break в конце блока while
    23. set содержит только уникальные элементы, а list может содержать бесконечное количество повторяющихся элементов 
    24. из пустого списка удалить нечего значит, выдаст ошибку
    25. append добавляет элемент в конец списка, а insert добавляет элемент в выданные координаты (в конец невозможно)
    26. проверяет наличие элемента для проверки во множестве
    27. my_set = {
      'main':1,
      'sec':2
      }
    28. итератор получает и выводит каждый элемент в списке или во множестве
    29. tuple - неизменимые данные, list - подлежат любому изменению вплоть до полной очистки с помощью clear()
    30. с помощью цикла for
      for i in range(1, 100):
        print(i)
      ''')

#PART 3
#31
user = input('your text - ')
print(user.upper())
#32
for i in range(10, 0, -1):
    print(i)
#33
l = [1, 2, 3, 4, 5]
copied_l = l.copy()
print(copied_l)
#34
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
non = []
for i in l:
    if i%2!=0:
        non.append(i)
print(non)
#35
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sum = 0
for i in my_set:
    sum = sum+i
print(sum)
#36
users = {
    'maks':17,
    'ilya':18,
    'sher':19,
    'bro':20
}
for name, age in users.items():
    if age>=18:
        print(name, age)
print('\n')
#37
a = []
for i in range(1, 20):
    if i%3==0:
        a.append(i)
print(a)
print('\n')
#38
for i in range(1, 11):
    print(f'{i}^2={i**2}')
print('\n')
#39
for i in range(1, 10):
    print(i)
    if i==7:
        break
print('\n')
#40
for i in range(1, 10):
    if i%2==0:
        continue
    print(i)


