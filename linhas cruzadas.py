def conta_cruzamentos(lista_valores, int_n):
    inv_lista_valores = lista_valores[::-1]
    cruza = 0
    anterior = int_n - 2
    constante = int_n - 1


    for i in inv_lista_valores:
        for j in range(int_n - 1):
            valor = lista_valores[anterior]
            if anterior < 0:
                break
            if int(i) < int(valor):
                cruza += 1
            anterior -= 1
        constante -= 1
        anterior = constante
    return cruza

def split_to_int(sentence):
    split_value = []
    tmp = ''
    for c in sentence:
        if c == ' ':
            split_value += [int(tmp)]
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value += [int(tmp)]

    return split_value

int_n = int(input())
lista_valores = split_to_int(input())
print(conta_cruzamentos(lista_valores, int_n))
