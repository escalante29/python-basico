import palindromo

def test_validar_palindromo():
    str_prueba = '12321'

    print(f'Probando si {str_prueba} es palindromo...')

    assert True == palindromo.validarPalindromo(str_prueba)

def test_validar_no_palindromo():
    str_prueba = '123'

    print(f'Probando si {str_prueba} no es palindromo...')

    assert False == palindromo.validarPalindromo(str_prueba)