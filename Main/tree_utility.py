#Wrapper class to hold various functions related to tree interactions.
from link import Link
from textToTree import TreeConverter
from linknature import LinkNature
from node import Node
from tree import Tree

def nouns_to_tree(noun_sentences):
    #Takes in the array of all nouns, separated by sentence
    reduced_sentences = []
    #invokes TreeConverter to handle nouns into nodes/links/trees
    tree_convert = TreeConverter()
    # print(noun_sentences)
    for sentence in noun_sentences:
        #Converts the Tagged Nouns into just their contents. The second part (Type of noun) is currently discarded. This is then added as a reduced sentence
        reduced_sentences.append([x[0] for x in sentence])
    total_trees = []
    #Each sentence is converted into a tree
    for reduced in reduced_sentences:
        if len(reduced) < 2:
            continue
        #Calls tree convert to turn the nouns into a list of linked nodes
        reduced_tree = tree_convert.convert_sentence(reduced)
        if reduced_tree:
            nodes = reduced_tree.traverse_tree(tranversal_type="dfs")[0]

            total_trees.append(reduced_tree)
    return total_trees

def parse_list(list, depth):
    if type(list) == type({}):
        for key in list:
            print(">"*depth + f"|{depth}|{key} - {list[key]}")
    else:
        depth += 1
        for item in list: 
            parse_list(item, depth)


#Recursive function to convert the nested dictionary into an array of nodes, with their depths
def recurse_list(tree, visited_nodes, depth, prior_depth, node_positions):
    #If the length of the list is at depth, create a new element
    if len(node_positions) < depth+1:
        node_positions.append([])   
    #Update prior depth
    prior_depth = depth
    #Increment depth here rather than through function call so as to keep the prior depth beforehand
    depth += 1
    #Each dict has to have at least 1 node
    first_id = next(iter(tree.keys()))
    #print(first_id)
    #Each dict starts at 1, and increments from there.
    if first_id == 1:
        #Checks the length of the array, for later iteration
        items = len(tree.keys())
        #Store an array of all the nodes visited
        total_nodes = []
        #Going through each depth in turn
        for i in range(1, items+1):
            if type(tree[i]) != str: 
                #Calling the next depth of tree, to find the next child node
                next_node = recurse_list(tree[i],visited_nodes,depth, prior_depth, node_positions)
                if next_node:
                    #If there is another node, append it as a sequential node of the prior depth item
                    node_positions[depth-1].append(next_node)
                    total_nodes.append(next_node)
            else:
                return tree
    else:
        return tree

#Quick function to create a link between nodes    
def link_nodes(node_1, node_2, id):
    new_link = Link(node_1, id, LinkNature.CHILD)
    new_link.set_end(node_2)
    return new_link


#Recursive function to parse through the nested array and return a dictionary.

def read_tree(node_tree):
    #First, check if its an array of items, or a dictionary
    if type(node_tree) == type(list()):
        #If it is an array, create a dictionary to hold the output, and recurse each element
        output = {}
        #Counting the number of links. Starting at 1 because this relates to Link IDs, which always start at 1 not 0.
        link_count = 1
        #Iterate through the items
        for x in node_tree:
            #Current item is recursed
            output[link_count] = read_tree(x)
            link_count += 1
        #Once all items are complete, return that nested dictionary
        return output
    else:
        #If it is a dictionary
        output = {}
        for x in node_tree:
            output[x] = node_tree[x]
        return output


#Iterates through each node in the node dict, then creates a link between each pair.
def build_links(contents_to_id, node_dict, output):
    prior_node = None
    new_link = None
    link_count = 1
    for node in node_dict:
        contents_to_id[node_dict[node].content] = node
    for key in output:
        current_node = node_dict[contents_to_id[key]]
        if prior_node:
            new_link.set_end(current_node)
            new_link = Link(current_node, link_count, LinkNature.CHILD)
            current_node.add_link(new_link)
            link_count += 1
            prior_node = current_node
        else:
            new_link = Link(current_node, link_count, LinkNature.CHILD)
            current_node.add_link(new_link)
            link_count += 1
            prior_node = current_node   
    

#Takes the node dictionary, and the recursive dictionary of its links, and generates a tree
def build_spanning_tree(node_dict, output):
    #Creating the empty set of visited nodes
    visited_nodes = set()
    node_positions = []
    #Creates a nested array of nodes to their children nodes
    recurse_list(output, visited_nodes, 0, 0, node_positions)
    prior_node = None
    #Checking what nodes might be encountered by keeping track of each node's children
    expected_nodes = set()
    #Root nodes holds the disparate strings of nodes, if they are not all connected
    root_nodes = []
    #Total array of all links
    links = []
    #Total array of all nodes
    total_nodes = []
    #A dict of nodes parent to child content
    parent_nodes = {}



    link_id = 1
    #Iterating through each depth in the list
    for level in range(0, len(node_positions)-1):
        #Get all nodes at that current level
        nodes = node_positions[level]
        #Array to hold the objects after lookup
        node_objs = []
        #Iterate through all the nodes
        for node in nodes:
            #Get the node ID from its dict key
            node_id = list(node.keys())[0]
            #Get its contents
            node_contents = node[node_id]
            #If it hasn't already been added,
            if node_id in node_dict:
                #Get that node object from the dictionary
                node_object = node_dict[node_id]
                #Add it to the current node objects array
                node_objs.append(node_object)
                #And also the total nodes object array
                total_nodes.append(node_object)
            #If it's a new ID
            else:
                #Create a new node for it
                node_dict[node_id] = Node(node_id, "Noun", node_contents)
                #If its contents are in the parent nodes, I.E. this word is followed by a prior word
                if node_contents in parent_nodes:
                    #Add a link between that node and its parent node
                    link = link_nodes(parent_nodes[node_contents], node_dict[node_id], link_id)
                    #Add that link to the node in the dictionary
                    node_dict[node_id].add_link(link)
                #Add the node to the array
                total_nodes.append(node_dict[node_id])

            #If its contents are expected, I.E. it was previously a child of another node
            if node_contents in expected_nodes:
                #Initialise an empty link
                link = None
                #If the node has a parent (as it should if it is expected)
                if node_contents in parent_nodes:
                    #If that node already exists, find it and link to it
                    if node_id in node_dict:
                        link = link_nodes(parent_nodes[node_contents], node_dict[node_id], link_id)
                        links.append(link)
                        link_id += 1
            #otherwise it is a new root node
            else:
                root_nodes.append(node)

        #Make a dict of all the children of each noun to its content
        node_children = {x.contents:x.get_children() for x in node_objs}

        #For each node,
        for node in node_objs:
            #For each child,
            for child in node.get_children():
                #If child is not none
                if child:
                    #it is now a parent node of the child's contents
                    parent_nodes[child.contents] = node

        #Declaring a dict for the array of the children nodes
        children_contents = {}
        for child in node_children:
            #Getting the nodes connected to the current child
            related_nodes = node_children[child]
            #Getting a list of contents for each child
            children_contents[child] = [x.contents for x in related_nodes if x]
        #If there are any children with contents
        if children_contents:
            total_vals = []
            items = []
            #Convert the dict into a linear array of strings
            child_content = [children_contents[x] for x in children_contents.keys()]
            #Add each string to the total words
            for x in child_content:
                total_vals += x
            #Add the child to the expected nodes
            for x in total_vals:
                expected_nodes.add(x)

    #If the resulting tree has more than 2 nodes
    if len(total_nodes)>2:
        #Create a tree from the list
        spanning_tree = Tree(total_nodes[0], total_nodes[1], links[0], 1)

        #Add all nodes remaining
        for node in total_nodes[2:]:
            spanning_tree.add_node(node)

        #Add all links remaining
        for link in links[1:]:
            spanning_tree.add_link(link)

        #Convert the tree into an array, output
        output = spanning_tree.get_recursed_tree()
        if output:
            return output, spanning_tree
    else:
        return "", ""