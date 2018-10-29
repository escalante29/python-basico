#ejemplo try except


a = 10
b = 0

#operaciones
try:
    c = a/b
except ZeroDivisionError:
    print("tengo un error")
    c = a
else:
    pass
finally:
    pass
