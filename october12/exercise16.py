'''
Проверка. Является ли введённая строка числом? → s.isdigit(). Ввод строки произвести с консоли
'''


word_str = input('write something ;')
s = word_str
if s.isdigit():
    print(' eto chislo')
else:
    print('eto ne chislo')