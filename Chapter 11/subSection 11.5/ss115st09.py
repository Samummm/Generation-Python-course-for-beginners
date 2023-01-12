# Количество совпадающих пар
#
# На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести одно число – количество пар элементов, равных друг другу.

# put your python code here
s = input().split()
sm = 0
while (len(s) > 0) :
    i = 0
    tmp = s[i]
    count = 1
    del s[i]
    while (len(s) > i) :
        if tmp == s[i] :
            count += 1
            del s[i]
        else : i += 1
    if count > 1 : sm += count * (count - 1) / 2
print(int(sm))