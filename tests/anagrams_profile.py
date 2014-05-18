__author__ = 'Антон Брагин'

import cProfile
from problemsc.anagrams import run
from sequences import nextperm_fast

def gen_perm():
    permutation = [x + 1 for x in range(9)]
    for _ in range(362880):
        permutation = nextperm_fast.generate_next(permutation)

cProfile.run('run()')
#cProfile.run('gen_perm()')