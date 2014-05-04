
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


with open('nextchoose.in', 'r') as infile:

    n, k = [int(i) for i in infile.readline().strip().split()]
    data = [int(i) for i in infile.readline().strip().split()]
    array = [0 for i in range(n)]
    for x in data:
        array[x - 1] = 1


with open('nextchoose.out', 'w') as outfile:
    try:
        array = right(array)
        outfile.write(
            ' '.join([str(i + 1) for i in range(n) if array[i] == 1]))
    except TypeError:
        outfile.write('-1')
