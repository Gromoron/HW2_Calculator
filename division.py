try:
    number_1 = float(input("Введите делимое: "))
    number_2 = float(input("Введите делитель: "))
    division = number_1 / number_2
    print(division)
    print(f"Результат: {number_1} / {number_2} = {division}")
except ZeroDivisionError:
    print("Ошибка: на ноль делить нельзя!")
except ValueError:
    print("Ошибка: введите корректное число!")
