# До КОНЦА 2
#
# На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является
# слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит члены данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести члены данной последовательности.

# put your python code here
s = input()
while(s != "КОНЕЦ" and s != "конец") :
    print(s)
    s = input()