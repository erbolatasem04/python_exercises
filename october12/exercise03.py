'''
Ввод данных осуществляется из консоли путем использования функции input().
Вывод результатов необходимо делать в консоль

2. Периметр прямоугольника. Запроси длину и ширину, выведи 2 * (a + b).
3. Среднее из трёх. Три числа вводятся с консоли.
4. Часы и минуты. Дано число минут (например, 135). Выведи, сколько это часов и минут (// и %).
5. Округление. Запроси число, выведи его round(x, 2) и abs(x).
6. Максимум из двух. Через max(a, b).
6a. Максимум из трех. Через max().
7. Степень. Запроси число и степень, выведи x ** n.

'''

length_str = input('Please input width (int):')

try:
    length = int(length_str)
    width_str = input('Please input length (int):')
    try:
        width = int(width_str)
        area = 2 * length + width
        print(f'Area of the rectangle is {area}')
    except ValueError as e:
        print('sorry,number 2 is not an integer! Please try again!')
except ValueError as e:
    print('sorry this is not an integer! Please try again!')

#print(f'You entered number {number1}')