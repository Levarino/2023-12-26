def introspection_info(obj):
    return {
        'type': type(obj),
        'id': id(obj),
        'class': obj.__class__.__doc__,
        'doc': obj.__doc__,
        'hash': obj.__hash__,
        'dir': dir(obj),
        'obj': obj
    }


class MyClass:
    def __init__(self):
        pass


obj = MyClass()

number_info = introspection_info(42)
print(number_info)
print()
print()
print(type(number_info))
print(obj.__hash__)
print(number_info['hash'])
print(number_info['class'])
print(number_info['id'])
print(number_info['type'])
