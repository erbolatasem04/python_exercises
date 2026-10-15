'''
Совершеннолетний? Если возраст >= 18 → «взрослый», иначе «ребёнок». Возраст вводится с консоли
'''

n_str = input('Введите целое число (int):')

try:
    n = int(n_str)
except ValueError as e:
    print('sorry this is not an integer! Please try again!')
    exit(0)

if n >=18:
    print('adult')
else:
    print('kid')