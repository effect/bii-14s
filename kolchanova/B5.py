infile = open ('subsets.in', 'r')
outfile = open ('subsets.out', 'w')

n = int(infile.readline().strip())

limit = range (1, n+1)
subsets = []


def generate_subsets(x, y):
    subsets.append(' '.join(str(i) for i in x))
    for val in limit:
        if val > y:
            generate_subsets(x + [val], val)
    return subsets


string = []
output = generate_subsets(string, 0)
 
outfile.write('\n'.join(output))

infile.close()
outfile.close()