from datetime import datetime


def decorator(function_to_decorate):
    def wrapper():
        print('Decorated function')
        function_to_decorate()
        print(datetime.strftime(datetime.now(), "%H:%M:%S"))
    return wrapper


@decorator
def just_print_function():
    print('Function was decorated at')


just_print_function()
