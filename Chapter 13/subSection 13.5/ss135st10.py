# Змеиный регистр
#
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».
#
# Примечание 1. Почитать подробнее о стилях именования можно тут.
#
# Примечание 2. Следующий программный код:
#
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
#
# должен выводить:
#
# this_is_camel_cased
# is_prime_number

# put your python code here
def convert_to_python_case(text):
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = []
    for i in range(1, len(text)) :
        if text[i] in eng : n.append(i)
    count = 0
    s = []
    s.extend(text)
    for x in n :
        s.insert(x + count, '_')
        count += 1
    st = ''.join(s)
    return st.lower()

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))