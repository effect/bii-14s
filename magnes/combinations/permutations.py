def gen_perm(a, p):
    if p < k:
        for i in range(1, k + 1):
            if i not in a:
                a[p] = i
                gen_perm(a, p + 1)
                a[p] = 0
    else:
        outfile.write(str(' '.join([str(i) for i in a])) + '\n')

with open('permutations.in', 'r') as infile:
    k = int(infile.readline().strip())

with open('permutations.out', 'w') as outfile:
    gen_perm([0 for i in range(k)], 0)
