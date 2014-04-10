from unittest import TestCase

from graphs.spanning_tree import DSU


__author__ = 'Антон Брагин'

dsu_size = 10

class TestDSU(TestCase):

    def setUp(self):
        self.dsu = DSU(dsu_size)

    def test_find_set(self):
        #Test that in the beginnng every element is the parent of itself
        for i in range(dsu_size):
            self.assertEqual(i, self.dsu.find_set(i))

        #Unite and check
        self.dsu.union_sets(0, 1)
        self.assertEqual(self.dsu.find_set(0), self.dsu.find_set(1))

        self.dsu.union_sets(5, 9)
        self.assertEqual(self.dsu.find_set(5), self.dsu.find_set(9))

        self.assertNotEqual(self.dsu.find_set(0), self.dsu.find_set(5))
        self.assertNotEqual(self.dsu.find_set(0), self.dsu.find_set(3))
        self.assertNotEqual(self.dsu.find_set(7), self.dsu.find_set(9))

        self.dsu.union_sets(5, 7)
        self.dsu.union_sets(0, 9)

        print(self.dsu.parent)

