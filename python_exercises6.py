'''
1. Анализ оценок класса
(list, for, if, dict, set)

grades = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5, 2, 4]

Выведи:

количество каждой оценки через dict + for ({5: 4, 4: 4, 3: 2, 2: 2})
средний балл
список уникальных оценок через set, отсортированный
сколько отличников (пятёрок)

Ожидаемый вывод:

Оценки: {5: 4, 4: 4, 3: 2, 2: 2}
Средний балл: 4.0
Уникальные: [2, 3, 4, 5]
Пятёрок: 4
'''


grades = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5, 2, 4]
grades_count = {}
for grade in grades:
    if grade in grades_count:
        grades_count[grade] +=1
    else:
        grades_count[grade] = 1

print(f'Оценки: {grades_count}')
average = sum(grades)
av = average / len(grades)
print(f'Средний балл: {av}')
unique = set(grades)
print(f'Уникльные:{unique}')

fives = 0
for grade in grades:
    if grade == 5:
        fives += 1

print(f'Пятерок: {fives}')



'''
2. Частотный словарь слов
(str methods, split, dict, for, sorted)

text = "python это язык python простой и python мощный"
Приведи к нижнему регистру.

Разбей на слова через split().
Посчитай частоту каждого слова в dict.
Выведи топ-3 по частоте (через sorted с key или вручную).

Ожидаемый вывод:

text
Слова: {'python': 3, 'это': 1, 'язык': 1, 'простой': 1, 'и': 1, 'мощный': 1}
Топ-3: [('python', 3), ('это', 1), ('язык', 1)]
Подсказка: для сортировки — sorted(d.items(), key=lambda x: -x[1]), но если lambda не проходили, отсортируй вручную.

'''

text = "python это язык python простой и python мощный"
print(text.lower())
words = text.split()
dict = {}
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)

max_word = ''
max_count = 0
for word1,count in dict.items():
    if count > max_count:
        max_count = count
        max_word = word1

second_word = ''
second_count = 0

for word1, count in dict.items():
    if word1 != max_word and count>second_count:
        second_count = count
        second_word = word1

third_word = ''
third_count = 0
for word1,count in dict.items():
    if word1 != max_word and word1 != second_word and count>third_count:
        third_count = count
        third_word = word1

print(f"Топ-3: {[(max_word, max_count), (second_word, second_count), (third_word, third_count)]}")

'''
3.. Общие друзья
(set, set operations)

anna_friends = {"Борис", "Вера", "Глеб", "Даша"}
boris_friends = {"Вера", "Глеб", "Егор", "Жанна"}
Выведи:

общих друзей (&)
всех знакомых (|)
только Анниных (-)
тех, кто есть только у одного (^)

'''

anna_friends = {"Борис", "Вера", "Глеб", "Даша"}
boris_friends = {"Вера", "Глеб", "Егор", "Жанна"}
o = anna_friends & boris_friends
all = anna_friends | boris_friends
anna = anna_friends - boris_friends
u = anna_friends ^ boris_friends
print(f'Общие друзья:{o}')
print(f'всех знакомых:{all}')
print(f'только анниных: {anna}')
print(f'у одного: {u}')

'''
4. Журнал ошибок
(try/except, file write, while, if)

В цикле while True проси ввести число. Пока не введено stop:
если число — запиши его в ok.txt
если не число — запиши в errors.txt строку вида "abc (не число)"

В конце выведи количество успешных и ошибочных строк.

'''
ok_count = 0
error_count = 0
while True:
    any_number_str = input('введите число:')
    if any_number_str == 'stop':
        break
    try:
        any_number = int(any_number_str)
        my_file1 = open('ok.txt','a')
        my_file1.write(str(any_number) + '\n')
        my_file1.close()
        ok_count += 1
    except ValueError:
        my_file1 = open('errors.txt','a')
        my_file1.write(any_number_str + 'не число\n')
        my_file1.close()
        error_count += 1
print(f'Успешные:{ok_count}')
print(f'ошибочные:{error_count}')