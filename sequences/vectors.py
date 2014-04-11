__author__ = 'Антон Брагин'

#Print all vectors of length n without two consecutive ones

def create_vectors(n):
    vectors = []
    extend([], n, 0, vectors)
    return vectors

def extend(sequence, n, last, vectors):
    if n == 0:
        vectors.append(sequence)
        return
    extend(sequence + [0], n - 1, 0, vectors)
    if last != 1:
        extend(sequence + [1], n - 1, 1, vectors)

if __name__ == '__main__':
    #Read input
    with open('vectors.in') as f:
        n = int(f.readline().strip())

    vectors = create_vectors(n)

    with open('vectors.out', 'w') as fout:
        fout.write(str(len(vectors)))
        fout.write('\n')

        for v in vectors:
            fout.write(''.join(str(x) for x in v))
            fout.write('\n')