# #1
# my_dict = {'apple':'alma', 'banana':'banan','cherry':'shiye'}
# my_dict.pop('banana')
# print(my_dict)

# #2
# my_dict = {'apple':'alma', 'banana':'banan','cherry':'shiye'}
# dict = {'pineapple':'ananas','watermelon':'garbiz'}
# my_dict.update(dict)
# print(my_dict)

# #3
# my_dict = {'apple':'alma', 'banana':'banan','cherry':'shiye'}

# print(my_dict)

# # #4
# # my_dict = {'apple':'alma', 'banana':'banan','cherry':'shiye'}
# # key = input('type key word: ')
# # value = input('type value word: ')
# # my_dict[key]=value
# # print(my_dict)

# #5

# # my_dict = [1,2,4, 5,3,32, 2,3,2,4,2,5,6]
# # count_dict = {}
# # max = 0
# # num = 0
# # for i in my_dict:
# #     if i < max:


# #6
# my_dict = {'a':'ankara', 'b':'berlin', 'c':'capital'}
# value = my_dict.pop('b')
# print(value)

# #7
# my_dict = {'apple':'alma', 'banana':'banan','cherry':'shiye'}
# key = input('type key word: ')
# value = input('type new value word: ')
# if key in my_dict:
#     my_dict[key]=value
#     print('passed)')
# else:
#     print(f'not found {key}')
# print(my_dict)

# #8
# dict1 = {'apple':'alma', 'banana':'banan','cherry':'shiye'}
# dict2 = {'apple':'яблоко','potato':'kartofel'}
# if dict2 in dict1:
#     dict1.update(dict2)
# else:
#     print('not matched!') 

# #9
# my_dict = {'azamrtbv':'123'}
# user = input('password:')
# if user in my_dict:
#     my_dict.pop(user)
#     print('succesfully deleted!')
# else:
#     print('password is not correct!')

# #10
# my_dict = {}
# age = int(input('type your age: '))
# if age>=18:
#     my_dict.update({'new_key':'adult'})
#     print('added!')
# else:
#     print('not added!')
# print(my_dict)


data = {}
name = input('type your name: ')
age = int(input('type your age: '))
if age>=18:
    data[name]='adult'
    print('added!')
else:
    data[name]='child'
    print('added but as child!')