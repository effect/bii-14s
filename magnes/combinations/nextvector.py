
def left(x):
    x = list([int(i) for i in x])[::-1]
    if x[0] == 1:
        x[0] = 0
    else:
        for i in range(len(x)):
            if x[i] == 1:
                x[i] = 0
                for z in range(len(x[:i])):
                    x[z] = 1
                break
    return ''.join([str(i) for i in x[::-1]])


def right(x):
    x = list([int(i) for i in x])[::-1]
    if x[0] == 0:
        x[0] = 1
    else:
        for i in range(len(x)):
            if x[i] == 0:
                x[i] = 1
                for z in range(len(x[:i])):
                    x[z] = 0
                break
    return ''.join([str(i) for i in x[::-1]])


with open('nextvector.in', 'r') as infile:

    x = infile.readline().strip()

    a = '-'
    b = '-'

    if set(list(x)) != set(['0']):
        a = left(x)

    if set(list(x)) != set(['1']):
        b = right(x)

with open('nextvector.out', 'w') as outfile:
    outfile.write(a + '\n' + b)
