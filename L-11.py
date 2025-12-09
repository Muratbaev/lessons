#           структуры данных

#7

# text = input('jaziw jaz:')
# print(text[::-1])
# for i in text[::-1]:
#     print(i)


# san = 5
# start = 1
# stop = 10
# for i in range(start,stop+1):
#     print(f'{san}*{i}={i*san}')


#структуры данных

#list -  список - dizim
#set - набор(множество) -  koplik
#tuple -  кортеж - izbe-izlik
#dictionary - словарь  - sozlik


# name = 'Rasul'

# names = ['Jamila','Nazira','Azamat','Alisher']


# my_list = ['Hello',123,3.14,True]
# print(my_list)

# fridge = ['meat','bread','eggs','butter','milk']
# # text = 'hello world'
# print(text[0])
# # print(fridge)
# print(fridge[0])

# print(fridge[-1])

# fridge[1]='Orange'
# print(fridge)
# fridge.append('Cola')
# print(fridge)
# fridge.insert(-1,'Shashlik')#
# print(fridge)
# from_bazar = ['Apple','Pineapple','Bananas','Cherry']
# fridge.append(from_bazar)
# fridge.extend(from_bazar)
# print(fridge)



# products = ['john','bread','banana','iphone']
# products.pop(0)
# print(products)
# products.remove('iphone')
# print(products)

#sort,reverse,count,index

# nums = [45,12,77,2323,12,58,65123,554,]
# nums.reverse()
# print(nums)
# nums.sort()
# print(nums)
# letters = ['bcv','asd','wea','fgd','abc']
# letters.sort()
# print(letters)



# nums = []
# for i in range(1,10+1):
#     nums.append(i)

# print(nums)

# nums = [123,234,12,786,12,23,986,23,889,43,12]
# # print(nums.count(12))
# print(nums.index(12))
# for i in nums:
#     if i%2==0:
#         print(i)

# #7
# # Исходный список
# my_list = [4, 2, 5, 2, 3, 4, 1]

# # Создаем второй список с уникальными элементами
# unique_list = []
# for i in my_list:
#     if i not in unique_list:
#         unique_list.append(i)

# # Сортируем второй список
# unique_list.sort()

# print("Исходный список:", my_list)
# print("Список без повторов:", unique_list)


# # 1
# #           HOMETASK

# #1234
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(nums)
# print('///')

# nums.append(6)
# print(nums)
# nums.pop(-1) #убрал 6 в конце
# print('///')

# print(len(nums))
# print('///')

# print(nums[0])
# print('///')

# print(nums[-1])
# print('///')

# nums.pop(0)
# for i in nums:
#         print(i)
# print('///')

# nums.insert(3, 10)
# print(nums)
# print('///')

# nums.pop(4)
# print('///')

# for i in nums:
#         if i==5:
#             print(True)
#         break
# print('///')

# #11
import random
# num1 = [] #пустой список для рандома
# n = 10
# for _ in range(n):
#     num1.append(random.randint(1, 100))
# print(f'список num1 = {num1}') #список заполнен 10 рандомными значениями в промежутке 1-100

# num2 = []
# for i in num1:
#       if i%2==0:
#             num2.append(i)
# num2.sort()
# print(num2)
# print('///')

#12
numbers = []
# Заполняем список 5 случайными числами от 1 до 10
i = 0
while i < 5:
    numbers.append(random.randint(1, 10))
    i += 1 
# Создаем новый список, содержащий квадраты чисел из первого списка
numbers2 = []
for n in numbers:
    numbers2.append(n*n)
numbers.sort()
numbers2.sort()
print(f'numbers = {numbers}')
print(f'numbers2 = {numbers2}')
print('///')

#13
numbers = numbers
numbers2 = numbers2
combo_list = []

for i in numbers:
     numbers2.append(i)
for o in numbers2:
     combo_list.append(o)
print(combo_list)

#14
combo_list.sort()
print(combo_list)

#15
combo_list.reverse()
print(combo_list)

#16
combo_list = combo_list
copy = []
for i in combo_list:
     copy.append(i)
print(f'copied list: {copy}')

#17
a = 0
copy = copy

for i in copy:
     if i==2:
          a = a+1
print(a)

#18
copy = copy
copy.clear()
print(copy)

#19-20
names=['alice', 'bob', 'charlie']
num = [] #пустой список для рандома
combo = [] #ну новый список для комбо
n = 5
for _ in range(n):
    num.append(random.randint(1, 100))
print(f'список num1 = {num}') #список заполнен 10 рандомными значениями в промежутке 1-100

for a in names:
     num.append(a)
print(f'новый список - {num}')

for i in num:
    combo.append(i)

print(f'комбо список - {combo}')

print('that\'s the end')