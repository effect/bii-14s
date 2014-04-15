#!/usr/bin/env python


def get_next_combination(current_combination, length, size):
    for i in range(1, size + 1):
        if current_combination[-i] != length - i + 1:
            break
    else:
        return [-1]
    prefix = current_combination[:-i]
    for j in range(1, i + 1):
        prefix.append(current_combination[-i] + j)
    return prefix

in_file = "nextchoose.in"
out_file = "nextchoose.out"

with open(in_file, "r") as in_fd:
    length, size = list(map(lambda x: int(x), in_fd.readline().strip().split()))
    current_combination = list(map(lambda x: int(x), in_fd.readline().strip().split()))

next_combination = get_next_combination(current_combination, length, size)

with open(out_file, "w") as out_fd:
    out_fd.write(" ".join(list(map(lambda x: str(x), next_combination))) + "\n")