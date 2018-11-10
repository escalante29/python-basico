#ejemplo de filter

a = [0, 1, 2, 3, 4, 5]

div_2 = lambda x: x % 2 == 0

print(list(filter(div_2, a)))

resultado = [i for i in a if div_2(i)]
print(resultado)