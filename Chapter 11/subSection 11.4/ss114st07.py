# Google search - 2 🌶️🌶️
#
# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
#
# Формат входных данных
# На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве, затем число k,
# затем сами поисковые запросы.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.

# put your python code here
n = int(input())
ln = []
for _ in range(n) : ln.append(input())
z = int(input())
zp = []
for _ in range(z) : zp.append(input())
for c in ln :
    for s in zp :
        if s.lower() not in c.lower() :
            break
    else : print(c)