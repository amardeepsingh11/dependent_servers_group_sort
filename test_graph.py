"""
    The module is for sorting the servers information contained in a CSV Amardeep
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

        self.graph_1_1 = Graph(1)
        self.graph_2_1 = Graph(2)
        self.graph_3_1 = Graph(3)
        self.graph_4_1 = Graph(4)
        self.graph_4_2 = Graph(4)
        self.graph_6_1 = Graph(6)
        self.graph_6_2 = Graph(6)

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

    def test_topologicalSort(self):
        """
            Description in the declaration
        """
        # test for 1 node
        self.graph_1_1.addEdge(0, 0)
        self.assertEqual(self.graph_1_1.topologicalSort(), [0])

        # test for 2 node 1 -> 0
        self.graph_2_1.addEdge(1, 0)
        self.assertEqual(self.graph_2_1.topologicalSort(), [1, 0])
        self.assertNotEqual(self.graph_2_1.topologicalSort(), [0, 1])
        self.assertNotEqual(self.graph_2_1.topologicalSort(), [0])
        self.assertNotEqual(self.graph_2_1.topologicalSort(), [1])

        # test for 3 nodes 2 -> 1 -> 0
        self.graph_3_1.addEdge(2, 1)
        self.graph_3_1.addEdge(1, 0)
        self.assertEqual(self.graph_3_1.topologicalSort(), [2, 1, 0])
        self.assertNotEqual(self.graph_3_1.topologicalSort(), [1, 2, 0])
        self.assertNotEqual(self.graph_3_1.topologicalSort(), [0, 1, 2])

        # test for 4 nodes 3 -> 2 -> 1 -> 0
        self.graph_4_1.addEdge(3, 2)
        self.graph_4_1.addEdge(2, 1)
        self.graph_4_1.addEdge(1, 0)
        self.assertEqual(self.graph_4_1.topologicalSort(), [3, 2, 1, 0])
        self.assertNotEqual(self.graph_4_1.topologicalSort(), [0, 1, 2, 3])

        # test for 4 nodes 3 -> 2 -> 1 -> 0 or 3 -> 1 -> 2 -> 0
        self.graph_4_2.addEdge(3, 2)
        self.graph_4_2.addEdge(2, 0)
        self.graph_4_2.addEdge(3, 1)
        self.graph_4_2.addEdge(1, 0)
        self.assertIn(self.graph_4_2.topologicalSort(), [[3, 2, 1, 0], [3, 1, 2, 0]] )
        self.assertNotEqual(self.graph_4_2.topologicalSort(), [0, 1, 2, 3])

        # test for 6 nodes 5 -> 4 -> 3 -> 2 -> 1 -> 0
        self.graph_6_1.addEdge(5, 4)
        self.graph_6_1.addEdge(4, 3)
        self.graph_6_1.addEdge(3, 2)
        self.graph_6_1.addEdge(2, 1)
        self.graph_6_1.addEdge(1, 0)
        self.assertEqual(self.graph_6_1.topologicalSort(), [5, 4, 3, 2, 1, 0])
        self.assertNotEqual(self.graph_4_2.topologicalSort(), [0, 1, 2, 3, 4, 5])

         # test for 6 nodes 5 -> 4 -> 3 -> 2 -> 1 -> 0
        self.graph_6_2.addEdge(5, 4)
        self.graph_6_2.addEdge(5, 3)
        self.graph_6_2.addEdge(4, 2)
        self.graph_6_2.addEdge(3, 1)
        self.graph_6_2.addEdge(2, 0)
        self.graph_6_2.addEdge(1, 0)
        self.assertIn(self.graph_6_2.topologicalSort(), [[5, 3, 4, 2, 1, 0], [5, 4, 3, 2, 1, 0], [5, 3, 4, 1, 2, 0], [5, 4, 3, 1, 2, 0], [5, 4, 3, 2, 1, 0], [5, 3, 4, 2, 1, 0], [5, 4, 3, 1, 2, 0], [5, 3, 4, 1, 2, 0]] )



if __name__ == '__main__':
    unittest.main()
