#!/usr/bin/env python


def permutations_generator(objects_list, prefix=[]):
    if len(objects_list) == 1:
        yield prefix + objects_list
    else:
        for i in range(0, len(objects_list)):
            for permutation in permutations_generator(objects_list[:i] + objects_list[i+1:], prefix+[objects_list[i]]):
                yield permutation

in_file = "permutations.in"
out_file = "permutations.out"

with open(in_file, "r") as in_fd:
    length = int(in_fd.readline().strip())

out_fd = open(out_file, "w")
for permutation in permutations_generator([str(i) for i in range(1, length + 1)]):
    out_fd.write(" ".join(permutation) + "\n")
out_fd.close()