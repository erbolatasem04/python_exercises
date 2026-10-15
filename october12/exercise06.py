'''
Максимум из двух. Через max(a, b)
'''

number1_str = input('Please input integer number 1(int):')

try:
    number1 = int(number1_str)
    number2_str = input('Please input integer number 2(int):')
    try:
        number2 = int(number2_str)
        max = max(number1, number2)
    except ValueError as e:
        print('sorry,number 2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry number 1 is not an integer! Please try again!')

print(f'max number from {number1} to {number2} is: {max}')