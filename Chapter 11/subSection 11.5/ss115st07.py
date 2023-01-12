# Корректный ip-адрес
#
# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу, которая определяет
# является ли введенная строка текста корректным ip-адресом.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
#
# Формат выходных данных
# Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.
#
# Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.

# put your python code here
n = input().split(".")
for x in n :
    if not (0 <= int(x) <= 255) :
        print("НЕТ")
        break
else : print("ДА")