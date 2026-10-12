'''
Ввести с консоли строку представляющую целое число с помощью функции input().
Произвести перевод данной строки в число с помощью функции явного приведения типов - int().
Функцию int() обрамить в try except - если введенная строка не является строковым представлением целого числа
 - то вывести в консоль сообщение "Это не число"
'''

number_str = input('Введите целое число (int):')

try:
    number = int(number_str)
except ValueError as e:
    print('sorry this is not an integer! Please try again!')
    number = None

print(f'You entered number {number}')