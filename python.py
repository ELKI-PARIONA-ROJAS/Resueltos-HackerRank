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

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    primero = -999999
    segundo = -999999
    for i in arr:
        if i > primero:
            primero = i
    for j in arr:
        if j > segundo and j != primero:
            segundo = j
    print(segundo)

