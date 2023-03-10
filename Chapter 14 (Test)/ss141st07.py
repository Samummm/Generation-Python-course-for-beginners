# Число словами 🌶️
#
# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его
# словесное описание на русском языке.
#
# Примечание 1. Считайте, что число 1 ≤ num ≤ 99 .
#
# Примечание 2. Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
#
# должен выводить:
#
# семь
# восемьдесят пять

# put your python code here
# объявление функции
def number_to_words(num):
    ed = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    des1 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    des = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    if num < 10 : return ed[num-1]
    if num%10 == 0 : return des[num//10 - 1]
    if 10 < num < 20 : return des1[num%10-1]
    if 20 < num < 100 : return des[num//10-1]+" "+ed[num%10-1]
# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))