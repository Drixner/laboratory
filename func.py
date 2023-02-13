# definicion: funcion que suma los elementos de una lista
def adicion(list):
    
    x = 0 # variable que almacena la suma
    for i in list: # recorre la lista
        x += i # suma los elementos de la lista
    return x # retorna el resultado

adic = adicion([1,2,3,4,5,6,7,8,9,10])# llamada a la funcion

print(adic) # imprime el resultado

adicc = adicion([1,2,3,4]) # llamada a la funcion

print(adicc)
