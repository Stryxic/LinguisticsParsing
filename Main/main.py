from text_parser import TextParser
from document import Document
from link import Link
from linknature import LinkNature
from node import Node
from tree import Tree
from tree_utility import nouns_to_tree, parse_list, link_nodes, recurse_list, read_tree, build_spanning_tree, build_links


parser = TextParser()
#Uses a '. ' as the split at the moment, should be converted
#Loading in a test file
file = "reed_sky"


with open(f"{file}.txt") as f:
    contents = f.read()



# contents = text
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
#Creates a document, then sets its current array of trees to the processed linked sentences from before.
test_document = Document()
test_document.set_trees(total_trees)
#Takes those trees, parses through them, and outputs a dictionary of node id to node contents.
output, node_dict = test_document.trees_reordering()
contents_to_id = {}
build_links(contents_to_id, node_dict, output)
visited_ids = set()
visited_contents = set()
total_node_tree = test_document.recurse_node(node_dict[1], visited_ids, visited_contents, 0)[0]
visited_ids = set()
visited_contents = set()
output = read_tree(total_node_tree)

span_output = build_spanning_tree(node_dict, output)
print(span_output)
span_links = span_output[0]
depth_nodes = span_output[1]
total_contents = span_output[2]
depth = 0
output_string = ""
expected_children = None
children_in_total = []
viz_dict = {}
prior_node = None
visited_nodes = []
span_contents = []
distinct_nodes = set()
viz_links = []

for x in depth_nodes:
    for y in x:
        span_contents.append(y.content)

# print(span_contents)
for x in depth_nodes:
    # print(depth)
    output_string += f"{depth}: "
    depth += 1
    output_string += "\t"*int(int(depth/2)+1)
    for node in x:
        node_id = node.id
        if node_id in node_dict:
            node_from_dict = node_dict[node_id]
            visited_nodes.append(node_from_dict.content)     
            # allowed_children[node_from_dict.content] = [""]
            children = node_from_dict.get_children()
            children_in_total = [x.content for x in children if x and x.content in total_contents]
            # if expected_children and node_from_dict.content in expected_children:
            #     if prior_node.content in allowed_children:
            #         allowed_children[prior_node.content].append(node_from_dict.content)
            #     else:
            #         allowed_children[prior_node.content] = [node_from_dict.content]

            # if expected_children:
            #     if children_in_total:
            #         expected_children += children_in_total
            # else:
            #     expected_children = children_in_total
            join_string = ", "
            current_children = [x for x in children_in_total if x in children_in_total and x in span_contents]
            if node_from_dict.content.lower() not in distinct_nodes:
                for child in current_children:
                    viz_links.append((node_from_dict.content.lower(), child.lower()))
            output_string += f"{node.content}->{join_string.join(current_children)}\n"+'\t'*depth
            distinct_nodes.add(node_from_dict.content.lower())
        prior_node = node_from_dict
    output_string += "\n"


print(output_string)
print(distinct_nodes)
print(viz_links)
# print(allowed_children)
# depth = 0
# print("####################")
# for x in depth_nodes:
#     print(depth)
#     depth += 1 
#     for node in x:
#         print("\t"*depth + node_from_dict.content + "\t")
#         node_id = node.id
#         if node_id in node_dict:
#             node_from_dict = node_dict[node_id]
#             print("\t"*depth + str(allowed_children[node_from_dict.content]))
    


#Graphviz component
from graphviz import Digraph
# Create a directed graph
dot = Digraph()

# Add nodes
# dot.node('A', 'Root')
# dot.node('B', 'Child 1')
# dot.node('C', 'Child 2')
# dot.node('D', 'Child 1.1')
# dot.node('E', 'Child 1.2')
# dot.node('F', 'Child 1.2')

for node in distinct_nodes:
    dot.node(node, node)
for edge in viz_links:
    dot.edge(edge[0],edge[1])


# Add edges (links between nodes)
# dot.edge('A', 'B')
# dot.edge('A', 'C')
# dot.edge('B', 'D')
# dot.edge('B', 'E')

# Render the graph (visualize it)
dot.render(f'{file}', format='png', cleanup=True)  # Saves as 'tree.png'
