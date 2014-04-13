from unittest import TestCase, skip

__author__ = 'Антон Брагин'

from sequences import nextperm_fast

class TestPermutations(TestCase):

    def test_generate_next(self):

        permutation = [1, 2, 3, 4]
        next = nextperm_fast.generate_next(permutation)
        self.assertEqual([1, 2, 4, 3], next)

        permutation = [3, 2, 4, 1]
        next = nextperm_fast.generate_next(permutation)
        self.assertEqual([3, 4, 1, 2], next)

        permutation = [1, 4, 3, 2]
        next = nextperm_fast.generate_next(permutation)
        self.assertEqual([2, 1, 3, 4], next)

        permutation = [4, 3, 2, 1]
        next = nextperm_fast.generate_next(permutation)
        self.assertEqual(None, next)

    def test_generate_previous(self):

        permutation = [1, 2, 3, 4]
        next = nextperm_fast.generate_previous(permutation)
        self.assertEqual(None, next)

        permutation = [2, 3, 4, 1]
        next = nextperm_fast.generate_previous(permutation)
        self.assertEqual([2, 3, 1, 4], next)

        permutation = [4, 3, 2, 1]
        next = nextperm_fast.generate_previous(permutation)
        self.assertEqual([4, 3, 1, 2], next)

        permutation = [2, 1, 3, 4]
        next = nextperm_fast.generate_previous(permutation)
        self.assertEqual([1, 4, 3, 2], next)
