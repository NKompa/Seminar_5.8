with open('employees.csv', encoding='utf-8') as file:
    data = file.read().split('\n')
list1 = []
for i in data:
    i = i.split(', ')
    list1.append(i)


print('Колонки: 1 - ID, 2 - Фамилия, 3 - Имя, 4 - Отчество, 5 - телефон, 6 - Должность, 7 - Отдел')
columns = list(map(int,(input("Выберите необходимые колонки: ").split(' '))))

print(list1)
request = []
for i in range(len(list1)):
    for k in columns:
        request.append(list1[i][k-1])
    print(request)
    # print(' '.join(request), end='\n')
    request = []