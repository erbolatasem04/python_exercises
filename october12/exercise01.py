'''
1. Сумма двух чисел. Запроси два числа через input(), выведи сумму.
'''

    number_str = input('Введите целое число (int):')

    try:
        number = int(number_str)
    except ValueError as e:
        print('sorry this is not an integer! Please try again!')
        number = None

    print(f'You entered number {number}')