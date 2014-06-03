__author__ = 'Антон Брагин'

def generate_combinations(n, k):
    elements = [i + 1 for i in range(n)]
    combinations = []
    extend([], elements, k, -1, combinations)

    return combinations

def extend(combination, elements, k, last, combinations):
    if len(elements) == 0 or k == 0:
        combinations.append(combination)
    else:
        for e in elements:
            if e > last:
                extend(combination + [e], elements, k - 1, e, combinations)

if __name__ == '__main__':
    #Read input
    with open('choose.in') as f:
        n, k = tuple(int(x) for x in f.readline().strip().split())

        combinations = generate_combinations(n, k)

        with open('choose.out', 'w') as fout:
            for c in combinations:
                fout.write(' '.join(str(x) for x in c))
                fout.write('\n')