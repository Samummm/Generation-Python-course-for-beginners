# Диаграмма
#
# На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.
#
# Формат выходных данных
# Программа должна вывести столбчатую диаграмму.

# put your python code here
n = input().split()
for x in n :
    print("+"*int(x))