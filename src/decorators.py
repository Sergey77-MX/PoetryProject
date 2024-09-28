import os


def log(filename=None):
    """Декоратор регистрирует детали выполнения функций"""

    def wrapper(func):

        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    if len(filename) > 0:
                        path_to_file = os.path.join(os.path.dirname(__file__), "../logs", filename)
                        with open(path_to_file, "w", encoding="utf-8") as file:
                            file.write(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e}. Inputs: ({args}), {kwargs}")
                else:
                    path_to_file = os.path.join(os.path.dirname(__file__), "../logs", filename)
                    with open(path_to_file, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}), {kwargs}")

        return inner

    return wrapper


@log(None)
def my_function(x, y):
    # raise ValueError("Something went wrong")
    return x + y


my_function(1, 2)
