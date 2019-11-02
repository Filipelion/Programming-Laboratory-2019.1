def main():
    global matrix
    row, col = split_to_int(input())

    matrix = matrix(row, col)

    for i in range(1, row + 1):
        n = input()
        for j in range(1, col + 1):
            matrix[i][j] = n[j - 1]

    return row, col

def matrix(i, j):
    matrix = []
    for i in range(i + 2):
        matrix += [['0'] * (j + 2)]
    return matrix


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

def explore(i, j):
    value = matrix[i][j]
    global size_ship, size_destroyed, val

    if value is '#':
        size_ship += 1
        matrix[i][j] = 'v'

        val += 1
    elif value is 'd':

        size_ship += 1
        size_destroyed += 1
        matrix[i][j] = 0

        val += 1
    else:
        return 0

    matrix[i][j] = 0
    explore(i, j + 1)
    explore(i, j - 1)
    explore(i - 1, j)
    explore(i + 1, j)

def shots(matrix):
    n = int(input())
    for n in range(n):
        i, j = split_to_int(input())
        if matrix[i][j] == '#':
            matrix[i][j] = 'd'

# main function
if __name__ == "__main__":
    row, col = main()
    shots(matrix)
    wrecked_ships = 0

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if matrix[i][j] != '.' and matrix[i][j] != 0:
                size_destroyed = 0
                size_ship = 0
                val = 0
                explore(i, j)

                if val > 0:
                    if size_ship - size_destroyed == 0:
                        wrecked_ships += 1
    print(wrecked_ships)
