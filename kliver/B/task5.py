#!/usr/bin/env python


def subsets_generator(objects_list, prefix=[]):
    yield prefix
    for i in range(0, len(objects_list)):
        for subset in subsets_generator(objects_list[i+1:], prefix=prefix + [objects_list[i]]):
            yield subset

in_file = "subsets.in"
out_file = "subsets.out"

with open(in_file, "r") as in_fd:
    length = int(in_fd.readline().strip())

with open(out_file, "w") as out_fd:
    for subset in subsets_generator([str(i) for i in range(1, length + 1)]):
        #print(permutation)
        out_fd.write(" ".join(subset) + "\n")