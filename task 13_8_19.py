tikets = int(input("Введите количество билетов: "))
n = 1
total = 0
if tikets <=0:
    print ("Введено некорректное значение. Введите корректное количество билетов")
else:
    while n <= tikets:
        age = int(input("Введите возраст посетителя ", ))
        if 0 <= age < 18:
            n += 1
        elif 18 <= age < 25:
            total += 990
            n += 1
        elif age > 25:
            total += 1390
            n += 1
        else:
            print("Указан некорректный возраст")

    if total > 0:
        if tikets > 3:
            total *= 0.9
        print("Сумма к оплате: ", total)
    else:
        print("Вход бесплатный")