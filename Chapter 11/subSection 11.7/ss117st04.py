# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк
# исходного списка.

# put your python code here
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
            'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(c) for c in keywords]

print(lengths)