# Remove outliers
#
# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
#
# На вход программе подается натуральное число n, а затем n различных натуральных чисел. Напишите программу, которая удаляет
# наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# put your python code here
n = int(input())
ln = []
for _ in range(n) : ln.append(int(input()))
for i in range(len(ln)) :
    if (ln[i] == min(ln)) :
        del ln[i]
        break
for i in range(len(ln)) :
    if (ln[i] == max(ln)) :
        del ln[i]
        break
for x in ln : print(x)