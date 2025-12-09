'''
#1
try:
    a = int(input('первое число - '))
    b = int(input('второе число - '))
except ValueError:
    print('введи только числа')
except ZeroDivisionError:
    print('на ноль  делить нельзя')
finally:
    print('программа завершена')

#2
try:
    file = open(file='data.txt', mode='r')
    copy = file.read()
    print(copy)
    file.close()
except FileNotFoundError:
    print('файл отсутствует')
finally:
    print('программа завершилась')

#3
try:
    user = int(input('введи число - '))
    print(user + 10)
except ValueError:
    print('это не число чел')
finally:
    print('программа завершилась')

#4
try:
    nums = [10, 5, "a", 8, 0]
    for num in nums:
        print(100/num)
except TypeError:
    print('ошибка при делении {num}')
'''
# #5
# try:
#     user = int(input('введи возраст - '))
#     if user<0:
#         print('возраст не может быть отрицательным')
# except ValueError:
#     print('введи цифры')
# finally:
#     print('возраст принят')

# #6
# try:
#     user = input('введи пароль - ')
#     if len(user)<6:
#         raise ValueError
# except ValueError:
#     print('слишком короткий пароль')
# finally:
#     print('Попробуй снова, если хочешь')

# #7
# try:
#     tot = 0
#     the = open(file='numbers.txt', mode='r')
#     copy = the.read()
#     the.close()
#     for i in copy:
#         tot +=int(i)
# except FileNotFoundError:
#     print('файл не найден')
# except ValueError:
#     print('в файле не числа')

# #9
# try:
#     user = {'name': 'Rasul', 'age': 20}
#     print(user[email])
# except KeyError:
#     print('такого ключа нет')
# except NameError:
#     print('NameError')

# #10
# try:
#     a = int(input('a = '))
#     b = int(input('b = '))
#     print(a/b)
# except ValueError:
#     print('нужно вводить числа')
# except ZeroDivisionError:
#     print('деление на ноль')
# except Exception:
#     print('общая ошибка')
# finally:
#     print('программа завершена')

# # finally:
# #     print('программа завершилась')

# #HOMETASK
# #1-3
# the = open(file='info.txt', mode='w')
# the.write('Я изучаю Python')
# the.close()
# the  = open(file='info.txt', mode='a')
# the.write('- и это интересно')
# the.close()
# the = open(file='info.txt', mode='r')
# copy = the.read()
# print(copy)
# the.close()

#4
num = open(file='numbers.txt', mode='w')
for i in range(2, 31, 2):
    num.write(str(i)+',')
num.close()

#5
try:
    num = open(file='numbers.txt', mode='r')
    copy = num.read()
    for i in copy.split(','):
        if int(i)%3==0:
            print(i)
except ValueError:
    pass

#6
li = ['Python', 'is', 'fun']
dile = open(file='file1.txt', mode='w')
for i in li:
    dile.write(i.join(', '))
dile.close()

#7
try:
    mm = open(file='magic.txt', mode='r')
except FileNotFoundError:
    print('такого файла нет')
finally:
    print('поиск закончен')
#8
words = ['hello', 'word', 'python']
fill = open(file='file2.txt', mode='w')
for i in words:
    fill.write(i+'\n')
fill.close()
fill = open(file='file2.txt', mode='r')
cop = fill.read()
print(cop)
fill.close()

#9
sum = 0
finn = open(file='numbers.txt', mode='w')
finn.write('5,10,15,20')
finn.close()
finn = open(file='numbers.txt', mode='r')
nums = finn.read()
lit = nums.split(',')
for num in lit:
    sum = sum+int(num)
print(sum)
finn.close()

