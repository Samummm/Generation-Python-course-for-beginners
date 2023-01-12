# Панграммы
#
# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов,
# чтобы можно было в одной фразе рассмотреть все глифы.
#
# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и возвращает
# значение True если текст является панграммой и False в противном случае.
#
# Примечание 1. Гарантируется, что введенная строка содержит только буквы английского алфавита.
#
# Примечание 2. Следующий программный код:
#
# print(is_pangram('Jackdaws love my big sphinx of quartz'))
# print(is_pangram('The jay pig fox zebra and my wolves quack'))
# print(is_pangram('Hello world'))
#
# должен выводить:
#
# True
# True
# False

# put your python code here
# объявление функции
def is_pangram(text):
    en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = text.lower()
    for c in en :
        if c not in s : return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))