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
            line = split_to_int(input())
            self.__matrix[i] = line

        return self.__matrix


def split_to_int(sentence):
    split_value = []
    tmp = ''
    for c in sentence:
        if c == ' ' or c == '  ':
            if tmp != '' or tmp == ' ':
                split_value += [int(tmp)]
                tmp = ''
        else:
            tmp += c
    if tmp:
        split_value += [int(tmp)]

    return split_value

def matrix_zero():
    d = []
    for x in range(l+1):
        line = []
        for x in range(c+1):
            line += [0]
        d += [line]

    return d

def builder(d):
    for i in range(1, l+1):
        for j in range(1, c+1):
            d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + matrix[i-1][j-1]
    return d

def find_bigger(d):
    big = 0
    for i in range(m, l+1):
        for j in range(n, c+1):
            tmp = (d[i][j] - d[i][j-n]) - d[i-m][j] + d[i-m][j-n]
            if tmp > big:
                big = tmp
    return big


# main function

if __name__ == '__main__':
    l, c, m, n = split_to_int(input())
    m1 = Matrix(l, c)
    m1.insert_elements()
    matrix = m1.__repr__()

    zero = matrix_zero()
    mz = builder(zero)
    print(find_bigger(mz))