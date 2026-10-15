'''
Положительное/отрицательное/ноль. Три ветки через elif. Анализируемое число x вводится с консоли
'''

i = input('Введите целое число (int):')

try:
    i = int(i)
except ValueError as e:
    print('sorry this is not an integer! Please try again!')
    exit(0)


if i > 0:
    print('Положительное')
elif i < 0:
    print("Отрицательное")
else:
    print('Ноль')
