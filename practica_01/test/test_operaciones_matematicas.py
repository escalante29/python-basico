# unit tests for calculator math operations
import operaciones_matematicas as OM


print('********** Testing calc methods **********')


def test_suma_simple():
    a = 2
    b = 1
    result = 3
    print(f'\n.test suma: {a} + {b}, deberia ser {result}')
    assert result == OM.suma(a, b)


def test_resta_simple():
    a = 5
    b = 4
    result = 1
    print(f'test resta: {a} - {b}, deberia ser {result}')
    assert result == OM.resta(a, b)


def test_multiplicacion_simple():
    a = 4
    b = 4
    result = 16
    print(f'test multiplicacion: {a} * {b} deberia ser {result}')
    assert result == OM.multiplicacion(a, b)


def test_division_por_zero():
    a = 10
    b = 0
    result = None # better would be to test for raised ZeroDivisionError exception
    print(f'test division entre cero deberia ser: None')
    assert result == OM.division(a, b)


def test_division_simple():
    a = 6
    b = 2
    result = 3
    print(f'test division entre {a} y {b} deberia ser: {result}')
    assert result == OM.division(a, b)
