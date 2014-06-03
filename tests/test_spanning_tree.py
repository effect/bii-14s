from unittest import TestCase

from graphs import spanning_tree


__author__ = 'Антон Брагин'


class TestSpanningTree(TestCase):

    def test_spanning_tree(self):

        n, edges = spanning_tree.parse_input('spantree.in')
        tree_size = spanning_tree.kruskal(n, edges)
        self.assertEqual(2, tree_size)

        n, edges = spanning_tree.parse_input('spantree1.in')
        tree_size = spanning_tree.kruskal(n, edges)
        self.assertEqual(0, tree_size)

        n, edges = spanning_tree.parse_input('spantree2.in')
        tree_size = spanning_tree.kruskal(n, edges)
        self.assertAlmostEqual(4.2426406871192851464050661726291, tree_size)
