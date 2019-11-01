import sys
sys.setrecursionlimit(100000) # alteração no tempo de recursão

class Matrix:
    def __init__(self, num_rows, num_columns):
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__matrix = [None]

    def __repr__(self):
        return self.__matrix

    def insert_elements(self):
        # insert lines to matrix

        self.__matrix = self.__matrix * self.__num_rows
        for i in range(self.__num_rows):
            line = split_to_str(input())
            self.__matrix[i] = line

        return self.__matrix


def bloody_night(pos):
    v, k = 0, 0

    if pos in forPass:

        if forPass[pos] == 'k':
            k += 1
        elif forPass[pos] == 'v':
            v += 1

        del forPass[pos]
        i, j = pos

        wolf, sheep = bloody_night((i - 1, j))
        v += wolf
        k += sheep
        wolf, sheep = bloody_night((i + 1, j))
        v += wolf
        k += sheep
        wolf, sheep = bloody_night((i, j - 1))
        v += wolf
        k += sheep
        wolf, sheep = bloody_night((i, j + 1))
        v += wolf
        k += sheep
        return v, k
    else:
        return v, k

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


# main function
if __name__ == "__main__":
    global matrix
    row, col = split_to_int(input())
    m2 = Matrix(row, col)
    m2.insert_elements()
    matrix = m2.__repr__()




    forPass = {}

    for i in range(row):
        for j in range(col):
            dot = matrix[i][j]
            if dot != '#':
                forPass[(i, j)] = dot

    total_wolfs = 0
    total_sheeps = 0

    while len(forPass) != 0:
        key = [x for x in forPass.keys()][0]

        v, k = bloody_night(key)

        if v >= k:
            total_wolfs += v
        else:
            total_sheeps += k
    print(total_sheeps, total_wolfs)