def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('no se puede dividir entre cero')
        result = None
    return result


def multiplicacion(a, b):
    return a * b

def init_operations_dictionary():
    return {
        'suma': suma,
        'multiplicacion': multiplicacion,
        'division': division,
        'resta': resta
    }