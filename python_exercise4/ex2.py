'''
2. Анализатор текстового файла
(file read, str methods, dict, set, for, sorted)
Дан файл text.txt с текстом (можешь положить туда пару абзацев сам).
Программа:
Читает файл построчно через for line in f.
Считает:
количество строк
количество слов
количество уникальных слов (через set)
самое частое слово (через dict + max)
самое длинное слово
количество знаков препинания (через in по строке ".,!?;:")
Выводит отчёт.
Ожидаемый вывод:

=== АНАЛИЗ ТЕКСТА ===
Строк: 5
Слов: 87
Уникальных слов: 54
Самое частое: "и" (7 раз)
Самое длинное: "программирование"
Знаков препинания: 12
Тренирует: файлы + строки + dict + set + for + sorted.
'''

f = open('text.txt','r')
line_count = 0
total_words = 0
uniq_words = set()
word_frequency = {}
longest_word = str()
punctuation_count = 0

for line in f:
    line_count +=1
    words_in_line = line.split()
    total_words += len(words_in_line)
    for words in words_in_line:
        uniq_words.add(words)
        if words in word_frequency:
            word_frequency[words] += 1
        else:
            word_frequency[words] = 1
    for current_word in uniq_words:
        if len(current_word) > len(longest_word):
            longest_word = current_word
    punctuation_marks = ".,!?;:"
    for current_symbol in line:
        if current_symbol in punctuation_marks:
            punctuation_count += 1

most_common_word = max(word_frequency, key=word_frequency.get)







print(line_count)
print(total_words)
print(len(uniq_words))
print(word_frequency)
print(f'Самое частое слово: "{most_common_word}"')
print(f'Количество повторений: {word_frequency[most_common_word]}')
print(longest_word)
print(punctuation_count)

