def gen_perm(a, p):
    if p < k:
        a[p] = 0
        gen_perm(a, p + 1)
        a[p] = 1
        gen_perm(a, p + 1)
    else:
        outfile.write(str(''.join([str(i) for i in a])) + '\n')

with open('allvectors.in', 'r') as infile:
    k = int(infile.readline().strip())

with open('allvectors.out', 'w') as outfile:
    gen_perm([2 for i in range(k)], 0)
