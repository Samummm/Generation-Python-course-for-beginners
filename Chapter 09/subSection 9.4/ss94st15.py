# Удаление фрагмента
#
# На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите программу, которая
# удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# put your python code here
s = input()
print(s[:s.find('h')], s[s.rfind('h')+1:], sep = '')