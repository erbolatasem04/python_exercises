'''
Оценка по баллу. >= 90 -> 5, >= 75 -> 4, >= 50 -> 3, иначе 2. Баллы вводятся с консоли
'''

n_str = input('Введите целое число (int):')

try:
    n = int(n_str)
except ValueError as e:
    print('sorry this is not an integer! Please try again!')
    exit(0)

if n >=90:
    print('5')
elif n >= 75:
    print('4')
elif n>= 50:
    print('3')
else:
    print('2')