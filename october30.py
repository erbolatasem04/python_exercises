# int          Целое число  42, -10
# float      Число с плавающей точкой  3.14, -0.5
# bool      Логическое значение  True, False

# str          Строка  "Привет"
# list      Список  [1, 2, 3]
# tuple      Кортеж  (1, 2, 3)
# range      Последовательность целых чисел  range(5)
# dict      Словарь: пары «ключ — значение»  {"имя": "Анна", "возраст": 25}
# set          Множество уникальных элементов  {1, 2, 3}
# frozenset  Неизменяемое множество  frozenset({1, 2, 3})

## complex      Комплексное число  2 + 3j
# bytes      Неизменяемая последовательность байтов  b"hello"
# bytearray  Изменяемая последовательность байтов  bytearray(b"hello")
# memoryview  Представление данных в памяти без копирования  memoryview(b"hello")
# NoneType  Отсутствие значения  None

# Неизменяемые типы:
# числа, bool, str, tuple, range, frozenset, bytes, NoneType.

# Изменяемые типы:
# list, dict, set, bytearray


#str
text = "Hello World"

#Первый символ в верхнем регистре остальное в нижнем
print(text.capitalize())

#Все в нижнем
print(text.lower())
#Все в верхнем
print(text.upper())
#каждое слово первый символ в верхнем регистре(ДЛЯ ФИО)
print(text.title())
#Меняет все в верхние на нижний и наоборот
print(text.swapcase())
#str - методы проверки
text = 'abc123'

#строка непустая состоит только из букв и числовых символов
print(text.isalnum())

#Строка непустая и состоит только из букв
print(text.isalpha())

#строка пустая и состоит только из англ букв
print(text.isascii())

#строка не пустая и состоит только из десятичных цифр
print(text.isdecimal())

#строка непустая и состоит только из цифр
print(text.isdigit())

#строка непустая и состоит только из числовых символов
print(text.isnumeric())

#можно ли создать переменную из этого текста
print(text.isidentifier())

#все буквы строчные
print(text.islower())

#все буквы заглавные
print(text.isupper())

#все слова с заглавной
print(text.istitle())

#строка непустая и состоит только из пробельных символов
print(text.isspace())

#все символы печатаемые для пустой строки тоже тру
print(text.isprintable())

# str - Удаление символов
text1 = '  Hello  '

#убирает пробел с двух сторон
print(text1.strip())
print(text1.lstrip()) #слева
print(text1.rstrip()) #справа

print(text1.strip('H'))
print(text1.lstrip('H'))
print(text1.rstrip('H'))

print('www.kaspi.kz'.removeprefix('www.'))
print('www.kaspi.kz'.removesuffix('.kz'))
print('akkahelloakka'.strip('ak'))

#str - замена и преоброзования
text = 'he11o'

#что заменить на что
print(text.replace('1','l'))

# str - выравнивание и заполнение
text = 'hello'

#заполянем длину
print(text.center(10,'*'))
print(text.ljust(10,'*'))
print(text.rjust(10,'*'))

#дополняет слева нулями
print(text.zfill(10))

#str - форматирование
text = 'Привет {name},забронируй место на {time}'

#подставляет значения в поля {}
print(text.format(name = 'assem',time = '19;00'))

name = 'Assem'
age = 22

print(f'Привет {name},забронируй место на {age}')

#str - поиск и подсчет
text = 'Привет {name},забронируй место на {time}'
print(text.count('и'))

#проверяет начало строки
print(text.startswith('При'))
#проверяет конец строки
print(text.endswith('}'))

#возвращает индекс подстроки при отсутствии ошибка
print(text.index('и'))
print(text.rindex('и')) #ищет с конца

#возвращает индекс подстроки при отсутствии вернет -1
print(text.find('и'))
print(text.rfind('и'))

#STR - срезы

#[start, stop, step]
#0 1 2 3 4 5
#П р и в е т
#-6 -5 -4 -3 -2 -1
print('Привет'[:3])
print('Привет'[2:])
print('Привет'[::-1])

#домашка на сб
#так же как на уроке разберите методы list,set,dict
#придумать мини функцию с использованием методов str


#list
flowers = ["роза", "тюльпан", "пион"]

#добавляет элемент в конец списка
flowers.append('хриза')
print(flowers)

#добавляет несколько элементов
new_flowers = ['гортензия','кустовая роза']
flowers.extend(new_flowers)
print(flowers)

#добавляет элемент на указанную позицию
flowers.insert(1, "лилия")
print(flowers)

#Удаляет элемент по значению
flowers.remove('хриза')
print(flowers)

#Удаляет элемент по индексу и возвращает его
flowers.pop(-1)
print(flowers)

#Находит индекс элемента
print(flowers.index('пион'))

#Считает количество повторений элемента
flowers.append('роза')
print(flowers.count('роза'))

#Сортирует исходный список
flowers.sort()
print(flowers)

#в обратном порядке
flowers.sort(reverse=True)
print(flowers)

#создает копию
flowers_copy = flowers.copy()
print(flowers_copy)

#очищает список
flowers_copy.clear()
print(flowers_copy)


# set — множество уникальных элементов
flowers1 = {"роза", "пион", "тюльпан"}

print(flowers)

#Добавляет один элемент
flowers1.add('лилия')
print(flowers1)

#Добавляет несколько элементов
flowers1.update(['хриза','кустовая роза'])
print(flowers1)

#Удаляет элемент, но вызывает ошибку, если его нет
flowers1.remove('роза')
print(flowers1)

#Удаляет элемент без ошибки, если его нет
flowers1.discard('роза')
print(flowers1)

# Удаляет элемент множества,любой

deleted_flower = flowers1.pop()

print(deleted_flower)
print(flowers1)

#Объединяет два множества
flowers2 = {'гортензия','эвкалипт'}
all = flowers1.union(flowers2)
print(all)

#Находит общие элементы
flowers1 = {"роза", "пион", "тюльпан"}
flowers2 = {'роза','гортензия','эвкалипт'}
print(flowers1.intersection(flowers2))


#	Находит элементы, которых нет во втором множестве
print(flowers1.difference(flowers2))

# Проверяет, входят ли все элементы одного множества в другое
flowers1 = {"роза", "пион"}
flowers2 = {"роза", "пион", "тюльпан", "лилия"}
print(flowers1.issubset(flowers2))

# Проверяет, содержит ли множество все элементы другого множества
flowers1 = {"роза", "пион", "тюльпан", "лилия"}
flowers2 = {"роза", "пион"}

print(flowers1.issuperset(flowers2))

#Очищает
flowers1.clear()
print(flowers1)

#SET

# dict — словарь
# dict — хранит данные в формате ключ: значение
shopping = {
    "молоко": 500,
    "хлеб": 200,
    "сыр": 1200
}

print(shopping)

# Добавляет новую пару ключ: значение
shopping['яблоки:'] = 300
print(shopping)

# Изменяет значение по ключу
shopping["молоко"] = 600
print(shopping)

# Получает значение по ключу
print(shopping.get("хлеб"))

# Выводит все названия продуктов
print(shopping.keys())

# Выводит все цены
print(shopping.values())

# Выводит названия продуктов и цены
print(shopping.items())

# Добавляет несколько пар
shopping.update({
    "бананы": 900,
    "апельсины": 800
})
print(shopping)

# Удаляет элемент по ключу
shopping.pop('хлеб')
print(shopping)

#удаление последнего элемента
shopping.popitem()
print(shopping)

#создать копию
shopping_copy = shopping.copy()
print(shopping_copy)

#Проверка наличия ключа — in
print("молоко" in shopping)

#чистка
shopping.clear()
print(shopping)