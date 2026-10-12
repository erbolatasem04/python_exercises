'''
Ввод данных осуществляется из консоли путем использования функции input().
Вывод результатов необходимо делать в консоль

1. Сумма двух чисел. Запроси два числа через input(), выведи сумму.
2. Периметр прямоугольника. Запроси длину и ширину, выведи 2 * (a + b).
3. Среднее из трёх. Три числа вводятся с консоли.
4. Часы и минуты. Дано число минут (например, 135). Выведи, сколько это часов и минут (// и %).
5. Округление. Запроси число, выведи его round(x, 2) и abs(x).
6. Максимум из двух. Через max(a, b).
6a. Максимум из трех. Через max().
7. Степень. Запроси число и степень, выведи x ** n.

'''

number1_str = input('Please input integer number (int):')

try:
    number1 = int(number1_str)
    number2_str = input('Please input another number (int):')
    try:
        number2 = int(number2_str)
        number_sum = number1 + number2
        print(f'sum of {number1} and {number2} = {number_sum}')
    except ValueError as e:
        print('sorry,number 2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry this is not an integer! Please try again!')

#print(f'You entered number {number1}')