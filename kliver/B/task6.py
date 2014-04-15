#!/usr/bin/env python


def get_prev_and_next_vector(vector):
    length = len(vector)
    vector_value = int(vector, 2)
    max_value = 2**length - 1
    if not vector_value:
        return "-", format(1, 'b').zfill(length)
    prev_vector = format(vector_value - 1, 'b').zfill(length)
    if vector_value == max_value:
        return prev_vector, "-"
    next_vector = format(vector_value + 1, 'b').zfill(length)
    return prev_vector, next_vector

in_file = "nextvector.in"
out_file = "nextvector.out"

with open(in_file, "r") as in_fd:
    input_vector = in_fd.readline().strip()

prev_vector, next_vector = get_prev_and_next_vector(input_vector)

out_fd = open(out_file, "w")
out_fd.write(prev_vector + "\n")
out_fd.write(next_vector + "\n")
out_fd.close()