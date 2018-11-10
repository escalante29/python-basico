# devuelve true si la cadena enviada como argumento es palindromo

def validarPalindromo(str):
    is_palindromo = True
    str = str.lower()
    reverse_str = str[::-1]
    print(f'Comparando: {str} con {reverse_str}')

    for idx, char in enumerate(str):
        if(char is not reverse_str[idx]):
            is_palindromo = False

    print(f'La cadena: {str} es palindromo? R/ {is_palindromo}')
    return is_palindromo


validarPalindromo('abc123321cba')
validarPalindromo('Carlos')
validarPalindromo('123321')
validarPalindromo('123456')


