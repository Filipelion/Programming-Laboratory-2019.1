'''
Aluno: Filipe de Freitas Lima
Data: 23/10/19

Resumo:

Implementei o algoritmo de dijkstra utilizando listas de adjacências.
Construi as classes Nó e fila. A classe fila duplamente encadeada possui os
metodos push, pop e emputy. Com isso evitei de utilizar as funções da
biblioteca padrão do python.
'''


class Node:
    def __init__(self, data, next=None, previous=None):
        self.__data = data
        self.__next = next
        self.__previous = previous

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def getPrevious(self):
        return self.__previous

    def setData(self, data):
        self.__data = data

    def setNext(self, next):
        self.__next = next

    def setPrevious(self, previous):
        self.__previous = previous


class Queue:
    def __init__(self, head=None, last=None):
        self.__head = head
        self.__last = last

    def getHead(self):
        return self.__head

    def getLast(self):
        return self.__last

    def setHead(self, head):
        self.__head = head

    def setLast(self, last):
        self.__last = last

    def push(self, data):
        new_node = Node(data)
        if not self.isEmpty():
            new_node.setNext(self.__head)
            self.__head.setPrevious(new_node)
        self.__head = new_node

    def my_pop(self):
        if self.__head is None:
            return None
        else:
            tmp = self.getHead()
            self.__head = self.__head.getNext()
            tmp.setPrevious(None)
            return tmp.getData()

    def isEmpty(self):
        if self.__head is None:
            return True
        else:
            return False


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


def create_graph():
    n, m = split_to_int(input())  # fist line
    graph = [[] for j in range(n)]

    for j in range(m):
        a, b, dist = split_to_int(input())
        graph[a] += [(b, dist)]
        graph[b] += [(a, dist)]

    return (graph, n, m)


def dijkstra_algorithm(vertex, start):
    Q = Queue()
    Q.push((0, start))
    dist = [float("INF")] * city  # FILA
    dist[start] = 0

    while not Q.isEmpty():
        cost, current_vertice = Q.my_pop()

        for neighbor in vertex[current_vertice]:

            if dist[neighbor[0]] > neighbor[1] + cost:
                dist[neighbor[0]] = neighbor[1] + cost
                Q.push((dist[neighbor[0]], neighbor[0]))

    return dist


# main function
if __name__ == "__main__":
    vertex, city, voos = create_graph()

    result = [0 for i in range(city)]

    for i in range(city):
        d = dijkstra_algorithm(vertex, i)


        for j in range(city):
            if result[j] < d[j]:
                result[j] = d[j]



    smaller = float("INF")
    for i in result:
        if i < smaller:
            smaller = i

    print(smaller)
