def ignore_exceptions(exception_func):
    def wrapper(x, y):
        try:
            exception_func(x, y)
        except TypeError:
            pass
        else:
            return exception_func(x, y)
    return wrapper

@ignore_exceptions
def str_plus_int(x, y):
    z = x + y
    return z

a = 'string'
b = 6

print(str_plus_int(a, b))
print('program continues')