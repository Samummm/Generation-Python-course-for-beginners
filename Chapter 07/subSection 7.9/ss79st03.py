# Делители-1 🌶️
#
# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное число
# из отрезка[a; b] с максимальной суммой делителей.
#
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и сумму его делителей.
#
# Примечание. Если таких чисел несколько, то выведите наибольшее из них.

# put your python code here
a, b = int(input()), int(input())
n = 0
endS = 0
for i in range(b, a-1, -1) :
    sm = 0
    for j in range(1, i+1) :
        if i%j == 0 :
            sm += j
    if endS < sm :
        endS = sm
        n = i
print(n, endS)