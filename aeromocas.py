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

    def size(self):
        tmp = self.__head
        count = 0

        while tmp is not None:
            count += 1
            tmp = tmp.getNext()
        return count

    def isEmpty(self):
        if self.__head is None:
            return True
        else:
            return False

    def printstack(self):

        print("stack elements are:")
        temp = self.getHead()
        while temp is not None:
            print(temp.getData(), end="->")
            temp = temp.getNext()


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
    n, m = split_to_int(input()) # fist line
    graph = [[] for j in range(n)]


    for j in range(m):
        a, b, dist = split_to_int(input())
        graph[a] += [(b, dist)]
        graph[b] += [(a, dist)]

    return (graph, n, m)

def dijkstra_algorithm(vertex, start):
    Q = Queue() # FILA
    Q.push((0, start))
    dist = [float("INF")]*city # FILA
    dist[start] = 0


    while not Q.isEmpty():
        cost, current_vertice = Q.my_pop()

        for neighbor in vertex[current_vertice]:

            if dist[neighbor[0]] > neighbor[1] + cost:
                dist[neighbor[0]] = neighbor[1] + cost
                Q.push((dist[neighbor[0]], neighbor[0]))



    return max(dist)

# main function
if __name__ == "__main__":
    vertex, city, voos = create_graph()

    menor = float("INF")
    for i in range(city):
        result = dijkstra_algorithm(vertex, i)
        if result < menor and result != 0:
            menor = result
    print(menor)
