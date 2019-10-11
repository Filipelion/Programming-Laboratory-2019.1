#numero de olhas e numero de cabos

def create_graph():
    ilhas, cabos = map(lambda i: int(i), input().split()) # fist line
    graph = [[] for j in range(n)]

    for j in range(ilhas-1):
        u, v, p = map(lambda i: int(i), input().split())
        graph[u-1].append((v-1, p))
        graph[v-1].append((u-1, p))

    servidor = int(input()) # inteiro S

    return (graph, ilhas, cabos, servidor)

'''
Depois que a função retorna a tupla com o grafo e a quantidade de ilhas, cabos e servidores.
O proximo passo e traçar o caminho mais do nó com o maior e do menor ping do servidor percorrendo todos os nós atraves de uma busca em profundidade.
'''