#list -  список - dizim
#set - набор(множество) -  koplik
#tuple -  кортеж - izbe-izlik
#dictionary - словарь  - sozlik

fridge = ['meat','bread','eggs','butter','milk']
fridge.append('Cola')#добавление в конец Cola

fridge.insert(-1,'Shashlik') #добавлние в координату -1 Shashlik
from_bazar = ['Apple','Pineapple','Bananas','Cherry']
# fridge.append(from_bazar) append не добавляет только объект в список (не список) 
fridge.extend(from_bazar) #объединение списков
products = ['john','bread','banana','iphone']
products.pop(0) #удаление из списка ПО ИНДЕКСУ
products.remove('iphone') #удаление из списка ПО ЗНАЧЕНИЮ




