
#set&tuple

# my_list = [1,2,3,4,'bes']#xolodilnik

# my_tuple = (1,2,3,4,'bes')#safe

# my_tuple[4]=5
# print(my_tuple[4])

#list,tuple, -> int()
#


# a = '5'
# b = '7'

# print(int(a)+int(b))#int - sanga otkeredi




#tuple - кортеж
# names = ('Rasul','Azamat','messi')

# new_names= list(names)

# print(new_names)
# new_names.remove('messi')
# print(tuple(new_names))


#set - множество/набор - koplik

# my_list = [1,2,2,4,6,5,4,3,2,4,4,3,3,3,5,4,3]
# my_set = {100,2,2,400,6,5,4,3,2,4,4,3,3,3,5,4,3}

# print(my_list)
# print(my_set)
# print(list(set(my_list)))

# my_set = set()# dict -{}
# names = []
# names = {'Azamat','Indira','Alisher','Nazira','Jamila'}
# print(names)

# my_set = {'Rasul','Alisher'}

# my_set.add('Azamat')
# print(my_set)
names = {'Messi','Rasul','Alisher','Neymar'}

# names.pop()
# print(names)

# names.remove('Messiasd')
# print(names)
# names.discard('Neymarasdas')
# print(names)
# user = input('jaz:')

#extend->update

#intersection,union,difference

# a = {1,4,6,8,3,12,7}
# b = {1,2,3,5,7,10,8}

# # print(a.difference(b))
# # print(b.difference(a))
# print(a.intersection(b))#пересечение
# # print(a.union(b))

# my_tuple = (1,2,4,6,7,7)
# for i in my_tuple:
#     print(i)

#
# text = 'rasul'#

# print(text.upper())
# print(text)


# nums = [12,35668,65]
# nums.sort()
# print(nums)
#

#HOMETASK1
#1
set1 = {'Rome', 'Tokio', 'Seoul', 'Moscow', 'Samarkand'}
set1.add('Tashkent')
print(set1)
#2
set1.remove('Samarkand')
print(set1)

#3
veg = {'tomato', 'carrot', 'potato'}
fru = {'peach', 'pear', 'cucumber'}
print(veg.intersection(fru))
#4
veg.update(fru)
print(veg)

#5
pa = {1, 3, 5, 7, 9}
ba = {2, 4, 6, 8, 10}
print(pa.union(ba))

#6
a = {1, 3, 5,3 ,2,34, 5 ,5}
b = {1, 3, 43, 5, 2, 3, 4,5}
print(a.difference(b))

#7
aa = {'kangaroo', 'jaguar', 'lion', 'wolf'}
for i in aa:
    print(i)

#8
days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
print(days[2])

#9
import random
a = (1, 2, 4, 5, 3)
for i in a:
    if i==5:
        print(True)
        break

#10
a = (1, 2, 4, 5, 3)
b = set(a)
print(b)


#HOMETASK 2
#1
a = [1, 2, 4, 1, 4, 2, 1, 1]
max = 0
num = 0
for i in a:
    if a.count(i)>max:
        max = a.count(i)
        num = i
print(num)


#11-12-13
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {10}
a.update(b)
print(a)

a.discard(7)
print(a)

a = [1, 2, 3 , 6,7 ,7, 8, 8,8 ,88, 5, 4, 3,45,7 ]
a.sort()
b = set(a)
print(b)

for i in a:
    if i==9:
        a.remove(i)
    else:
        a.append(9)
a.sort()
b = set(a)
print(b)

#15
set1 = set()
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
for i in set2:
    set1.add(i)
print(f'sss {set1}')

#17
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
a.pop()
print(a)

#18
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
a.clear()
print(a)

#19
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
b = [11, 22, 33, 44, 55, 66, 77, 88, 9]
c = list(a)
c.extend(b)
c.sort()
r = set(c)
print(r)

#20
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
b = {2, 4, 6, 8, 10}
print(a.intersection(b))

#21
a = (11, 22, 33, 44, 55, 66, 77, 88, 99, 0)
s = list(a)
s.sort()
t = tuple(s)
print(t)

#22
a = ('said', 'bobur')
b = ('slk', 'kllskdlsd;sakd;lask')
print(a+b)
#23
a = (11, 22, 33, 44, 55, 66, 77, 88, 99, 0)
b = a + (4,)
print(b)

#24
a = (11, 22, 33, 44, 55, 66, 77, 88, 99, 0)
b = a[:3] + (4,) + a[3:] #срезаем промежуток до индекса 3 и после 3
print(b)

#25
a = (11, 22, 33, 44, 55, 66, 77, 88, 99, 0)
b = a[:4] + a[4+1:]
print(b)

#26
a = (11, 22, 33, 44, 55, 66, 77, 88, 99, 0)
sorted = tuple(sorted(a))
print(sorted[0])
print(sorted[-1])

#27
d = (1, 2,3 ,4, 2, 7,5, 0, 4)
sorted = tuple(reversed(d))
print(sorted)

#28
a = (1, 3, 5, 7, 9)
b = (2, 4, 6, 8, 0)

new = tuple(a+b)
print(new)

#29??????

#30
a = (1, 4, 6, 3, 8, 5, 0)
object = 10
if object in a:
    print(f'объект {object} есть в кортеже')
else:
    print(f'объекта {object} нету в кортеже')


#HOMETASK 3

#1
a = [1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2]
b = a.count(1)
# for i in a:
#     if 

#2
a = {1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2}
b = {2, 2,4, 6, 7, 8,1, 2,1}
print(a.intersection(b))

#3
a = [1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2]
print(set(a))

#4
a = {1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2}
b = {2, 2,4, 6, 7, 8,1, 2,1}
c = {11, 23,4, 2,12, 1, 3, 5}
b.update(a)
b.update(c)
print(b)

#5
a = [2, 2,4, 6, 7, 8,1, 2,1]
b = []
for i in a:
    if i%2==0:
        b.append(i)
print(b)

#6
a = [2, 2,4, 6, 7, 8,1, 2,1]
a.sort()
print(a)

#8
a = [1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2]
b = [2, 2,4, 6, 7, 8,1, 2,1]
c = []
for i in a and b:
    if i in a and b:
        c.append(i)
print(c)

#9
a = [2, 2,4, 6, 7, 8,1, 2,1]
b = list(set(a))
print(b)

#10
a = (2, 2,4, 6, 7, 8,1, 2,1)
b = list(a)
b.sort()
print(b[0], b[-1])

#11
a = (1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2)
b = (2, 2,4, 6, 7, 8,1, 2,1)
aa = set(a)
bb = set(b)
print(aa.intersection(bb))

#13
a = (1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2)
b = (2, 2,4, 6, 7, 8,1, 2,1)
c = (12,13,11,35,24,87)
aaa = a+b+c
print(aaa)

#14
a = (1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2)

#15
a = {1, 2, 3, 2, 2, 4, 5, 1, 2, 3, 2}
b = {2, 2,4, 6, 7, 8,1, 2,1}
print(a.intersection(b))

#16






