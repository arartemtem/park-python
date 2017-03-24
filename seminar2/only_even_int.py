class only_even_ints():
    '''This class add to list only even numbers of type int'''

    message = 'I LIKE ONLY INT TYPE AND I DON\'T LIKE ODD NUMBERS!'

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values
            for i in range(len(values)):
                if type(values[i]) == int and values[i] % 2 == 0:
                    pass
                else:
                    values[i] = only_even_ints.message

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        if type(value) == int and value % 2 == 0:
            self.values[key] = value
        else:
            self.values[key] = only_even_ints.message

values_list = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 'one', 'two', 5.5, 3.3]
my_list = only_even_ints(values_list)
print(my_list[:])
print('\n')
my_list[0] = 2000000000
my_list[1] = 1
print(my_list[:])
