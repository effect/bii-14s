with open('airplane.in', 'r') as infile:
    s, n, a = [int(x) for x in infile.readline().strip().split()]
    p = sum([int(x) for x in infile.readline().strip().split()])

    if a >= 1000:
        x = 'Impossible'
    else:
        x = (s + p) * a / (1000 - a)


with open('airplane.out', 'w') as outfile:
    outfile.write(str(x))
