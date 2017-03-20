from datetime import datetime


def log_duration(function_to_decorate):
    def wrapper():
        print('Decorated function')
        function_to_decorate()
        print(datetime.strftime(datetime.now(), "%H:%M:%S"))
    return wrapper


@log_duration
def just_print_function():
    print('Function was decorated at')


just_print_function()
