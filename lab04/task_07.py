def log_call(function):
    def wrapper(*args):
        print(f"Вызов функции {function.__name__}")
        result = function(*args)
        print(f"Результат: {result}")
        return result

    return wrapper


@log_call
def add(first, second):
    return first + second


add(2, 3)
