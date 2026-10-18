'''
1. Сумма двух чисел. Запроси два числа через input(), выведи сумму.
'''

number_str = input('Введите целое число (int):')

try:
    number = int(number_str)
    number2_str = input('Введите целое число 2 (int):')
    try:
        number2 = int(number2_str)
        sum = number + number2
        print(f'sum of number1: {number} and number2: {number2} is {sum}')
    except ValueError as e:
        print('sorry number2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry number1 is not an integer! Please try again!')


