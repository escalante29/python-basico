#primer ejemplo con for

for elemento in [1,2,3,4,5]:
    print(elemento)

for nombre in ['maria', 'jose', 'carlos', 'daniela']:
    print(nombre)

nombres = ['maria', 'jose', 'carlos', 'dani']

for idx, elem in enumerate(nombres):
    print(elem, idx)
    print('El indice {} para el valor {}'.format(idx, elem))
    print(f'El indice {idx}, para el valor {elem}')

for idx, elem in enumerate(nombres[::2]):
    print(f'El indice {idx}, para el valor {elem}\n')

for idx, elem in enumerate(nombres[::-1]):
    print(f'El indice {idx}, para el valor {elem}\n')

for idx, elem in enumerate(sorted(nombres)):
    print(f'El indice {idx}, para el valor {elem}')

for idx, elem in enumerate(sorted(nombres, reverse=True)):
    print(f'El indice {idx}, para el valor {elem}')

for idx, elem in enumerate([]):
    print(f'El indice {idx}, para el valor {elem}')
else:
    print('El loop no inicio')
