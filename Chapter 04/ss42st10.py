# Принадлежность 3
#
# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.
#
# Формат входных данных
# На вход программе подаётся целое число x.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается.

# put your python code here
n = int(input())
if ((-30 < n <= -2) or (7 < n <= 25)):
    print("Принадлежит")
else:
    print("Не принадлежит")