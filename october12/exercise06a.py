'''

3. Среднее из трёх. Три числа вводятся с консоли.

'''

number1_str = input('Please input integer number 1(int):')

try:
    number1 = int(number1_str)
    number2_str = input('Please input integer number 2(int):')
    try:
        number2 = int(number2_str)
        number3_str = input('Please input integer number 3(int):')
        try:
            number3 = int(number3_str)
            max = max(number1, number2, number3)
        except ValueError as e:
            print('sorry, number 3 is not an integer!')
    except ValueError as e:
        print('sorry,number 2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry number 1 is not an integer! Please try again!')

print(f'number from {number1} to {number2} and {number3} is {max}')