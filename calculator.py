def multiply(a, b):
    return a * b
def main_function():
    input_data = input("введите выражение")
    parts = input_data.split()

    a = to_number(parts[0])
    operator = parts[1]
    b = to_number(parts[2])

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = substract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    elif operator == "/":
        result = divide(a, b)
    else:
        print("Вы мне втерли какую то дичь, что такое", operator, "?")
        return
    print(result)



