import random


dict = {}
for i in range(1,11):
    dict[i] = i*2

print(dict)

diccionario = ['col','mex','ven']

poblacion = {element: random.randint(0,5000) for element in diccionario}
print(poblacion)