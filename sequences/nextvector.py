__author__ = 'Антон Брагин'

def generate_vectors(vector):
    return (decrement(list(vector)), increment(vector))

def increment(vector):
    for i in range(len(vector)):
        if vector[len(vector) - i - 1] == 0:
            vector[len(vector) - i - 1] = 1
            return vector
        else:
            vector[len(vector) - i - 1] = 0
    return None

def decrement(vector):
    for i in range(len(vector)):
        if vector[len(vector) - i - 1] == 1:
            vector[len(vector) - i - 1] = 0
            return vector
        else:
            vector[len(vector) - i - 1] = 1
    return None

if __name__ == '__main__':
    #Read input
    with open('nextvector.in') as f:
        vector = [int(x) for x in f.readline().strip()]

        prev_next = generate_vectors(vector)

        with open('nextvector.out', 'w') as fout:
            if prev_next[0] is not None:
                fout.write(''.join(str(x) for x in prev_next[0]))
            else:
                fout.write('-')
            fout.write('\n')
            if prev_next[1] is not None:
                fout.write(''.join(str(x) for x in prev_next[1]))
            else:
                fout.write('-')
            fout.write('\n')