# def num(a):
#     print('sup', a)

# for i in range(4):
#     a = input('name - ')
#     num(a)


# user = input('text - ')
# def ceck(a):
#     if user.lower()==user:
#         print(f'{a} написан мелкими')
#     if user.upper()==user:
#         print(f'{a} написан большими ')
# ceck(a=user)

names = ['aza', 'alish', 'indi', 'malika']
def length():
    for i in names:
        print(f'{i} - {len(i)} harip')
length()    

print('\n')

file = open(file='file1.txt', mode='r')
copy = file.read()
def file_read():
    print(copy)
file_read()






