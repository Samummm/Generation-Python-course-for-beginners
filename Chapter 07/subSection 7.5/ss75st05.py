# Обратный порядок 2
#
# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести число, записанное в обратном порядке.

# put your python code here
n = int(input())
s = ""
while (n != 0) :
    s += str(n%10)
    n = n // 10
print(s)