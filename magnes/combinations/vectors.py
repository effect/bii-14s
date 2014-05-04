def gen_perm(a, p):
    if k == 0:
        return 0
    if p < k:
        a[p] = 0
        gen_perm(a, p + 1)

        if a[p - 1] != 1:
            a[p] = 1
            gen_perm(a, p + 1)

    else:
        output.append(str(''.join([str(i) for i in a])) + '\n')

with open('vectors.in', 'r') as infile:
    k = int(infile.readline().strip())

with open('vectors.out', 'w') as outfile:
    output = []
    gen_perm([0 for i in range(k)], 0)
    gen_perm([1 for i in range(k)], 1)

    output = sorted(list(set(output)))
    outfile.write(str(len(output)) + '\n')
    for x in output:
        outfile.write(x)
