# BEEGEEK
#
# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет
# от математики, то он решил:
#
#     число a – должно быть палиндромом;
#     число b – должно быть простым;
#     число c – должно быть четным.
#
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
#
# Примечание. Следующий программный код:
#
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))
#
# должен выводить:
#
# True
# False
# False
# False

# put your python code here
def is_valid_password(password):
    s = password.split(':')
    n = int(s[1])
    s1 = s[0]
    if s1 != s1[::-1] or len(s) > 3: return False
    for i in range(2, n) :
        if n%i == 0 : return False
    if int(s[2])%2 != 0 or n == 1 : return False
    return True

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))