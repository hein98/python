def greater_first(func):
    def wrap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return wrap


@greater_first
def divide(a, b):
    return a / b


@greater_first
def sub(a, b):
    return a - b


result = divide(2, 4)
print(result)

result2 = sub(4, 98)
print(result2)
