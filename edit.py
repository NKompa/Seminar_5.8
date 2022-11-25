def Edit_Entry(file):

    print(f'Введите фамилию сотрудника для изменения данных о нём в БД: ')
    name = input()
    lines = []

    with open(file, encoding="utf-8") as data:
        for line in data:
            if not name in line:
                lines += line
            else:
                line = line.split(", ")
                old = int(input("Номер элемента для замены: "))
                new = input("На что заменить: ")
                line[old] = new
                line = ", ".join(line)
                lines += line

    with open(file, 'w', encoding="utf-8") as data:
        data.writelines(lines)

    print('Изменение выполнено.')