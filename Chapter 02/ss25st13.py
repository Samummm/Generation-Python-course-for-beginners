# Трехзначное число
#
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
#
# Формат входных данных
# На вход программе подаётся положительное трёхзначное число.
#
# Формат выходных данных
# Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.

# put your python code here
n = int(input())
print("Сумма цифр =", (n//100) + (n%10) + (n%100 //10))
print("Произведение цифр =", (n//100) * (n%10) * (n%100 //10))