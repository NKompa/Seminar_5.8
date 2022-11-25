def Veiw_all(file):
    with open(file, encoding="utf-8") as data:
        for line in data:
            print(line.replace(',', ''))