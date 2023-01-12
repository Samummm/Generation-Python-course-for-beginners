# Сумма цифр
#
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

# put your python code here
def print_digit_sum(num):
    sum = 0
    if num > 9 :
        while (num > 0) :
            sum += num%10
            num //= 10
    else : sum = num
    print(sum)
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)