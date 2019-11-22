def create_graph():
    global n
    n, start, end = split_to_int(input())
    graph = [[] for j in range(n)]

    for j in range(n-1):
        a, b = split_to_int(input())
        graph[a-1].append((b-1, 1))
        graph[b-1].append((a-1, 1))

    return (graph, start, end)

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

def find_path(graph, start, end):
    key = []
    visited = [None for i in range(n)]

    for i in graph[start]:
        key += [i]
        visited[i[0]] = 1
    vertex = key[0]

    key.pop(0)
    while vertex[0] != end:
        for i in graph[vertex[0]]:
            if visited[i[0]] is None:
                visited[i[0]] = 1
                key.append((i[0], vertex[1] + i[1]))
        vertex = key[0]
        key.pop(0)

    return vertex[1]

# main function
if __name__ == "__main__":
    graph, start, end = create_graph()
    output = find_path(graph, start - 1, end - 1)
    print(output)
