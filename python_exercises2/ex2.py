'''
Задача 2. «Банкомат»
(while, if/elif/else, list, функции, try/except, f-strings)

Сделай мини-банкомат с меню.
Что делает:
Начальный баланс — 1000.
История операций — пустой список.
В цикле while True показать меню:

1 — пополнить
2 — снять
3 — история
4 — выход

Ввод обработать через try/except (если не число → сообщение об ошибке).

Логика:
пополнение → прибавить к балансу, добавить в историю "+500"
снятие → если хватает денег, вычесть; если нет → «Недостаточно средств»
история → вывести все операции через for
выход → break

После выхода — вывести итоговый баланс и количество операций (через len).


'''

balance = 1000
history = []

while True:
    print("1 = Пополнить")
    print("2 = снять")
    print("3 = история")
    print("4 = выход")
    choise_str = input('выбери 1 пункт:')
    try:
        choise = int(choise_str)
    except ValueError:
        print('ошибка! введи число!')
        continue

    if choise == 1:
        print("Пополнение")
        amount_str = input("Какую сумму хотите внести : ")
        try:
            amount = int(amount_str)
            if amount > 0:
                balance += amount
                history.append("+" + str(amount))
                print(f"Пополнение прошло успешно! Ваш баланс: {balance}")
            else:
                print("введи положительное число")

        except ValueError:
            print('напиши число!')
    elif choise == 2:
        print("Снятие")
        amount_str = input("Какую сумму хотите снять : ")
        try:
            amount = int(amount_str)
            if amount <= 0:
                print("Введи положительную сумму!")
            elif amount > balance:
                print("Недостаточно средств!")
            else:
                balance -= amount
                history.append("-" + str(amount))
                print(f"Снятие прошло успешно! Ваш баланс: {balance}")

        except ValueError:
            print('напиши число!')
    elif choise == 3:
        if len(history) == 0:
            print('История пустая!')
        else:
            for element in history:
                print(element)
    elif choise == 4:
        print("Работа завершена!")
        print(f"Ваш баланс: {balance}")
        print(f"Количество операций: {len(history)}")
        break
    else:
        print("такого пункта нет")
