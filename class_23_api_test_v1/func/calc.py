def add(a, b):
    """ 不是if的时候默认返回None """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b


def minus(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b


def multiply(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b


def division(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a / b
