# Звездная рамка
#
# На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n × 19.
#
# Формат входных данных
# На вход программе подаётся натуральное число n ∈ [3; 19] — высота звездной рамки.
#
# Формат выходных данных
# Программа должна вывести звездную рамку размерами n × 19.
#
# Подсказка. Для печати звездной линии используйте умножение строки на число.

# put your python code here
n = int(input())
print("*"*19)
for _ in range(n-2) :
    print("*", " "*17, "*", sep = "")
print("*"*19)