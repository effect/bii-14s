#!/usr/bin/env python


def get_previous_permutation(current_permutation, length):
    for i in range(1, length):
        if current_permutation[-i] < current_permutation[-(i+1)]:
            break
    else:
        return [0 for i in range(0, length)]
    i += 1
    prefix = current_permutation[:-i]
    suffix = sorted(current_permutation[-i:], reverse=True)
    for j in range(0, i):
        if suffix[j] < current_permutation[-i]:
            insert = suffix.pop(j)
            break
    return prefix + [insert] + suffix


def get_next_permutation(current_permutation, length):
    for i in range(1, length):
        if current_permutation[-i] > current_permutation[-(i+1)]:
            break
    else:
        return [0 for i in range(0, length)]
    i += 1
    prefix = current_permutation[:-i]
    suffix = sorted(current_permutation[-i:])
    for j in range(0, i):
        if suffix[j] > current_permutation[-i]:
            insert = suffix.pop(j)
            break
    return prefix + [insert] + suffix

in_file = "nextperm.in"
out_file = "nextperm.out"

with open(in_file, "r") as in_fd:
    length = int(in_fd.readline().strip())
    current_permutation = list(map(lambda x: int(x), in_fd.readline().strip().split()))

previous_permutation = get_previous_permutation(current_permutation, length)
next_permutation = get_next_permutation(current_permutation, length)

with open(out_file, "w") as out_fd:
    out_fd.write(" ".join(list(map(lambda x: str(x), previous_permutation))) + "\n")
    out_fd.write(" ".join(list(map(lambda x: str(x), next_permutation))) + "\n")