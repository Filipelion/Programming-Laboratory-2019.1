def backpack(max_capacity, weight, value, num_objects):
    degrade = num_objects - 1
    if num_objects == 0 or max_capacity == 0: # Caso base
        return 0

    if (weight[degrade] > max_capacity):
        return backpack(max_capacity, weight, value, degrade)
    else:
        return max_two(value[degrade] + backpack(max_capacity - weight[degrade], weight, value, degrade), backpack(max_capacity, weight, value, degrade))

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

def max_two(x, y):
    if x >= y:
        return x
    else:
        return y


if __name__ == '__main__':

    num_objects, maxweight = split_to_int(input())
    weight = [None] * num_objects
    value = [None] * num_objects

    for i in range(num_objects):
        items = split_to_int(input())
        weight[i] = items[0]
        value[i] = items[1]

    print(backpack(maxweight, weight, value, num_objects))
