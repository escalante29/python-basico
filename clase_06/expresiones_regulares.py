def detectar_termino_en_cadena(termino, cadena):
    return termino in cadena

is_in_string = detectar_termino_en_cadena('Pidro', 'Carlos Andres Pedro Felipe')
print(f'resultado: {is_in_string}')

import re

result = re.search(r'Co.k.e', 'Cookie').group()

print('result-> ', result)