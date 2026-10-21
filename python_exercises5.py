'''
1. Визитка
(input, f-strings, if)

Спроси имя, возраст, город. Выведи:

=== ВИЗИТКА ===
Имя: Аня
Возраст: 20
Город: Алматы
Статус: взрослый (если >= 18) или ребёнок
'''


name = input('Write name:')
age = input('Write age:')
city = input('Write city:')
print('=== ВИЗИТКА ===')
print(f'Имя: {name}')
print(f'Возраст: {age}')
print(f'Город: {city}')
try:
    age = int(age)
except ValueError:
    print('write int!')
if age >= 18:
    print("Cтатус взрослый")
else:
    print('Статус ребенок')



'''
2. работа со string
(slices, string methods)

Дано слово. Выведи:
слово целиком
перевёрнутое ([::-1])
первые 3 буквы
последние 3 буквы
слово в верхнем регистре
слово с заменой первой буквы на *

Пример для "python":

python
nohtyp
pyt
hon
PYTHON
*ython
'''
word = 'python'
print(word)
print(word[::-1])
print(word[:3])
print(word[3:])
print(word.upper())
print(word.replace('p','*'))


'''
3. Список цен
(list, append, len, sum)

Создай список цен на товары: [120, 80, 350, 45, 200].
Выведи:
- количество товаров (len)
- сумму (sum)
- самую дорогую покупку (max)
- самую дешёвую (min)
- среднее (sum / len)

'''
prices = [120, 80, 350, 45, 200]
print(len(prices))
print(sum(prices))
print(max(prices))
print(min(prices))
s = sum(prices) / len(prices)
print(s)

'''
4. Телефонная книга-мини
(dict, get, in)
дан словарь:

phonebook = {
    "Аня": "+7-701-111-22-33",
    "Сауле": "+7-702-444-55-66",
}

Выведи номер Ани через [ ].
Проверь, есть ли Вера (in).
Попробуй вывести Веру через [ ] — поймай KeyError через try/except.
Выведи Веру через .get("Вера", "нет номера").

'''

phonebook = {
    "Аня": "+7-701-111-22-33",
    "Сауле": "+7-702-444-55-66",
}
print(phonebook['Аня'])
if 'Вера' in phonebook:
    print('True')
else:
    print('False')
try:
    print(phonebook['Вера'])
except KeyError:
    print('такого номера нет')
phonebook.get("Вера", "нет номера")

'''
5. Уникальные гости
(set, list, set())
Дан список гостей с повторами:
guests = ["Аня", "Борис", "Аня", "Сауле", "Борис", "Аня", "Жулдыз"]

Выведи всех уникальных через set(guests).
Выведи количество уникальных.
Выведи количество всего (len).

'''
guests = ["Аня", "Борис", "Аня", "Сауле", "Борис", "Аня", "Жулдыз"]
unique_guests = set(guests)
print(unique_guests)
print(len(unique_guests))
print(len(guests))


'''
6. Нумерация меню
(enumerate, for)

menu = ["Плов", "Лагман", "Манты", "Шашлык"]
Выведи с номерами начиная с 1:

1. Плов
2. Лагман
3. Манты
4. Шашлык
'''
menu = ["Плов", "Лагман", "Манты", "Шашлык"]
for i,foods in enumerate(menu, start = 1):
    print(i, foods)

'''
7. Имена и оценки
(zip, list, for)

names = ["Аня", "Борис", "Вера"]
grades = [5, 3, 4]

Выведи:

Аня - 5
Борис - 3
Вера - 4

Потом создай dict(zip(names, grades)) и выведи его.

'''
names = ["Аня", "Борис", "Вера"]
grades = [5, 3, 4]
for name,grade in zip(names, grades):
    print(name, grade)
d = dict(zip(names, grades))
print(d)


'''
8. Безопасный калькулятор
создай калькулятор для следующих операций + - / *.
Принимает с консоли через input() 2 целых числа. Необходимо обеспечить обработку возможных исключений при операциях 
int() и делении на ноль

'''

try:
    num1 = int(input('Введите 1 число: '))
    num2 = int(input('Введите 2 число: '))

    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2

    print(f'Сложение: {add}')
    print(f'Вычитание: {sub}')
    print(f'Умножение: {mult}')

    try:
        div = num1 / num2
        print(f'Деление: {div}')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

except ValueError:
    print('Ошибка! Введите целые числа.')


'''
9. Заметка в файл
(file write, file read, close)

Спроси у пользователя заметку.
Открой notes.txt в режиме "a", запиши строку с \n, закрой.
Открой notes.txt в режиме "r", прочитай всё, выведи.

Запусти 2–3 раза — заметки должны накапливаться.

'''
note = input('Write something:')
my_file = open('notes.txt','a')
my_file.write(note + '\n')
my_file.close()
my_file = open('notes.txt','r')
b = my_file.read()
my_file.close()
print(b)