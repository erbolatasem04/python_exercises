'''
Округление. Запроси число, выведи его round(x, 2) и abs(x).
'''

number_str = input('Введите целое число (int):')

try:
    number = float(number_str)
    number_rounded = round(number, 2)
    number_abs_rounded = abs(number)
except ValueError as e:
    print('sorry this is not a float! Please try again!')
    number = None
    number_rounded = None
    number_abs_rounded = None

print(f'round of {number} is {number_rounded} and abs is {number_abs_rounded}')