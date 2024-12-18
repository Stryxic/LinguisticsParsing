from utility import *
from word_tagging import *

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

test_tree = Tree(test_node, test_node_2, test_link, 1)

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
print(test_tree.get_links())
links = test_tree.get_links()
for link in links:
    print(link)

paragraph_1 = '''Bali is predominantly a Hindu country. Bali is known for its elaborate, traditional dancing. 
The dancing is inspired by its Hindi beliefs. 
Most of the dancing portrays tales of good versus evil. 
To watch the dancing is a breathtaking experience. 
Lombok has some impressive points of interest - the majestic Gunung Rinjani is an active volcano. 
It is the second highest peak in Indonesia. 
Art is a Balinese passion. 
Batik paintings and carved statues make popular souvenirs. 
Artists can be seen whittling and painting on the streets, particularly in Ubud. 
It is easy to appreciate each island as an attractive tourist destination. 
Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year. 
Snorkelling and diving around the nearby Gili Islands is magnificent. 
Marine fish, starfish, turtles and coral reef are present in abundance. 
Bali and Lombok are part of the Indonesian archipelago. 
Bali has some spectacular temples. 
The most significant is the Mother Temple, Besakih. 
The inhabitants of Lombok are mostly Muslim with a Hindu minority. 
Lombok remains the most understated of the two islands. 
Lombok has several temples worthy of a visit, though they are less prolific. 
Bali and Lombok are neighbouring islands.'''

converter = Converter(paragraph_1)

converter.tag()
nouns = converter.get_nouns()

#The starting noun is likely the head noun. From noun to noun, each is created as a node (or reused) and linked to the prior.

print(nouns)

#Testing sentence splitting
converter.tag_sentences()
#Testing converting sentences to nouns, then building nodes
sentences = converter.get_sentence_nouns()
tree_id = 0
trees = []
for sentence in sentences:
    #Convert the sentence into singular nodes, each noun = one node.
    nodes = converter.build_nodes(sentence)
    print(nodes)
    print(sentence)
    #Constructs an array of links from the nodes
    links = converter.build_links(nodes)
    print(links)
    #Testing to check each link has each word on either end
    for link in links:
        if link:
            print(link.get_terminals())

    #Adding fuctionality to construct trees from these links + nodes
    if nodes:
        first_node = nodes[0]
        second_node = nodes[1]
        link = links[0]
        # print(f"{first_node} | {second_node} | {link}")
        tree_id += 1
        tree = Tree(first_node, second_node, link, tree_id)
        remaining_nodes = nodes[2:]
        remaining_links = links[1:]
        if remaining_nodes:
            for node in remaining_nodes:
                tree.add_node(node)
        if remaining_links:
            for link in remaining_links:
                tree.add_link(link)
        # print(tree)
        trees.append(tree)

    


    
for tree in trees:
    print(tree.traverse_tree())