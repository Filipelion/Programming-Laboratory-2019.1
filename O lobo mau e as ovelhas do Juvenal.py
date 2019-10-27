import sys
sys.setrecursionlimit(10000)

class Matrix:
    def __init__(self, num_rows, num_columns):
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__matrix = []

    def __repr__(self):
        return self.__matrix

    def insert_elements(self):
        # insert lines to matrix

        self.__matrix = self.__matrix * self.__num_rows
        for i in range(self.__num_rows):
            line = split_to_str(input())
            self.__matrix.insert(i, line)

        return self.__matrix


def split_to_str(sentence):
    split_value = []
    for c in sentence:
        split_value += [c]

    return split_value


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


def bloody_night(matrix, i, j):
    global ovelhas, lobos
    value = matrix[i][j]

    if value is '#':
        return False

    elif value is 'k':
        ovelhas += 1
        matrix[i][j] = '#'

    elif value is 'v':
        lobos += 1
        matrix[i][j] = '#'

    matrix[i][j] = '#' # to '.'

    bloody_night(matrix, i, j + 1)  # go ahead
    bloody_night(matrix, i, j - 1)  # go back
    bloody_night(matrix, i - 1, j)  # go up
    bloody_night(matrix, i + 1, j)  # go down


# main function
if __name__ == "__main__":
    row, col = split_to_int(input())
    m1 = Matrix(row, col)
    m1.insert_elements()
    ma = m1.__repr__()

    num_ovelhas = 0
    num_lobos = 0
    for i in range(row):
        for j in range(col):

            if ma[i][j] != '#':
                ovelhas = 0
                lobos = 0

                bloody_night(ma, i, j)
                if (ovelhas or lobos) > 0:

                    if ovelhas > lobos:
                        num_ovelhas += ovelhas
                    elif lobos >= ovelhas:
                        num_lobos += lobos


    print(num_ovelhas, num_lobos)
