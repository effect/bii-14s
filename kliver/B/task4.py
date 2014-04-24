#!/usr/bin/env python


def combination_generator(size, objects_list, prefix=[]):
    if len(prefix) == size:
        yield prefix
    else:
        for i in range(0, len(objects_list)):
            for combination in combination_generator(size, objects_list[i+1:], prefix=prefix + [objects_list[i]]):
                yield combination

in_file = "choose.in"
out_file = "choose.out"

with open(in_file, "r") as in_fd:
    length, size = list(map(lambda x: int(x), in_fd.readline().strip().split()))

with open(out_file, "w") as out_fd:
    for combination in combination_generator(size, [str(i) for i in range(1, length + 1)]):
        #print(permutation)
        out_fd.write(" ".join(combination) + "\n")
