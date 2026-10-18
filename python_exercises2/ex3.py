'''
Задача 3. «Метеостанция»
(list, tuple, for, if, распаковка, min/max/sum)

Даны замеры температуры по дням недели:

data = [
    ("Пн", 5, 12),
    ("Вт", 3, 10),
    ("Ср", -2, 8),
    ("Чт", 0, 6),
    ("Пт", 7, 14),
    ("Сб", 10, 18),
    ("Вс", 8, 15),
]
Каждый кортеж — (день, мин, макс).

Что делает программа:
В цикле for day, min_t, max_t in data: вывести для каждого дня строку:

Пн: мин 5, макс 12, среднее 8.5
Посчитать среднюю температуру за неделю (среднее из всех средних).
Найти самый тёплый день (по максимальной температуре) без max.
Найти самый холодный день (по минимальной температуре).
Вывести список дней, где минимальная температура была ниже нуля.
'''


data = [
    ("Пн", 5, 12),
    ("Вт", 3, 10),
    ("Ср", -2, 8),
    ("Чт", 0, 6),
    ("Пт", 7, 14),
    ("Сб", 10, 18),
    ("Вс", 8, 15),
]
avg_of_week = []

for day, min_t, max_t in data:
    avg = (min_t + max_t)/2
    print(f'{day}: мин {min_t}, макс {max_t}, среднее {avg}')
    avg_of_week.append(avg)
    average = sum(avg_of_week)/len(avg_of_week)

print(f'Средняя температура за неделю:{average}')


max_temperature = 12
first_day = "пн"
for day, min_t, max_t in data:
    if max_temperature<max_t:
        max_temperature = max_t
        first_day = day
print(f'самый теплый день: {first_day}, самая высокая температура: {max_temperature}')

min_temperature = 5
f_day = "пн"
for day, min_t, max_t in data:
    if min_temperature>min_t:
        min_temperature = min_t
        f_day = day
print(f'самый холодный день: {f_day}, самая низкая температура: {min_temperature}')


for day, min_t, max_t in data:
    if min_t<0:
        print(f'{day}: {min_t}')
