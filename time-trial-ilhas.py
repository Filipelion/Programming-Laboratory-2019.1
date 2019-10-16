def create_graph():
    ilhas, cabos = map(lambda i: int(i), input().split())
    matrix = [[0 for i in range(ilhas)] for j in range(ilhas)]

    for i in range(cabos):
        if i < ilhas:
            u, v, p = map(lambda i: int(i), input().split())
            matrix[u - 1][v - 1] = p
            matrix[v - 1][u - 1] = p
        else:
            trash = input()

    servidor = int(input())

    return (matrix, ilhas, cabos, servidor)

def dijkstra_algorithm(matrix_adj, start, end):

    D = {str(i): float("INF") for i in range(len(matrix_adj))}
    D[str(start)] = 0  # starting with zero in dictionary
    L = [(0, start)]  # make a list starting with zero (cost, vertice)

    while L != []:
        cost, current_vertice = L.pop(0)
        for neighbor in range(len(matrix_adj)):
            if matrix_adj[current_vertice][neighbor]:
                if D[str(neighbor)] > (matrix_adj[current_vertice][neighbor] + cost):
                    D[str(neighbor)] = matrix_adj[current_vertice][neighbor] + cost
                    L.append((D[str(neighbor)], neighbor))
    return D

def ping(temp, island):
    del temp[str(island)]
    print(temp)
    smaller_ping, bigger_ping = max(temp.values())
    print(bigger_ping, smaller_ping)
    return bigger_ping - smaller_ping

# main function

if __name__ == "__main__":
    map_ilhas = create_graph()
    list_servidor = ((map_ilhas[0][map_ilhas[-1] - 1])[:])
    list_servidor.sort()

    for i in list_servidor:
        if i > 0:
            smaller_ping = i
            break

    tracks = dijkstra_algorithm(map_ilhas[0], 0, map_ilhas[-1]-1)
    print(max(tracks.values()) - smaller_ping)
