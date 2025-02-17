from text_parser import TextParser
from document import Document
from tree_utility import nouns_to_tree, parse_list, link_nodes, recurse_list, read_tree, build_spanning_tree, build_links


#Process of building the code is as follows:
#First, we get the context from the text file. The text parser class converts the raw text into its noun arrays.
#After this point, those arrays are turned into consequtive trees. 
#They are added to the document, and rearranged inside the document to form dictionaries to iterate through
#When all nodes are built and rearranged, their links are found.
#These links are then recursed through, in order to produce a depth map of each node via DFS. 
#This depth-indexed array of nodes is then read, and generates the nested array into a nested dict
#Finally, this is used to generate the spanning tree via only visting each node


#Creates the text parser. This handles the conversion from raw text into the list of single sentence trees.
parser = TextParser()

#List of text file names

#Graphviz for plotting
from graphviz import Digraph
dot = Digraph()




def load_text(filename):
    with open(f"{filename}.txt") as f:
        contents = f.read()
    return contents


def create_trees(contents):
    #Parser is given the text to read
    parser.set_text(contents)
    #Text is parsed, converting into a dict of paragraphs (\n\n) which contains the array of trees for each sentence.
    parser.process_text()   
    #Getting the paragraph dictionary back out from the parser
    para_dict = parser.get_para_dict()
    parser_text = para_dict[0]
    noun_sentences = []
    #Noun sentences is the reduced list of nouns from every sentence. These are iteratively added to an array.
    for sentence in parser_text:
        noun_sentences.append(parser.extract_nouns(sentence))
    #Nouns to tree takes the full list of individual nouns from each sentence, then constructs one tree per sentence, from the starting word to the end word, linked from one to the next.
    total_trees = nouns_to_tree(noun_sentences)
    return total_trees


def document_handling(total_trees):
    #Creates a document, then sets its current array of trees to the processed linked sentences from before.
    test_document = Document()
    #Moving the trees into the document object
    test_document.set_trees(total_trees)
    #Takes those trees, parses through them, and outputs a dictionary of node id to node contents.
    output, node_dict = test_document.trees_reordering()
    #Creating a dict aliasing the noun to its id for easy lookup later
    contents_to_id = {}
    #Linking nodes together to then recurse through
    build_links(contents_to_id, node_dict, output)
    #Creating variables for the sets of nouns outside to then pass into the function, updated as it iterates. 
    visited_ids = set()
    visited_contents = set()
    #Returns the first array (top level node) from the nested array+dict output
    total_node_tree = test_document.recurse_node(node_dict[1], visited_ids, visited_contents, 0)[0]
    #Creating a new set to check against all visited IDs
    visited_ids = set()
    #And the same for the contents
    visited_contents = set()
    #Converts the nested arrays into a nested dictionary
    output = read_tree(total_node_tree)
    #Converts this nested dictionary into a reduced graph format
    span_output, spanning_tree = build_spanning_tree(node_dict, output)
    return span_output, node_dict, spanning_tree
distinct_nodes = set()
viz_links = []

def span_to_viz(span_output, node_dict):
    #span_output = 
    #Gets the nodes at each level from the second item of the output of build_spanning_tree
    depth_nodes = span_output[1]
    #The array of all nodes is found from the third item
    total_contents = span_output[2]
    depth = 0
    output_string = ""
    children_in_total = []
    visited_nodes = []
    span_contents = []

    #For each depth of node
    for x in depth_nodes:
        #For each node at that level
        for y in x:
            #Add its contents to the spanning contents array
            span_contents.append(y.content)

    #For each depth of node again
    for x in depth_nodes:
        #The Output String is the visualization, and stores the current depth at each level at the start.
        output_string += f"{depth}: "
        depth += 1
        #Add an indentation relative to its current depth
        output_string += "\t"*int(int(depth/2)+1)
        #For each node at that depth
        for node in x:
            #Get the ID of the node for lookup from the object id
            node_id = node.id
            #Seeing if the node exists
            if node_id in node_dict:
                #Get the node object
                node_from_dict = node_dict[node_id]
                #Add its content to the list of total visited nodes
                visited_nodes.append(node_from_dict.content)
                #Get the children of the node     
                children = node_from_dict.get_children()
                #Get an array of the contents of each child
                children_in_total = [x.content for x in children if x and x.content in total_contents]
                join_string = ", "
                #If the node is an element of the total tree, and if it exists
                current_children = [x for x in children_in_total if x in children_in_total and x in span_contents]
                #Adding to the array for vizualization later
                if node_from_dict.content.lower() not in distinct_nodes:
                    for child in current_children:
                        viz_links.append((node_from_dict.content.lower(), child.lower()))
                #Joining the array to the output string
                output_string += f"{node.content}->{join_string.join(current_children)}\n"+'\t'*depth
                #Adding the lowercase version to the set of all nodes aliased via content
                distinct_nodes.add(node_from_dict.content.lower())
        output_string += "\n"
    return distinct_nodes, viz_links


def combine_trees(tree_array):
    distinct_nouns = set()
    intersections = []
    total_contents = {}
    total_nodes = {}
    for tree in tree_array:
        nodes = tree.get_nodes()
        node_contents = {x[1].content.lower():x[0] for x in nodes.items()}
        item_set = set([x[1].content.lower() for x in nodes.items()])
        intersection = distinct_nouns.intersection(item_set)
        total_contents = total_contents | node_contents
        total_nodes = total_nodes | nodes

        # print(node_contents.items())
        distinct_nouns = distinct_nouns.union(set([x[0] for x in node_contents.items() if x not in intersection]))
        # print(distinct_nouns)
        if not intersection:
            if distinct_nouns:
                distinct_nouns = distinct_nodes.union(item_set)
            else:
                distinct_nouns = item_set
        else:
            intersections.append(intersection)
        # else:
        # node_contents = [x[x.keys()[0]].content for x in nodes.items()]
       # print(noun_additions)
            
    #print(intersections)
            
    
    #print(total_nodes)
    #print(intersections)

def run(filenames):

    selected_nodes = ["toddy", "remedy", "coronavirus", "uk", "brit", "virus", "beat", "flu", "glass", "whisky", "honey"]

    total_trees = []

    for file in filenames:
        total_trees = create_trees(load_text(file))
        # total_trees[0].union(total_trees[1])
        span_output, node_dict, spanning_tree = document_handling(total_trees)
        distinct_nodes, viz_links = span_to_viz(span_output, node_dict)
        total_trees.append(spanning_tree)
        for node in distinct_nodes:
            #if node in selected_nodes:
            dot.node(node, node)
        for edge in viz_links:
            #if edge[0] in selected_nodes or edge[1] in selected_nodes:
            dot.edge(edge[0],edge[1])
        dot.render(f'selections/physics', format='png', cleanup=True)  # Saves as 'tree.png'
##Main Loop

    combine_trees(total_trees)

filenames = ["business_standard", "usa_today", "reed_reuters", "daily_post", "aljazeera", "reed_base_text", "reed_daily_post", "reed_daily_record", "reed_mh", "reed_mirror", "reed_nwpioneer", "reed_ny_post", "reed_personal", "reed_sky", "reed_sun", "reed_vice"]
run(filenames)

