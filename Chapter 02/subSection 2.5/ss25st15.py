# Четырёхзначное число
#
# Напишите программу для нахождения цифр четырёхзначного числа.
#
# Формат входных данных
# На вход программе подаётся положительное четырёхзначное целое число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# put your python code here
n = int(input())
print("Цифра в позиции тысяч равна", n//1000)
print("Цифра в позиции сотен равна", n%1000//100)
print("Цифра в позиции десятков равна", n%100//10)
print("Цифра в позиции единиц равна", n%10)