'''
3. Угадай число с рекордами
(random, while, try/except, file)

Программа:

Читает best.txt (там хранится лучший результат в попытках). Если файла нет — лучший = бесконечность.

Компьютер загадывает число 1–100 через random.randint.
В цикле while True спрашивает угадывание:
try/except для числа
подсказки «больше» / «меньше»
считает попытки
при победе — break
Если новое число попыток меньше сохранённого — обновить best.txt.
Вывести: «Ты угадал за N попыток. Рекорд: M».

Тренирует: random + while + try/except + файлы + if.
Бонус: добавь отказ от игры, если введено "stop" (через break).

'''

try:
    f = open('best.txt', 'r')
    best_record = int(f.read())
except:
    best_record = float('inf')

import random
number = random.randint(1,100)

attemps = 0
while True:
    number1 = input('Введите случайное число:')
    try:
        number1 = int(number1)
        attemps +=1
    except ValueError:
        print('введите число!')
        continue
    if number1 < number:
        print('больше')
    elif number1 > number:
        print('меньше')
    else:
        print('победа')
        if attemps < best_record:
            l = open('best.txt','w')
            l.write(str(attemps))
            best_record = attemps
            l.close()
        print(f'Ты угадал за {attemps} попыток. Рекорд: {best_record}')
        break
