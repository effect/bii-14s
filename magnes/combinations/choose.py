
def right(x):
    if x[-1] == 0:
        x = x[::-1]
        for i in range(len(x)):
            if x[i] == 1:
                x[i], x[i - 1] = x[i - 1], x[i]
                return x[::-1]
    else:
        x = x[::-1]
        for i in range(len(x) - 1):
            if x[i] == 0 and x[i + 1] == 1:
                x[i], x[i + 1] = x[i + 1], x[i]
                x = x[:i][::-1] + x[i:]
                return x[::-1]


def gen_all(array):
    while array != end:
        array = list(right(array))
        yield ' '.join([str(i + 1) for i in range(len(array)) if array[i] == 1])


with open('choose.in', 'r') as infile:

    n, k = [int(i) for i in infile.readline().strip().split()]
    array = [0 for x in range(n)]
    for x in range(k):
        array[x] = 1
    end = [0 for x in range(n)]
    for x in range(k):
        end[-x - 1] = 1


with open('choose.out', 'w') as outfile:
    outfile.write(
        ' '.join([str(i + 1) for i in range(len(array)) if array[i] == 1]) + '\n')
    for x in gen_all(array):
        outfile.write(x + '\n')
