#!/usr/bin/env python

in_file = "allvectors.in"
out_file = "allvectors.out"

in_fd = open(in_file, "r")
length = int(in_fd.readline().strip())
in_fd.close()

out_fd = open(out_file, "w")
for i in range(0, 2**length):
    out_fd.write(format(i, 'b').zfill(length) + "\n")
out_fd.close()