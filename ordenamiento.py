# Ordenamiento de datos por el metodo de la burbuja

# import random as rd
# lista = [rd.randint(1,100) for i in range(20)]
# for i in range(len(lista)-1):
#     for j in range(len(lista)-1):
#         if lista[j] > lista[j+1]:
#             lista[j], lista[j+1] = lista[j+1], lista[j]
# print(lista)

# Ordenamiento de datos por el metodo de la insercion

# import random as rd
# lista = [rd.randint(1,100) for i in range(20)]

# for i in range(1, len(lista)):
#     actual=lista[i]
#     indice=i
#     while indice>0 and lista[indice-1]>actual:
#         lista[indice]=lista[indice-1]
#         indice-=1
#     lista[indice] = actual
# print(lista)

# Ordenamiento de datos por metodo de la selección

# import random as rd
# lista = [rd.randint(1,100) for i in range(20)]
# longitud=len(lista)
# for i in range (longitud-1):
#     ind_menor=i
#     for j in range(i+1,longitud):
#         if lista[j]<lista[ind_menor]:
#             ind_menor = j
#     lista[i], lista[ind_menor] = lista[ind_menor], lista[i]
# print(lista)

# Oordenamiento de datos por el metodo shell

import random as rd
lista = [rd.randint(1,100) for i in range(21)] 
longitud = len(lista)
gap = longitud//2
while gap > 0:
    for i in range(gap, longitud):
        actual= lista[i]
        indice = i
        while indice>= gap and lista[indice - gap] > actual:
            lista[indice] = lista[indice-gap]
            indice-=gap
        lista[indice] = actual     
    gap//=2

print(lista)







