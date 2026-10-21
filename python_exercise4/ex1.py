'''
1. Телефонный справочник с сохранением
(dict, file, try/except, while, str methods)
Программа:
При старте читает contacts.txt (формат: Имя:номер по строке) и загружает в dict.
В цикле показывает меню:
1 - добавить
2 - найти
3 - удалить
4 - показать все
5 - сохранить и выйти
Операции:
добавить: спросить имя и номер, положить в dict
найти: спросить имя, вывести номер или «не найден»
удалить: спросить имя, удалить через pop с обработкой
показать все: перебрать for k, v in dict.items()
При выходе — записать весь dict в contacts.txt.
Тренирует: dict + файлы + try/except + while + строковые методы.
Ожидаемая структура contacts.txt:
Аня:+7-701-111-22-33
Борис:+7-702-444-55-66
'''

contacts_dict = dict()
# загружаю файл contacts.txt в dict
contacts_file = open("contaxts.txt", "r")
for line in contacts_file.readlines():
    line_list = line.split(",")
    name = line_list[0]
    phone_number = line_list[1].replace("\n", "")
    # contacts_dict.setdefault(name, phone_number)  # оставляем первое
    # вхождение повторяющихся имен
    contacts_dict[name] = phone_number  # оставляем последнее
    # вхождение повторяющихся имен
contacts_file.close()

while True:
    print('1 - добавить')
    print('2 - найти')
    print('3 - удалить')
    print('4 - показать все')
    print('5 - сохранить и выйти')
    choise_str = input('Выберите пункт:')
    try:
        choise = int(choise_str)
    except ValueError:
        print('напишите число!')
        continue
    if choise == 1:
        print('Добавить:')
        new_name = input('Напишите имя:')
        new_number_str = input('Напишите номер:')
        try:
            new_number = int(new_number_str)
        except ValueError:
            print('напишите число!')
        if new_name in contacts_dict:
            print('Уже есть такой контакт.Сначала удалите старый контакт')
            continue
        contacts_dict[new_name] = new_number_str
    elif choise == 2:
        print('Найти')
        name_to_search = input('Введите имя контакта,который ищете:')
        if name_to_search not in contacts_dict:
            print('не найден')
        else:
            print(phone_number)
    elif choise == 3:
        # 3 - удалить
        name_to_delete = input("Введите имя контакта, который удаляете:")
        deleted_name = contacts_dict.pop(name_to_delete, None)
        if deleted_name is None:
            print("Имя не найдено")
    elif choise == 4:
        # 4 - показать все
        for name, phone_number in contacts_dict.items():
            print(f"{name}: {phone_number}")
    elif choise == 5:
        # 5 - сохранить и выйти
        contacts_file = open("contacts.txt", "w")
        for name, phone_number in contacts_dict.items():
            contacts_file.write(f"{name}:{phone_number}\n")
        contacts_file.close()
        exit(0)
    else:
        print("Вы ввели число не из меню, попробуйте еще раз")
        continue

if __name__ == '__main__':
    main()

