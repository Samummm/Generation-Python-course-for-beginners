# Следующее и предыдущее
#
# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
#
# Формат входных данных
# На вход программе подаётся целое число.
#
# Формат выходных данных
# Программа должна вывести текст согласно условию задачи.

# put your python code here
a = int(input())
print("Следующее за числом", a, "число:", a+1)
print("Для числа", a, "предыдущее число:", a-1)