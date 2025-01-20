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
        print("Reduced sentence:")
        print(reduced)
        #Calls tree convert to turn the nouns into a list of linked nodes
        reduced_tree = tree_convert.convert_sentence(reduced)
        #print(reduced_tree)
        #print("-------")
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

def recurse_list(tree, visited_nodes, depth, prior_depth, node_positions):
    if len(node_positions) < depth+1:
        node_positions.append([])   
    prior_depth = depth
    depth += 1
    first_id = next(iter(tree.keys()))
    if first_id == 1:
        items = len(tree.keys())
        total_nodes = []
        for i in range(1, items+1):
            next_node = recurse_list(tree[i],visited_nodes,depth, prior_depth, node_positions)
            if next_node:
                node_positions[depth-1].append(next_node)
                total_nodes.append(next_node)
    else:
        return tree
        
def link_nodes(node_1, node_2, id):
    new_link = Link(node_1, id, LinkNature.CHILD)
    new_link.set_end(node_2)
    return new_link

def read_tree(node_tree):
    if type(node_tree) == type(list()):
        output = {}
        link_count = 1
        for x in node_tree:
            output[link_count] = read_tree(x)
            link_count += 1
        return output
    else:
        output = {}
        for x in node_tree:
            output[x] = node_tree[x]
        return output

def build_links(contents_to_id, node_dict, output):
    prior_node = None
    new_link = None
    link_count = 1
    for node in node_dict:
        #print(node_dict[node].content)
        contents_to_id[node_dict[node].content] = node
    #print(contents_to_id)
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
    

def build_spanning_tree(node_dict, output):
    # print(node_dict)
    visited_nodes = set()
    added_links = []
    added_nodes = []
    node_positions = []
    recurse_list(output, visited_nodes, 0, 0, node_positions)
    prior_node = None
    expected_nodes = set()
    root_nodes = []
    links = []
    total_nodes = []
    parent_nodes = {}



    link_id = 1
    for level in range(0, len(node_positions)-1):
        nodes = node_positions[level]
        node_objs = []
        for node in nodes:
            node_id = list(node.keys())[0]
            node_contents = node[node_id]
            if node_id in node_dict:
                node_object = node_dict[node_id]
                node_objs.append(node_object)
                total_nodes.append(node_object)
            else:
                node_dict[node_id] = Node(node_id, "Noun", node_contents)
                if node_contents in parent_nodes:
                    link = link_nodes(parent_nodes[node_contents], node_dict[node_id], link_id)
                    node_dict[node_id].add_link(link)
                total_nodes.append(node_dict[node_id])

            if node_contents in expected_nodes:
                link = None
                if node_contents in parent_nodes:
                    if node_id in node_dict:
                        link = link_nodes(parent_nodes[node_contents], node_dict[node_id], link_id)
                        from_node_link = link_nodes(node_dict[node_id], parent_nodes[node_contents], link_id+1)
                        links.append(link)
                        link_id += 2
                prior_node = node
            else:
                root_nodes.append(node)
                prior_node = node

        node_children = {x.contents:x.get_children() for x in node_objs}

        for node in node_objs:
            for child in node.get_children():
                if child:
                    parent_nodes[child.contents] = node

        children_contents = {}
        for child in node_children:
            related_nodes = node_children[child]
            children_contents[child] = [x.contents for x in related_nodes if x]
        if children_contents:
            total_vals = []
            items = []
            child_content = [children_contents[x] for x in children_contents.keys()]
            for x in child_content:
                total_vals += x
            for x in total_vals:
                expected_nodes.add(x)


    # print(total_nodes)
    # print(links)
    print(len(total_nodes))
    if len(total_nodes)>2:
        spanning_tree = Tree(total_nodes[0], total_nodes[1], links[0], 1)

        for node in total_nodes[2:]:
            spanning_tree.add_node(node)

        for link in links[1:]:
            spanning_tree.add_link(link)

        output = spanning_tree.tree_to_string()
        return output