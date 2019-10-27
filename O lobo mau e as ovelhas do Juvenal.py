'''
Aluno: Filipe de Freitas Lima
Data: 27/10/19

Resumo:

Implementei o algoritmo utilizando recursões;
Construi as classes Matrix e search que possuem metodos para criar o campo e buscar as informações contidas.
'''


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

class search(Matrix):
    def __init__(self, num_rows, num_columns):
        super().__init__(num_rows, num_columns) # class Matrix
        self.__num_rows = num_rows
        self.__num_columns = num_columns



    def field(self, m, rows, columns):
        global sheeps, wolves
        num_ovelhas = 0
        num_lobos = 0
        for i in range(rows):
            for j in range(columns):

                if m[i][j] != '#':
                    sheeps = 0
                    wolves = 0
                    self.bloody_night(m, i,j)
                    if (sheeps or wolves) > 0:

                        if sheeps > wolves:
                            num_ovelhas += sheeps
                        elif wolves >= sheeps:
                            num_lobos += wolves

        return num_ovelhas, num_lobos

    def bloody_night(self, matrix, i, j):
        global sheeps, wolves
        value = matrix[i][j]

        if value is '#':
            return False

        elif value is 'k':
            sheeps += 1
            matrix[i][j] = '#'

        elif value is 'v':
            wolves += 1
            matrix[i][j] = '#'

        matrix[i][j] = '#'  # to '.'

        self.bloody_night(matrix, i, j + 1)  # go ahead
        self.bloody_night(matrix, i, j - 1)  # go back
        self.bloody_night(matrix, i - 1, j)  # go up
        self.bloody_night(matrix, i + 1, j)  # go down



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
    row, col = split_to_int(input())
    m2 = search(row, col)
    m2.insert_elements()
    matrix = m2.__repr__()
    sheeps, wolves = m2.field(matrix, row, col)
    print(sheeps, wolves)
