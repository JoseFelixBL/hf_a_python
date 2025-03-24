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
