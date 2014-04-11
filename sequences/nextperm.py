__author__ = 'Антон Брагин'

import math
import sys

#Create and return previous and next permutation

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

        return self

def get_permutation(n, permutation_number):

    inv = permutation_number.value + [0] * (n - len(permutation_number.value))
    sequence = [i + 1 for i in range(n)]

    permutation = []

    for i in range(len(inv)):
        element = inv[len(inv) - i - 1]
        permutation.append(sequence[element])
        del sequence[element]

    return permutation

def get_permutation_number(permutation):

    factorial = []
    for i in range(len(permutation)):
        number_of_inversions = 0
        for j in range(i, len(permutation)):
            if permutation[j] < permutation[i]:
                number_of_inversions += 1
        factorial.append(number_of_inversions)

    fn = FactorialNumber(0)
    factorial.reverse()
    fn.value = factorial

    return fn

#-------------------------------------------------------Execution-------------------------------------------------------

if __name__ == '__main__':
    #Read input
    with open('nextperm.in') as f:
        n = int(f.readline().strip())
        permutation = [int(x) for x in f.readline().split()]

        fn = get_permutation_number(permutation)

        with open('nextperm.out', 'w') as fout:

            down = get_permutation_number(permutation).decrement()

            #Write previous
            if sum(fn.value) != 0:
                fout.write(' '.join(str(x) for x in get_permutation(n, down)))
            else:
                fout.write(' '.join(['0'] * n))

            fout.write('\n')

            up = get_permutation_number(permutation).increment()

            #Write next
            if len(up.value) == len(fn.value):
                fout.write(' '.join(str(x) for x in get_permutation(n, up)))
            else:
                fout.write(' '.join(['0'] * n))