# Google search - 1
#
# На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос. Напишите программу,
# которая выводит все введенные строки, в которых встречается поисковый запрос.
#
# Формат входных данных
# На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве,
# затем один поисковый запрос.
#
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречается поисковый запрос.
#
# Примечание. Поиск не должен быть чувствителен к регистру символов.

# put your python code here
n = int(input())
ln = []
for _ in range(n) : ln.append(input())
s = input()
for c in ln :
    if s.lower() in c.lower() : print(c)