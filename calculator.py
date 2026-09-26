def multiply(expression):
    """Принимает выражение вида 'a * b', вычисляет произведение и возвращает результат"""
    parts = expression.split('*')
    a = float(parts[0].strip())
    b = float(parts[1].strip())
    return a * b