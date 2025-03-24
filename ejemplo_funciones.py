# Funciones
def hello():
    print(msg)


msg = 'Mensaje de hello'
# Pasar una función a otra función
print(f'{id(msg)=}, {type(msg)=}')
print(f'{id(hello)=}, {type(hello)=}')
print('hello()')
hello()

print(f'{"-" * 30}')

# retornar una función


def apply(func: object, value: object) -> object:
    return func(value)


print('apply(print, 42)')
apply(print, 42)
print(f'{apply(id, 42)=}')
print(f'{apply(type, 42)=}')
print(f'{apply(len, 'Marvin')=}')
print(f'{apply(type, apply)=}')

print(f'{"-" * 30}')

# Retornar una función interna


def outer():
    def inner():
        print('This is inner')
    print('This is outer, returning inner')
    return inner


print('i = outer()')
i = outer()
print(f'{id(i)=}, {type(i)=}')
print('i()')
print(f'{i()}')

print(f'{"-" * 30}')

# Procesando una lista de argumentos


def my_func(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()


my_func(10)
my_func()
my_func(10, 20, 30, 40, 50)
my_func(1, 'dos', 3, 'cuatro', 5)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'diez']
my_func(values)
my_func(*values)

print(f'{"-" * 30}')

# Procesando diccionarios


def my_dict_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


my_dict_func(a=10, b=20)
my_dict_func()
my_dict_func(a=10, b=20, c=30, d=40, e=50)

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }
my_dict_func(**dbconfig)

# Procesando cualquier número y tipo de argumentos de función


def my_func_3(*args, **kwargs):
    for a in args:
        print(a, end=' ')
    # if args:
    #     print()

    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    # if kwargs:
    print()


my_func_3(1, 2, 3)
my_func_3()
my_func_3(a=10, b=20, c=30)
my_func_3(1, 2, 3, a=10, b=20, c=30)
