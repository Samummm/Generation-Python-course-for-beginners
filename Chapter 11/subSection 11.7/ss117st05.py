# Good password 🌶️
#
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
#     его длина не менее 8 символов;
#     он содержит как минимум одну заглавную букву (верхний регистр);
#     он содержит как минимум одну строчную букву (нижний регистр);
#     он содержит хотя бы одну цифру.
#
# Примечание. Следующий программный код:
#
# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
#
# должен выводить:
#
# True
# False

# put your python code here
def is_password_good(password):
    if len(password) < 8: return False
    tr1, tr2, tr3 = False, False, False
    for c in password:
        if not (tr1) and c.isupper(): tr1 = True
        if not (tr2) and c.islower(): tr2 = True
        if not (tr3) and c.isdigit(): tr3 = True
        if tr1 and tr2 and tr3: return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))