# Сортировка чисел
#
# На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести две строки текста в соответствии с условием задачи.

# put your python code here
s = input().split()
n = []
for c in s : n.append(int(c))
n.sort()
print(*n)
n.sort(reverse = True)
print(*n)