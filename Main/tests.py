from utility import *

#Node tests

test_node = Node(1) #Nodes must start from at least 1. An id of 0 = uninstantianted object of the node, 1 = object.
test_node_2 = Node(2)
test_node_3 = Node(3)

test_node.set_contents(1)
test_node_2.set_contents(2)
test_node_3.set_contents(2)

test_node.set_name("one")
test_node_2.set_name("two")
test_node_3.set_name("two")

print(f"{[test_node, test_node_2, test_node_3]}: [1, 2, 3]")
print(f"{test_node} {test_node_2} {test_node_3}: 1-one 2-two 3-two")

print(f"{test_node==test_node_2}: False")
print(f"{test_node==test_node_3}: False")
print(f"{test_node_2==test_node_3}: True")

#Link tests

test_link = Link(test_node, 1)
print(test_link)
test_link.set_end(test_node_2)
print(test_link)
test_link.set_nature("BEFORE")
print(test_link)

#we could also add a reciprocal link back, from 2 to 1.

test_link_2 = Link(test_node_2, 2)
test_link_2.set_end(test_node)
test_link_2.set_nature("AFTER")

print(test_link_2)

print(test_link==test_link_2)

#Making a third link

test_link_3 = Link(test_node, 3)
test_link_3.set_end(test_node_3)
test_link_3.set_nature("BEFORE")

print(test_link_3)
print(test_link==test_link_3)

#Testing trees

test_tree = Tree(test_node, test_node_2, test_link)

print(test_tree)
print(test_tree.get_nodes())
test_tree.add_link(test_link_3)
print(test_tree)
print(test_tree.get_nodes())
test_tree.add_link(test_link_2)
print(test_tree.get_nodes())
print(test_tree.get_links())
test_tree.remove_link(3)
print(test_tree.get_links())


#Testing different interactions

test_link_4 = Link(test_node_2, 4)
test_node_4 = Node(4)
test_node_4.set_contents(3)
test_node_4.set_name("three")
test_link_4.set_end(test_node_4)
test_link_4.set_nature("BEFORE")
print(test_link_4)

#adding the link but not node to the tree, to test if the tree adds it to its nodes

print(test_tree.get_nodes())
test_tree.add_link(test_link_4)
print(test_tree.get_nodes())