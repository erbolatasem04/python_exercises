'''
Деление на ноль. a / b в try, при ZeroDivisionError — «На ноль делить нельзя».
'''

number1_str = input('Please input integer number 1(int):')

try:
    number1 = int(number1_str)
    number2_str = input('Please input integer number 2(int):')
    try:
        number2 = int(number2_str)
        number3 = number1/number2
        print(f'esli delit {number1} na {number2} vyidet {number3}')
    except ZeroDivisionError:
        print("dont devision to zero!")
    except ValueError as e:
        print('sorry,number 2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry number 1 is not an integer! Please try again!')


