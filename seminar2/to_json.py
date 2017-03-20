import json


def to_json(dict_or_no):
    def wrapper(data):
        if type(data) == dict:
            data = json.dumps(data)
            return 'Conversion to json: ' + dict_or_no(data)
        else:
            return dict_or_no(data)
    return wrapper


data1 = {'1': 'first', '2': 'second', '3': 'third'}
data2 = ['one', 'two', 'three']


@to_json
def input_data(data):
    return data


print(input_data(data1))
print(input_data(data2))
