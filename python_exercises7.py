'''
1. Первая функция
(def, return, f-string)

Напиши функцию greet(name), которая возвращает строку "Привет, <name>!". Вызови её 3 раза с разными именами и выведи результаты.

'''

def say_hello(name):
    print(f'Привет,{name}')

say_hello('Asem')
say_hello('Asem1')
say_hello('Asem2')

'''
-----------------------------------------------------------
2. Квадрат и куб
(def, return, арифметика)

Напиши две функции: square(x) и cube(x). Выведи square(5) и cube(3).


-----------------------------------------------------------
'''

def square(x):
    return x**2

print(square(5))

def cube(x):
    return x**3

print(cube(3))


'''
3. return vs printx

def f1(x):
    print(x * 2)

def f2(x):
    return x * 2

Выведи результаты:

a = f1(5)     # что в a?
b = f2(5)     # что в b?
print("a =", a)
print("b =", b)

Сделай анализ результатов вывода в консоль
'''

def f1(x):
    print(x * 2)

def f2(x):
    return x*2
a = f1(5)
b = f2(5)

print("a =", a)
print("b =", b)

'''
-----------------------------------------------------------
4. Функция с двумя параметрами
(def, несколько параметров)

Напиши rectangle_area(width, height) — возвращает площадь. Выведи для (5, 3) и (10, 2.5). 
Проверь type() результата в обоих случаях - выведи его в консоль.

-----------------------------------------------------------
'''

def rectangle_area(width,height):
    return width * height

print(rectangle_area(5,3))
print(rectangle_area(10, 2.5))

print(type(rectangle_area(5,3)))
print(type(rectangle_area(10, 2.5)))

'''
5. Значение по умолчанию
(def, дефолтные параметры)

Напиши power(base, exp=2) — возводит base в степень exp. Проверь:

power(5)         # 25
power(2, 10)     # 1024
power(3, 3)      # 27
'''
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 10))     # 1024
print(power(3, 3))

'''
6. Возврат кортежа
(def, tuple)

Напиши min_max(numbers) — возвращает (минимум, максимум) через return min(numbers), max(numbers). Распакуй результат в две переменные:

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)   # 1 5
'''

def min_max(numbers):
    return min(numbers), max(numbers)
lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)
'''
-----------------------------------------------------------
7. Функция-проверка
(def, if, return bool)

Напиши is_even(n) — возвращает True/False. Проверь на 4, 7, 0, -2.
'''
def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(7))
print(is_even(0))
print(is_even(-2))
'''
-----------------------------------------------------------
8. Функция со строкой
(def, str methods)

Напиши clean_name(s) — убирает пробелы по краям и делает первую букву заглавной:

clean_name("  аня  ")   # "Аня"
clean_name("БОРИС")     # "Борис"
Подсказка: s.strip().capitalize() или s.strip()[0].upper() + s.strip()[1:].lower().
'''

def clean_name(s):
    return s.strip()[0].upper() + s.strip()[1:].lower()
print(clean_name("  аня  "))  # "Аня"
print(clean_name("БОРИС"))
'''
-----------------------------------------------------------
9. Вызов функции из функции
(def, вызов внутри вызова)

Напиши circle_area(r) и circle_length(r) (через 3.14). Затем circle_info(r), которая возвращает кортеж (площадь, длина), 
вызывая первые две.
'''
def circle_area(r):
    return 3.14 * r ** 2
def circle_length(r):
    return 3.14 * r * 2
def circle_info(r):
    return circle_area(r),circle_length(r)
print(circle_area(3))
print(circle_length(3))
print(circle_info(3))
'''
-----------------------------------------------------------
10. Ловушка с изменяемым дефолтом
(def, ловушка lst=[])

def add(item, lst=[]):
    lst.append(item)
    return lst

print(add(1))    # ?
print(add(2))    # ?
print(add(3))    # ?

Запусти и посмотри на результат. Затем исправь функцию через lst=None:

def add(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
Проверь снова — теперь [1], [2], [3].
'''


def add(item, lst=[]):
    lst.append(item)
    return lst

print(add(1))    # ?
print(add(2))    # ?
print(add(3))    # ?

def add(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add(1))    # ?
print(add(2))    # ?
print(add(3))