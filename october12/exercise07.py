'''
Степень. Запроси число и степень, выведи x ** n.

'''


number1_str = input('Please input integer number 1(int):')

try:
    number1 = int(number1_str)
    number2_str = input('Please input integer number 2(int):')
    try:
        number2 = int(number2_str)
        result = number1 ** number2
    except ValueError as e:
        print('sorry,number 2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry number 1 is not an integer! Please try again!')

print(result)