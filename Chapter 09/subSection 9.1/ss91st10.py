# Цифра 1
#
# На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
#
# Формат входных данных
# На вход программе подается одна строка состоящая из цифр.
#
# Формат выходных данных
# Программа должна вывести сумму цифр данной строки.

# put your python code here
ns = input()
sm = 0
for c in ns :
    sm += int(c)
print(sm)