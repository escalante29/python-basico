def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def division(a, b):
    return a / b


def multiplicacion(a, b):
    return a * b

def init_operations_dictionary():
    return {
        'suma': suma,
        'multiplicacion': multiplicacion,
        'division': division,
        'resta': resta
    }