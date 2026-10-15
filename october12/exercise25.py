'''
Логические операторы. Число в диапазоне 0 < x < 20.
Число ввести с коносли. Вывод строка в консоль - "число N в диапазоне 1-19" или "число N не в диапазоне 1-19"
'''

i = input('Введите целое число (int):')

try:
    i = int(i)
except ValueError as e:
    print('sorry this is not an integer! Please try again!')
    exit(0)


if 0<i<20:
    print('chislo v diapazone 1-19')
else:
    print('cgislo ne v diapazone 1-19')
