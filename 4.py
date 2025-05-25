def calculator():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Введите операцию (+, -, *, /): ")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            try:
                result = a / b
            except ZeroDivisionError:
                print("Ошибка: деление на ноль!")
                return
        else:
            print("Ошибка: неизвестная операция!")
            return

        print("Результат:", result)

    except ValueError:
        print("Ошибка: введено не число!")

calculator()
