# В одну строку 1
#
# На вход программе подается строка текста, содержащая слова. Напишите программу, которая выводит слова введенной строки в столбик.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая слова, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Программу можно написать в одну строку кода.

# put your python code here
print(*[c for c in input().split()], sep = '\n')