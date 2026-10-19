'''
1.оздай список из 5 любимых фильмов. Выведи его и его длину.
2. Дан список [10, 20, 30, 40, 50]. Выведи первый, последний элемент и срез [1:4].
3. Создай пустой список. В цикле for добавь 3 числа через input и добавь его в список с помощью функции append. Выведи результат.
4. Дан список [3, 1, 4, 1, 5]. Отсортируй его через sort(), потом выведи. Затем сделай sorted копию и сравни.
5. Дан список [1, 2, 3]. Сделай копию через .copy(), измени оригинал — копия не должна поменяться.
6. Дан список [5, 3, 8, 1, 9]. Выведи sum, min, max, len.
'''

#1
list = ['H','Q','S','T','U']
print(len(list))

#2
l = [10, 20, 30, 40, 50]
print(l[0])
print(l[-1])
print(l[1:4])

#3

list2 = []
for i in range(3):
    i = input('write 3 int:')

    try:
        i = int(i)
    except ValueError:
        print('error,write int!')

    list2.append(i)
print(list2)



#4

list3 = [3, 1, 4, 1, 5]
list3.sort()
print(list3)

sorted_list3 = sorted(list3)
print(sorted_list3)

if list3 == sorted_list3:
    print('Они равны')
else:
    print('Они разные')

#5
l1 = [1, 2, 3]
a = l1.copy()
print(a)
l1.append([4,5,6])
print(l1)
print(a)

#6
l3 = [5, 3, 8, 1, 9]
print(min(l3))
print(max(l3))
print(sum(l3))
print(len(l3))