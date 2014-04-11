__author__ = 'Антон Брагин'

import math
import sys

#Create and return all possible permutations of given length

#Maximum permutation length is set in the task conditions
MAX_PERMUTATION_LENGTH = 8
#Precalculate factorial powers
factorial_powers = [math.factorial(i) for i in range(1, MAX_PERMUTATION_LENGTH + 1)]


class FactorialNumber:
    '''
    Represent number if factorial number system that can be converted to permutation
    '''

    def __init__(self, n):
        self.value = [0]
        i = 0
        while n > 0:
            self.value.append(n % (factorial_powers[i + 1]) // factorial_powers[i])
            n -= n % (factorial_powers[i + 1])
            i += 1

    def increment(self):
        self.value.append(0)
        for i in range(1, len(self.value)):
            if self.value[i] < i:
                self.value[i] += 1
                break
            else:
                self.value[i] = 0

        if self.value[-1] == 0:
            del self.value[-1]

        return self

    def decrement(self):
        for i in range(1, len(self.value)):
            if self.value[i] > 0:
                self.value[i] -= 1
                break
            else:
                self.value[i] = i

def create_permutations(n, writer=sys.stdout):
    fn = FactorialNumber(0)

    for i in range(math.factorial(n)):
        writer.write(' '.join(str(x) for x in get_permutation(n, fn)))
        writer.write('\n')
        fn.increment()

def get_permutation(n, permutation_number):

    inv = permutation_number.value + [0] * (n - len(permutation_number.value))
    sequence = [i + 1 for i in range(n)]

    permutation = []

    for i in range(len(inv)):
        element = inv[len(inv) - i - 1]
        permutation.append(sequence[element])
        del sequence[element]

    return permutation

if __name__ == '__main__':
    #Read input
    with open('permutations.in') as f:
        n = int(f.readline().strip())

        with open('permutations.out', 'w') as fout:
            create_permutations(n, fout)