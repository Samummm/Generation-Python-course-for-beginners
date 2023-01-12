# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел палиндромов от 100 до 1000.

# put your python code here
palindromes = [ x for x in range(100, 1000) if str(x) == str(x)[::-1]]

print(palindromes)