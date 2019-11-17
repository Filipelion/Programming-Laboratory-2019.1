def partition(lista, menor, maior):
    i = (menor - 1)
    pivot = lista[maior]

    for j in range(menor, maior):
        if lista[j] >= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[maior] = lista[maior], lista[i + 1]
    return (i + 1)

def quicksort(lista, menor, maior):
    if menor < maior:
        q = partition(lista, menor, maior)
        quicksort(lista, menor, q - 1)
        quicksort(lista, q + 1, maior)

def ordenar_nome(lista):
    for i in range(n):
        for j in range(n):
            if lista[i][1] == lista[j][1]:
                if lista[i][2] < lista[j][2]:
                    lista[i], lista[j] = lista[j], lista[i]

def classificar_planos(plano):
    lista = [('premium', 6), ('diamante', 5), ('ouro', 4), ('prata', 3), ('bronze', 2), ('resto', 1)]
    for i in lista:
        if i[0] == plano:
            return i[1]

def split_to_list(sentence):
    split_value = []
    tmp = ''
    for c in sentence:
        if c == ' ':
            split_value += [tmp]
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value += [tmp]

    return split_value

n = int(input())
fila_prioridade = [None] * n

for i in range(n):
    nome, plano, urgencia = split_to_list(input())
    int_plano = classificar_planos(plano)
    fila_prioridade[i] = (int_plano, int(urgencia), nome)

quicksort(fila_prioridade, 0, n - 1)
ordenar_nome(fila_prioridade)
[print(i[2]) for i in fila_prioridade]
