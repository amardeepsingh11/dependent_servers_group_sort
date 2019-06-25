"""
    The module is for sorting the servers information contained in a CSV
"""
import unittest
from dependent_servers_group_sort import Graph

class TestGraph(unittest.TestCase):
    """
        The module is for sorting the servers information contained in a CSV
    """
    def setUp(self):
        """
            Description in the declaration
        """
        self.graph_1 = Graph()
        self.graph_2 = Graph(11)

    def tearDown(self):
        """
            Description in the declaration
        """

    def test_vertices(self):
        """
            Description in the declaration
        """
        self.assertEqual(self.graph_1.V, 0)
        self.assertEqual(self.graph_2.V, 11)

    def test_graphs(self):
        """
            Description in the declaration
        """
        self.assertEqual(len(self.graph_1.graph), 0)
        self.assertEqual(len(self.graph_2.graph), 0)

    def test_addEdge(self):
        """
            Description in the declaration
        """
        self.graph_1.addEdge(0, 00)
        self.graph_1.addEdge(1, 11)
        self.graph_1.addEdge(1, 12)
        self.graph_1.addEdge(6, 60)
        self.assertNotEqual(self.graph_1.graph[0], 0)
        self.assertEqual(self.graph_1.graph[0], [00])
        self.assertEqual(self.graph_1.graph[1], [11, 12])
        self.assertEqual(self.graph_1.graph[6], [60])



if __name__ == '__main__':
    unittest.main()
