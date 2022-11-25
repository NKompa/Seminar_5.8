def Delete_Entry(file):

    print(f'Введите данные сотрудника для удаления записи о нём: ')
    name = input()
    lines = []

    with open(file, encoding="utf-8") as data:
        for line in data:
            if not name in line: lines += line

    with open(file, 'w', encoding="utf-8") as data:
            data.writelines(lines)

    print('Удаление выполнено.')