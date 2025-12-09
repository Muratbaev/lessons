#list part2

#list part 2


#append,insert,extend
#pop,remove
#sort,reverse

# #iteraciya
# nums = []
# for i in range(1,10+1):

#     nums.append(i)
# print(nums)
# #generaciya
# nums2 = [ i for i in range(1,10+1)]
# print(nums2)


# nums = []
# for i in range(1,10+1):
#     if i%2==0 :
    
#         nums.append(i)
# print(nums)


# nums2 = [ i for i in range(1,10+1) if i%2==0]#[i if i%2==0 else i**2 for in in range(...) ]
# print(nums2)



# big_bag = ['laptop',['telephone','airpods',['money','cards','coins','id card','keys'],'charger'],'mouse','headphones','book']

# # print(big_bag[0])
# print(big_bag[1][2][-1])
# print(big_bag[2])



#classwork

#1
gan = [i for i in range(1, 11)]
print(gan)

#2
gan = []
for i in range(1, 11):
    gan.append(i)
print(gan)

#3
a = [1,2,3,['hello','Python',[3.5,['hello world']],[8,9,10,[11,12,13,'name']]]] 
print(a[3][3][3][3])

#4
kvad = [i**2 for i in range(1, 11)]
print(kvad)

#5
import random

num1 = [] #пустой список для рандома
n = 10
for _ in range(n):
    num1.append(random.randint(1, 100))
num1.sort()
print(f'список num1 = {num1}')
a = num1.__len__()
print(f'наибольшее число - {num1[-1]}, его индекс - {a}')

#6
kvad = []
for i in range(1, 11):
    i = i**2
    kvad.append(i)
print(kvad)

#               DOC2
#1-3
list1 = []
list1.append('name')
list2 = ['surname']
list2.extend(list1)
#4-6
names = ['gordon', 'hensy', 'volodya', 'jumabay']
names.pop(3) #delete object by index
names.remove('volodya') #delete object by value
names.insert(3, 'muxa') #add muxa to coords 3

#7
nums = []
for i in range(1, 11):
    nums.append(i)
nums.clear()
#8
for i in range(50, 101):
    if i%5==0:
        nums.append(i)
print(nums)


