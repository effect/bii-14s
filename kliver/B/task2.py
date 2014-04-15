#!/usr/bin/env python


def fibbonachi(n):
    if n < 3:
        return 1
    return fibbonachi(n-1) + fibbonachi(n-2)


def generate_binary_vectors_no_neighbor_ones(length, prefix=[]):
    if len(prefix) == length:
        yield prefix
    else:
        for vector in generate_binary_vectors_no_neighbor_ones(length, prefix + ["0"]):
            yield vector
        if not prefix or prefix[-1] != "1":
            for vector in generate_binary_vectors_no_neighbor_ones(length, prefix + ["1"]):
                yield vector

in_file = "vectors.in"
out_file = "vectors.out"

with open(in_file, "r") as in_fd:
    length = int(in_fd.readline().strip())

with open(out_file, "w") as out_fd:
    out_fd.write(str(fibbonachi(length + 2)) + "\n")
    for vector in generate_binary_vectors_no_neighbor_ones(length):
        out_fd.write("".join(vector) + "\n")
