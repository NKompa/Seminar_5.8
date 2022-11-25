import delete
import write
import print1
import edit
import search
import columns

while True:
    print("Меню:")
    print('1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Вывести колонки.\n7. Выход.\n')

    value = int(input("Выберите действие: "))
    if value == 1:
        print1.Veiw_all('employees.csv')
    if value == 2:
        write.New_Entry('employees.csv')
    if value == 3:
        search.Search_Entry('employees.csv')
    if value == 4:
        edit.Edit_Entry('employees.csv')
    if value == 5:
        delete.Delete_Entry('employees.csv')
    if value == 6:
        columns.Print_Columns()
    if value == 7:
        break