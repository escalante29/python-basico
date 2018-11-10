# ejemplo de reduce

from functools import reduce

a = [0,1,2,3,4,5,6,7,8,9]

mi_funcion = lambda x, y : x+y

print(reduce(mi_funcion, a))