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


def bloody_night_rec(i, j):
    global sheeps, wolfs

    try:
        if matrix[i][j] == '#' or matrix[i][j] == 0:
            return False

        elif matrix[i][j] == 'k':
            sheeps += 1

        elif matrix[i][j] == 'v':
            wolfs += 1

    except IndexError:
        return

    matrix[i][j] = 0
    bloody_night_rec(i - 1, j)
    bloody_night_rec(i, j + 1)
    bloody_night_rec(i + 1, j)
    bloody_night_rec(i, j - 1)


# main function
if __name__ == "__main__":
    row, col = split_to_int(input())
    matrix = []
    m2 = Matrix(row, col)
    m2.insert_elements()
    matrix = m2.__repr__()

    total_sheeps, total_wolfs = 0, 0
    sheeps, wolfs = 0, 0

    for x in range(row):
        for y in range(col):
            if matrix[x][y] != '#' or matrix[x][y] != 0:
                sheeps, wolfs = 0, 0
                bloody_night_rec(x, y)
                if sheeps > wolfs:
                    total_sheeps += sheeps
                else:
                    total_wolfs += wolfs

    print(total_sheeps, total_wolfs)
