__author__ = 'Антон Брагин'

import sys

#Print all binary vectors of given length
def create_binary(n, writer=sys.stdout):
    extend([], n, writer=writer)

def extend(sequence, n, writer):
    if n == 0:
        writer.write(''.join(str(x) for x in sequence))
        writer.write('\n')
        return
    extend(sequence + [0], n - 1, writer)
    extend(sequence + [1], n - 1, writer)

if __name__ == '__main__':
    #Read input
    with open('allvectors.in') as f:
        n = int(f.readline().strip())

        with open('allvectors.out', 'w') as fout:
            create_binary(n, writer=fout)

