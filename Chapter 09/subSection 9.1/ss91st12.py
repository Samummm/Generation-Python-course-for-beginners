# Сколько раз?
#
# На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Программа должна вывести сколько раз встречаются символы  + и * в строке.

# put your python code here
s = input()
cZ = 0
cV = 0
for c in s :
    if c == '*' : cZ +=1
    if c == '+' : cV +=1
print("Символ + встречается", cV, "раз")
print("Символ * встречается", cZ, "раз")