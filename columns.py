def File_2D_List(file):
    with open(file, encoding='utf-8') as file:
        data = file.read().split('\n')

    list1 = []
    for i in data:
        i = i.split(', ')
        list1.append(i)
    return list1

def Print_Columns():
    file = File_2D_List('employees.csv')
    a = file.pop()
    print('Колонки: 1 - ID, 2 - Фамилия, 3 - Имя, 4 - Отчество, 5 - телефон, 6 - Отдел, 7 - Должность')
    columns = list(map(int,(input("Выберите необходимые колонки: ").split(' '))))
    request = []
    for i in range(len(file)):
        for k in columns:
            request.append(file[i][k-1])
        print(' '.join(request), end='\n')
        request = []