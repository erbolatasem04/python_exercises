'''
Пароль. Если введённая строка равна "python" -> вывести в консоль - «доступ разрешён», иначе «отказ»
.Пароль. Если введённая строка равна "python" -> вывести в консоль - «доступ разрешён», иначе «отказ».
'''

p = input('write password:')

if p == 'python':
    print('dostup razreshen')
else:
    print('dostup zapreshen')