# Последовательность чисел 2 🌶️
#
# Даны два целых числа m и n. Напишите программу, которая выводит все числа от mm до nn включительно в порядке возрастания,
# если m < n, или в порядке убывания в противном случае.
#
# Формат входных данных
# На вход программе подаются два целых числа mm и nn, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести числа в соответствии с условием задачи.

# put your python code here
n, m = int(input()), int(input())
if (n < m) :
    k = 1
    m += 1
else :
    k = -1
    m -= 1
for i in range (n, m, k) :
    print(i)