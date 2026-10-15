'''
Максимум из двух через if/else (без max). Оба числа вводятся с консоли
'''

n1_str = input('Please input integer number 1(int):')

try:
    n1 = int(n1_str)
    n2_str = input('Please input integer number 2(int):')
    try:
        n2 = int(n2_str)
    except ValueError as e:
        print('sorry,number 2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry number 1 is not an integer! Please try again!')

if n1 > n2 :
    print('max')
else:
    print('min')
