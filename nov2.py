#создает функцию
import tarfile


def ab_sum(name,age):
    return name, age

print(ab_sum('Assem',22))

def ab_sum(name,age,*args, **kwargs):
    return name, age, args, kwargs

print(ab_sum('Assem',22, 1, 4, 'a' ,gender = 'Female'))


cap_name = lambda name:  name.title()
print(cap_name('asem'))

def cap_name(n):
    return n ** 2

numbers = list(range(11))
print(numbers)

#Для отнотипных функции map
print(list(map(cap_name, numbers)))
print(list(map(lambda n: n ** 2 , numbers)))
print(list(map(lambda  n: str(n), numbers)))

names = ['gh','sh','ls']
print(list(map(lambda n: n.title(), names)))

#filter можно поставить условие
print(list(filter(lambda n: n % 2 == 0, numbers)))

print(sorted([3,5,6,2]))
print(sorted([3,5,6,2], reverse = True))


#задание


# 1. Исправление списка гостей

# guests = ["  аЛи ", "АННА", "али", "  иВАН", "анна  "]
# Напиши функцию prepare_guests(guests), которая:
# - Удаляет пробелы по краям и приводит имена к виду "Али".
# -  Убирает повторяющиеся имена.
# - Возвращает список имён по алфавиту.
# Ожидаемый результат:
# ["Али", "Анна", "Иван"]
# Используй методы строк, map(), set() и sorted().


guests = ["  аЛи ", "АННА", "али", "  иВАН", "анна  "]

def prepare_guests(guests):
    guests = list(map(lambda name: name.strip().capitalize(), guests))
    sets = set(guests)
    sorted_guests = sorted(sets)
    return sorted_guests

print(prepare_guests(guests))

'''
2. Управление очередью
queue = ["Али", "Анна", "Иван", "Мария"]
Выполни события по порядку:
В очередь встал Олег.
Вера заняла место сразу после Али.
Иван ушёл из очереди.
Первого человека обслужили — сохрани его имя.
Найди позицию Марии в очереди, считая места с единицы.
Выведи имя обслуженного человека, итоговую очередь и место Марии.
Используй append(), insert(), remove(), pop() и index().
'''
queue = ["Али", "Анна", "Иван", "Мария"]
queue.append("Олег")
queue.insert(1,"Вера")
queue.remove("Иван")
print(queue.pop(0))
print(queue)
print(queue.index("Мария"))

# 3. Фильтр правильных имён
# names = ["Анна", "иван", "123", "", "Олег!", "  Мария  ", "Ян"]
# Напиши функцию valid_names(names), которая очищает пробелы и оставляет только имена, состоящие из букв и
# содержащие не менее трёх символов. Приведи имена к виду "Анна".

# Ожидаемый результат:
# ["Анна", "Иван", "Мария"]
# Используй strip(), isalpha(), len(), map() и filter().

names = ["Анна", "иван", "123", "", "Олег!", "  Мария  ", "Ян"]
def valid_names(names):
    names = list(map(lambda name: name.strip().capitalize(), names))
    names = list(filter(lambda name:name.isalpha() and len(name) > 3 ,names))
    return names

result = valid_names(names)
print(result)


#4. Общие интересы
# ali = {"Python", "шахматы", "музыка", "кино"}
# anna = {"музыка", "рисование", "Python", "танцы"}
# Найди:
# - Общие интересы.
# - Все интересы двух друзей.
# - Интересы, которые есть только у Али.
# - Интересы, которые есть только у Анны.
# - Есть ли у обоих интересы "Python" и "музыка".
# Для удобства выводи полученные множества как списки по алфавиту.

# Используй intersection(), union(), difference() и issubset().

ali = {"Python", "шахматы", "музыка", "кино"}
anna = {"музыка", "рисование", "Python", "танцы"}

print(sorted(ali.intersection(anna)))
print(sorted(ali.union(anna)))
print(sorted(ali.difference(anna)))
print(sorted(anna.difference(ali)))
required_interests = {"Python", "музыка"}
if required_interests.issubset(ali) and required_interests.issubset(anna):
    print(True)
else:
    print(False)
# 5. Анализ сообщения
# text = "  Python это интересно python это полезно Python  "
# Напиши функцию analyze_text(text), которая приводит текст к нижнему регистру, разбивает его на слова и возвращает словарь:
# {
#     "words": 8,
#     "unique_words": 5,
#     "python_count": 3
# }
# Используй lower(), split(), set(), count() и len().

text = "  Python это интересно python это полезно Python  "
def analyze_text(text):
    text1 = text.lower()
    text2 = text1.split()
    words = len(text2)
    unique_words = len(set(text2))
    python_count = text2.count('python')
    return {
        "words": words,
        "unique_words": unique_words,
        "python_count": python_count
    }


result = analyze_text(text)
print(result)

# 6. Обновление профиля игрока
# player = {
#     "name": "  аЛи ",
#     "level": 3,
#     "city": "Алматы",
#     "temporary": True
# }
# Напиши функцию update_profile(player), которая создаёт копию словаря и в ней:
# - Исправляет имя на "Али".
# - Повышает уровень на один.
# - Удаляет ключ "temporary".
# - Добавляет "country": "Kazakhstan", только если такого ключа ещё нет.
# Верни обновлённый словарь. Исходный player должен сохранить прежние данные.

# Используй copy(), методы строк, update(), pop() и setdefault().

player = {
    "name": "  аЛи ",
    "level": 3,
    "city": "Алматы",
    "temporary": True
}

def update_profile(player):
    new_player = player.copy()
    new_player["name"] = new_player["name"].strip().capitalize()
    new_player["level"] += 1
    new_player.pop("temporary")
    new_player.setdefault("country", "Kazakhstan")
    return new_player

result = update_profile(player)
print(result)
print(player)

