def New_Entry(file):
    ID = input('Введите ID: ')
    sirname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    department = input('Введите отдел: ')
    position = input('Введите должность: ')
    with open(file,'a', encoding='utf-8') as book:
        book.write(f'{ID}, {sirname}, {name}, {father_name}, {phone}, {department}, {position}\n')
    print('Новый сотрудник добавлен.')