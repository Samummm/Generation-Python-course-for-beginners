# Взлом Братства Стали 🌶️
#
# Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали, и любезно соглашается
# помочь им в решении их проблем. Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде
# появления комментариев к программам на терминалах Братства Стали. Известно, что программисты Братства никогда не оставляют
# комментарии к коду, и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. Помогите писцу
# Ибсену удалить все комментарии из программы.
#
# Формат входных данных
# На первой строке вводится символ решётки и сразу же натуральное число n — количество строк в программе, не считая первой.
# Далее следует n строк кода.
#
# Формат выходных данных
# Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк. Пустую строку вместо
# первой строки ввода выводить не надо.

# put your python code here
n = int(input()[1:])
s = []
for _ in range(n) :
    tmp = input()
    fn = tmp.find('#')
    if fn != -1 : s.append(tmp[:fn].rstrip())
    else : s.append(tmp.rstrip())
for c in s : print(c)