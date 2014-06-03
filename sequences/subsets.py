__author__ = 'Антон Брагин'

def generate_subsets(n):
    elements = [x + 1 for x in range(n)]
    subsets = []
    extend_subset([], elements, -1, subsets)
    return subsets

def extend_subset(subset, elements, last, subsets):
    #if len(subset) > 0:
    subsets.append(subset)
    for e in elements:
        if e > last:
            extend_subset(subset + [e], elements, e, subsets)

if __name__ == '__main__':
    #Read input
    with open('subsets.in') as f:
        n = int(f.readline().strip())

        subsets = generate_subsets(n)

        with open('subsets.out', 'w') as fout:
            for s in subsets:
                fout.write(' '.join(str(x) for x in s))
                fout.write('\n')
