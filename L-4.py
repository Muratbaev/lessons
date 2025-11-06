#                           TEST
# code for result-chart

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
    {"1": "B", "2": "B", "3": "D", "4": "A", "5": "B", "6": "C", "7": "B", "8": "A", "9": "B", "10": "A"}
]
rows = [
    data[0]
]
rows += [(k, v) for k, v in data[1].items()]
print(pretty_table(rows))


#                           PRACTICAL WORKS (DOC1)
#1 Преобразуй строку 'tAshKeNt' так, чтобы первая буква была заглавной, остальные — строчные.

word = "tAshKeNt"
low = word.lower()
cap = low.capitalize()
print(cap)

#2.	Преврати строку 'Hello World!' в 'hELLO wORLD!'.

word = "Hello World!"
print(word.swapcase())

#3.	Подсчитай, сколько раз встречается символ '!' в строке 'Hi! How are you!? Fine! Cool!'.
word = "Hi! How are you!? Fine! Cool!"
print(word.count("!"))

#4.	Замени слово 'bad' на 'good' в строке 'This is a bad day'.
word="This is a bad day"
swap = word.replace("bad", "good")
print(swap)

#5.	Удали все символы '!@#$' с начала и конца строки '!@#Hi there#$@!'.
word="!@#Hi there#$@!"
print(word.strip('!@#$'))

#6.	Сделай строку 'MY NAME IS ALI' полностью в нижнем регистре.
word = "MY NAME IS ALI"
print(word.lower())

#7.	Преобразуй 'python programming' так, чтобы каждое слово начиналось с заглавной буквы.
word = "python programming"
print(word.title())

#8.	Удали лишние символы '_' и '!' из строки '__Hello!__' и сделай первую букву заглавной.
word = "__Hello!__"
print(word.strip("_!"))

#9.	Выведи длину строки 'Abc123!@#'.
word = "Abc123!@#"
a = word.index("#")
print(a + 1)

#10.	Замени все буквы 'a' на '@' в строке 'Salam aleikum'.
word = "Salam aleikum"
print(word.replace("a", "@"))

#                           10 open questionS (DOC2)
#1.	Что такое тип данных string и зачем он нужен?
#хранение и обработка текста
# 2.	В чём разница между методами upper() и lower()?
#upper = capslock/lower = все маленькие буквы
# 3.	Что делает метод title()?
#каждое слово с большой буквы
# 4.	Объясни, как работает метод replace().
#замена заданных символов на новые заданные символы
# 5.	Когда стоит использовать метод strip()?
#для удаления символов вначале и в конце строки
# 6.	Что вернёт len('Python123!') и почему?
#вернет 10 потому считает количество символов
# 7.	Чем отличаются capitalize() и title()?
#capitalize() - только первая буква в строке на заглавную а остальные мелкие, 
#title() - первая буква каждого слова с заглавного
# 8.	Как удалить ненужные символы из строки?
#используя strip()
# 9.	Как посчитать, сколько раз символ встречается в строке?
#использовать count()
# 10.	Объясни на примере, как работает метод swapcase().
#меняет в тексте заглавные на прописные и также наоборот например
a = "i lOVE cATS"
print(a.swapcase())

#                           DOC2 EXERCISES

#11
text = input("your text here --> ")
print(text.lower())

#12
text = input("your text here --> ")
print(text.upper())

#13
text = input("your text here --> ")
print(text.swapcase())

#14
text = input("your text here --> ")
print(text.capitalize())

#15
text = input("your text here --> ")
print(text.title())

#16
text = input("your text here --> ")
count = input("search symbol--> ")
print(text.index(count))

#17
text = input("your text here --> ")
count = input("search symbol--> ")
print(text.rindex(count))

#18
text = input("your text here --> ")
print(text.strip(" "))

#19
text = input("your text--> ")
ask = input("what replace--> ")
replace = input("replace to what--> ")
print(text.replace(ask, replace))

#20
text = input("your text: ")
start = int(input("type start index: "))
end = int(input("type last index: "))
cutted = text[start:end+1]
print("cutted result: ", cutted)


print('that\'s the end')