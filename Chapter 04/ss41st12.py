# Только + 🌶️
#
# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
#
# Формат входных данных
# На вход программе подаются три целых числа.
#
# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.
#
# Примечание. Если положительных чисел нет, то следует вывести 00.

# put your python code here
a, b, c = int(input()), int(input()), int(input())
count = 0
if (a > 0):
    count = count + a
if (b > 0):
    count = count + b
if (c > 0):
    count = count + c
print(count)