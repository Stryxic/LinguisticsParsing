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

paragraph_1 = '''Bali is predominantly a Hindu country. 
Bali is known for its elaborate, traditional dancing. 
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

paragraph_2 = '''
Bali and Lombok are neighbouring islands; 
both are part of the Indonesian archipelago. 
It is easy to appreciate each island as an attractive tourist destination – majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year. 
Snorkelling and diving around the nearby Gili Islands is magnificent, with marine fish, starfish, turtles and coral reef present in abundance. 
Whereas Bali is predominantly a Hindu country, the inhabitants of Lombok are mostly Muslim with a Hindu minority. 
Bali is known for its elaborate, traditional dancing which is inspired by its Hindi beliefs. 
Most of the dancing portrays tales of good versus evil; to watch it is a breathtaking experience. 
Art is another Balinese passion – batik paintings and carved statues make popular souvenirs. 
Artists can be seen whittling and painting on the streets, particularly in Ubud. 
The island is home to some spectacular temples, the most significant being the Mother Temple, Besakih. Lombok, too, has some impressive points of interest – the majestic Gunung Rinjani is an active volcano and the second highest peak in Indonesia. 
Like Bali, Lombok has several temples worthy of a visit, though they are less prolific. 
Lombok remains the most understated of the two islands.
'''

paragraph_3 = '''
Martin Luther King Jr led many demonstrations against racism. 
He delivered his message in a non-violent manner. 
Some members of his movement later engaged in less peaceful protests. 
Luther King was detained several times. The longest jail sentence he received was four months. 
Martin Luther King’s famous 1963 speech, “I Have a Dream”, inspired many African-Americans to envisage a better future. 
Luther King was an American citizen. 
Nelson Mandela is a native South African. 
Their dreams were the same. 
Their battles were tumultuous. 
Nelson Mandela was arrested in 1962 for treason. 
He was incarcerated for twenty-seven years. 
Nelson Mandela and Martin Luther King Jr both fought for racial equality. 
The intolerance of white people towards black co-inhabitants was the catalyst for years of activism. 
In 1994, Nelson Mandela became the first black president of South Africa. 
He was the first president elected by the people. 
Mandela and Luther King have been awarded the Nobel Peace Prize for their dedication to improving civil rights for black people. 
During Nelson Mandela’s best known speech in 1994, he recited “Our Deepest Fear”, an inspirational poem by Marianne Williamson. 
Mandela initially avoided violence but ended up resorting to it following the massacre of unarmed black Africans by the government. 
Martin Luther King Jr was assassinated in 1968.'''

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
    if len(nodes)>1:
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

    


tree_node_id = 1
tree_nodes = []
for tree in trees:
    tree_node = Node(tree_node_id)
    tree_node_id+=1
    tree_node.set_contents(tree)
    tree_node.set_name("Tree")
    tree_nodes.append(tree_node)
    print(tree.traverse_tree())

for tree in tree_nodes:
    print(tree)
    tree_obj = tree.get_contents()
    print(tree_obj.traverse_tree())
    tree_links = tree_obj.get_links()
    for link in tree_links:
        print(link)
        print(f"\t{link.get_terminals()}")

#Now we know the trees work as expected. Each tree contains a list of nodes, and links. It traverses the tree, showing all continuous links. Then each link is created in successeion.

#Next step: Make a links from all these nodes, similar to before. Note to self: Might be good to move this [general node->link generation] into utility.
print("---------")
tree_links = converter.build_links(tree_nodes)

tree_id = 98
paragraph_tree = Tree(tree_nodes[0], tree_nodes[1], tree_links[0], tree_id)

for node in tree_nodes[2:]:
    paragraph_tree.add_node(node)

for link in tree_links[1:]:
    paragraph_tree.add_link(link)

#Here we have the resulting total paragraph tree. Now to test iteration through nodes.

print("List of all the nodes + Links in each tree:")
print(paragraph_tree)

print("Traversing the total paragraph tree.")
print(paragraph_tree.traverse_tree())


#Now that the tree is created, we parse it.

parser = TreeParser(paragraph_tree)
parser.parse_tree()
#Get all the nouns from the tree
nouns = parser.get_nouns()
print(nouns)
print("-----------")
#Print their counts
count = parser.get_counts()
print(count)

print("----------------------")
parser.find_ratios()
ratios = parser.get_ratios()
print(ratios)

print("--------------------")

#Testing the Document class

document = Document(paragraph_1)
document.find_sentences()
document.set_ratios(ratios)
#Testing the average of the count
document.find_avg()

#Iterating through sentences, comparing their outputs when related via the earlier statistics. This dictionary forms the seed for the initial tree of the document.
document.process_text()

#Once we have the definitions, we construct a tree. Starting from the occurance of nouns in order from the start of the text using read words, we 
#build up a tree and either add a node, add a link, or add a link and a node. Or none of the above.

document.build_root()

