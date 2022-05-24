# List Comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lista = []
for x in range(x+1):
    for y in range(y+1):
        for z in range(z+1):
            if x+y+z!=n:
                if [x, y, z] not in lista:
                    lista.append([x, y, z])
print(lista)