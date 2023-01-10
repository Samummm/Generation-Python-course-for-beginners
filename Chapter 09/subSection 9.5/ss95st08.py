# Дополните приведенный код, используя форматирование строк с помощью f-строк, так чтобы он вывел текст:
#
# «In 2010, someone paid 10K Bitcoin for two pizzas.» (без кавычек).

# put your python code here
year = 2010
amount = '10K'
currency = 'Bitcoin'

print('In {}, someone paid {} {} for two pizzas.'.format(year, amount, currency))