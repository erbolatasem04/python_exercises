'''

2. Периметр прямоугольника. Запроси длину и ширину, выведи 2 * (a + b).

'''

length_str = input('Please input integer number (int):')

try:
    length_str = int(length_str)
    width_str = input('Please input another number (int):')
    try:
        width_str = int(width_str)
        perimeter = 2* (length_str + width_str)
        print(f'perimeter of a rectangle {perimeter}.')
    except ValueError as e:
        print('sorry,width is not an integer! Please try again!')
except ValueError as e:
    print('sorry length not an integer! Please try again!')

