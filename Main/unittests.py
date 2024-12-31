import unittest
from node import Node
from link import Link
from linknature import LinkNature
from tree import Tree

class TestCases(unittest.TestCase):

    def setUp(self):
        #Creating Nodes
        self.node_1 = Node(1, "Root")
        self.node_2 = Node(2, "Child1")
        self.node_3 = Node(3, "Child2")
        self.node_4 = Node(4, "Child3")
        #Creating Links
        self.link_1 = Link(self.node_1, "link1", LinkNature.CHILD, self.node_2)
        self.link_2 = Link(self.node_1, "link2", LinkNature.CHILD, self.node_3)
        self.link_3 = Link(self.node_2, "link3", LinkNature.CHILD, self.node_4)
        #Adding links
        self.node_1.add_link(self.link_1)
        self.node_1.add_link(self.link_2)
        self.node_2.add_link(self.link_3)
        #Creating tree
        self.tree = Tree(self.node_1, self.node_2, self.link_1, "tree1")
        self.tree.add_node(self.node_3)
        self.tree.add_node(self.node_4)
        self.tree.add_link(self.link_2)
        self.tree.add_link(self.link_3)

    def test_node_creation(self):
        self.assertEqual(self.node_1.id, 1)
        self.assertEqual(self.node_1.name, "Root")
        self.assertEqual(self.node_1.content, None)


    def test_link_creation(self):
        self.assertEqual(self.link_1.id, "link1")
        self.assertEqual(self.link_1.nature, LinkNature.CHILD)
        self.assertEqual(self.link_1.start, self.node_1)
        self.assertEqual(self.link_1.end, self.node_2)

    def test_tree_nodes(self):
        nodes = self.tree.get_nodes()
        self.assertEqual(len(nodes), 4)
        self.assertIn(self.node_1.id, nodes)
        self.assertIn(self.node_2.id, nodes)
        self.assertIn(self.node_3.id, nodes)
        self.assertIn(self.node_4.id, nodes)

    def test_dfs_traversal(self):
        result = self.tree.traverse_tree(tranversal_type="dfs")
        #DFS -> Links are 1->2, 2->3, 2->4. As such, DFS results in IDs 1,2,4,3
        self.assertEqual(len(result),4)
        self.assertEqual(result[0], self.node_1)
        self.assertEqual(result[1], self.node_2)
        self.assertEqual(result[2], self.node_4)
        self.assertEqual(result[3], self.node_3)

    def test_bfs_traversal(self):
        result = self.tree.traverse_tree(tranversal_type="bfs")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], self.node_1)
        self.assertEqual(result[1], self.node_2)
        self.assertEqual(result[2], self.node_3)
        self.assertEqual(result[3], self.node_4)

    def test_add_node(self):
        new_node = Node(5, "NewChild")
        self.tree.add_node(new_node)
        nodes = self.tree.get_nodes()
        self.assertEqual(len(nodes), 5)
        self.assertIn(new_node, nodes.values())

    def test_remove_node(self):
        self.tree.remove_node(4)
        nodes = self.tree.get_nodes()
        self.assertEqual(len(nodes), 3)
        self.assertNotIn(self.node_4, nodes.values())

    def test_add_link(self):
        new_node = Node(5, "NewChild")
        new_link = Link(self.node_3, "link4", LinkNature.CHILD, new_node)
        self.tree.add_node(new_node)
        self.tree.add_link(new_link)
        links = self.tree.get_links()
        self.assertEqual(len(links), 4)
        self.assertIn(new_link, links)

    def test_remove_link(self):
        self.tree.remove_link("link3")
        links = self.tree.get_links()
        self.assertEqual(len(links), 2)
        self.assertNotIn(self.link_3, links)

    
    

        



if __name__ == "__main__":
    unittest.main(verbosity=2)

