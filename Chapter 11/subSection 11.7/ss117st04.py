# Next Prime 🌶️🌶️
#
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое
# простое число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
#
# Примечание 2. Следующий программный код:
#
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))
#
# должен выводить:
#
# 7
# 11
# 17

# put your python code here
def get_next_prime(num):
    end = num + 1
    if end == 2 : return 2
    while (True) :
        for i in range(2, end) :
            if end%i == 0 : break
        else : return end
        end += 1

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))