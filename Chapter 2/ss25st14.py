# Перестановка цифр
#
# Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел,
# образованных при перестановке цифр заданного числа.
#
# Формат входных данных
# На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.
#
# Формат выходных данных
# Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
# abc,acb,bac,bca,cab,cba.

# put your python code here
n = int(input())
a = n // 100
b = n % 100 // 10
c = n % 10
print(n , a*100+c*10+b, b*100+a*10+c, b*100+c*10+a, c*100+a*10+b, c*100+b*10+a, sep = '\n')
