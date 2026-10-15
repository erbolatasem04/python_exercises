'''

4. Часы и минуты. Дано число минут (например, 135). Выведи, сколько это часов и минут (// и %).

'''


minutes = input('Введите целое число (int):')

try:
    minutes = int(minutes)
    hours = minutes // 60
    remaining_minutes = minutes % 60
except ValueError as e:
    print('sorry this is not an integer! Please try again!')
    number = None

print(f'in {minutes} minutes has {hours} hours , {remaining_minutes} minutes')
