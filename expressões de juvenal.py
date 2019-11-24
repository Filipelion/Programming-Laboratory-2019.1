class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

class Stack:
    def __init__(self):
        self._start = None
        self._end = None

    def push(self, data):
        new_node = Node(data)
        if self._start == None:
            self._start = new_node
            self._end = new_node
        else:
            new_node.set_next(self._start)
            self._start = new_node

    def pop(self):
        head_node_data = self._start.get_data()
        if self._start is self._end:
            self._start = None
            self._end = None
        else:
            self._start = self._start.get_next()
        return head_node_data

    def is_vazia(self):
        return self._start is None

    def clear_stack(self):
        self._start = None
        self._end = None

def evaluate_expression(stack, expressions):
    for elem in expressions:
        if elem == "{" or elem == "[" or elem == "(":
            # Elementos abrindo sempre validos
            stack.push(elem)
        else:
            if stack.is_vazia():
                # Caso a pilha esteja vazia e entre um elemento fechando
                return "N"

            # Elementos que não fecham diacordo
            elif elem == "}":
                if stack.pop() != "{":
                    return "N"
            elif elem == "]":
                if stack.pop() != "[":
                    return "N"
            elif elem == ")":
                if stack.pop() != "(":
                    return "N"
    else:
        if stack.is_vazia():
            # Todos os elementos foram retirados ou elemento vazio
            return "S"
        else:
            # Elementos retirados, mas ficou algum aberto
            return "N"



obj_stack = Stack()
for i in range(int(input())):
    expressions = input()
    print(evaluate_expression(obj_stack, expressions))
    obj_stack.clear_stack() # Necessario para não criar novo objeto pilha
