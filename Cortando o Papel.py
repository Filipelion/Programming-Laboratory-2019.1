lista = [0]
n = int(input())
x = ""
qtd, resp = 2, 2

for i in input().split():
    if i != x:
        lista.append(int(i))
    x = i
lista.append(0)

pico_vale = []

for j in range(1, len(lista) - 1):

    if (lista[j] > lista[j - 1]) and (lista[j] > lista[j + 1]):
        pico_vale.append((lista[j], -1))

    if (lista[j] < lista[j - 1]) and (lista[j] < lista[j + 1]):
        pico_vale.append((lista[j], 1))

# Quantidade minima de papeis cortados começa com 2
pico_vale.sort()

for i in pico_vale:
    qtd += i[1]
    resp = max(qtd, resp)

print(resp)