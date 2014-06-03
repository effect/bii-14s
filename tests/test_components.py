from unittest import TestCase

from graphs import components_fast as components


__author__ = 'Антон Брагин'

import random
import datetime


class TestComponents(TestCase):

    def test_time(self):
        n = 100000
        m = 200000

        self.test_file = 'test.in'

        with open(self.test_file, 'w') as f:
            f.write(str(n))
            f.write(' ')
            f.write(str(m))
            f.write('\n')

            for e in range(m):
                f.write(str(random.randint(1, n)))
                f.write(' ')
                f.write(str(random.randint(1, n)))
                f.write('\n')

        print('Test file created. n = {}, m = {}. Starting testing...'.format(n, m))
        start = datetime.datetime.now()

        graph = components.create_graph(self.test_file)
        print('Graph created...')

        #print('Graph:\n{}'.format(graph))

        ncomp = components.get_components(graph)
        components.print_components('test.out', graph, ncomp)

        end = datetime.datetime.now()

        #print('Graph:\n{}'.format(graph))

        print('Total time: {}'.format(end - start))