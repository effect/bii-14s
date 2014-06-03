from unittest import TestCase, skip
from sequences.permutations import FactorialNumber, get_permutation
from sequences.nextperm import get_permutation_number

__author__ = 'Антон Брагин'


class TestFactorialNumber(TestCase):

    def test_create(self):

        n = 0
        f = FactorialNumber(n)
        self.assertEqual([0], f.value)

        n = 1
        f = FactorialNumber(n)
        self.assertEqual([0, 1], f.value)

        n = 2
        f = FactorialNumber(n)
        self.assertEqual([0, 0, 1], f.value)

        n = 3
        f = FactorialNumber(n)
        self.assertEqual([0, 1, 1], f.value)

        n = 4
        f = FactorialNumber(n)
        self.assertEqual([0, 0, 2], f.value)

        n = 5
        f = FactorialNumber(n)
        self.assertEqual([0, 1, 2], f.value)

        n = 6
        f = FactorialNumber(n)
        self.assertEqual([0, 0, 0, 1], f.value)

        n = 23
        f = FactorialNumber(n)
        self.assertEqual([0, 1, 2, 3], f.value)

        n = 719
        f = FactorialNumber(n)
        self.assertEqual([0, 1, 2, 3, 4, 5], f.value)

        n = 720
        f = FactorialNumber(n)
        self.assertEqual([0, 0, 0, 0, 0, 0, 1], f.value)

    def test_increment(self):

        n = 0
        f = FactorialNumber(n)
        self.assertEqual([0, 1], f.increment().value)
        self.assertEqual([0, 0, 1], f.increment().value)
        self.assertEqual([0, 1, 1], f.increment().value)
        self.assertEqual([0, 0, 2], f.increment().value)
        self.assertEqual([0, 1, 2], f.increment().value)
        self.assertEqual([0, 0, 0, 1], f.increment().value)
        self.assertEqual([0, 1, 0, 1], f.increment().value)
        self.assertEqual([0, 0, 1, 1], f.increment().value)

        n = 719
        f = FactorialNumber(n)
        self.assertEqual([0, 0, 0, 0, 0, 0, 1], f.increment().value)

    def test_decrement(self):
        for n in range(1, 100):
            f = FactorialNumber(n)
            fval = f.value
            f.increment().decrement()
            self.assertEqual(fval, f.value)

    def test_permutation(self):

        n = 5
        f = FactorialNumber(0)
        p = get_permutation(n, f)
        self.assertEqual([1, 2, 3, 4, 5], p)

        f.increment()
        p = get_permutation(n, f)
        self.assertEqual([1, 2, 3, 5, 4], p)

        n = 719
        f = FactorialNumber(n)
        p = get_permutation(6, f)
        self.assertEqual([6, 5, 4, 3, 2, 1], p)

    def test_get_permutation_number(self):
        p = [1, 2, 3, 4, 5]
        p = [5, 4, 3, 2, 1]
        p = [1, 2, 3]

        self.assertEqual([0, 0, 0], get_permutation_number([1, 2, 3]).value)
        self.assertEqual([0, 1, 2], get_permutation_number([3, 2, 1]).value)

        p = [1, 2, 3]
        pn = get_permutation_number(p)
        self.assertEqual(p, get_permutation(3, pn))

        p = [3, 2, 1]
        pn = get_permutation_number(p)
        self.assertEqual(p, get_permutation(3, pn))

        p = [5, 2, 4, 3, 1]
        pn = get_permutation_number(p)
        self.assertEqual(p, get_permutation(5, pn))
