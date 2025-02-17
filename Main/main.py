from text_parser import TextParser
from document import Document
from tree_utility import nouns_to_tree, parse_list, link_nodes, recurse_list, read_tree, build_spanning_tree, build_links
from graphviz import Digraph

def parse_document(files, output_name, distinct_nodes, viz_links):

    #Creates the text parser. This handles the conversion from raw text into the list of single sentence trees.
    parser = TextParser()

    #List of text file names
    #files = ["business_standard", "usa_today", "reed_reuters", "daily_post", "aljazeera", "reed_base_text", "reed_daily_post", "reed_daily_record", "reed_mh", "reed_mirror", "reed_nwpioneer", "reed_ny_post", "reed_personal", "reed_sky", "reed_sun", "reed_vice"]
    #files = ["trump-davos-1", "trump-davos-2", "trump-davos-5", "trump-davos-6", "trump-davos-9", "trump-davos-10", "trump-davos-11", "trump-davos-12", "trump-davos-13", "trump-davos-14", "trump-davos-15", "trump-davos-16", "trump-davos-17", "trump-davos-18", "trump-davos-19", "trump-davos-20", "trump-davos-21", "trump-davos-22", "trump-davos-25"]

    #Graphviz for plotting

    # dot = Digraph()

    # distinct_nodes = set()
    # viz_links = []
    def process_file(contents):
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
        #print(output)
        #Converts this nested dictionary into a reduced graph format
        span_output = build_spanning_tree(node_dict, output)[0]
        #Gets the nodes at each level from the second item of the output of build_spanning_tree
        depth_nodes = span_output[1]
        #The array of all nodes is found from the third item
        #print(span_output)
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
        


    ##Main Loop


    for file in files:
        with open(f"articles/{file}.txt", encoding="utf-8") as f:
            contents = f.read()
        try:
            process_file(contents)
        except IndexError:
            print("Error")

    # return(distinct_nodes, viz_links)


        
        
    # for node in distinct_nodes:
    #     # if node in selected_nodes:
    #     dot.node(node, node)
    # for edge in viz_links:
    #     # if edge[0] in selected_nodes or edge[1] in selected_nodes:
    #     dot.edge(edge[0],edge[1])
    # dot.render(f'selections/{output_name}', format='png', cleanup=True)  # Saves as 'tree.png'


# files = ["trump-davos-1", "trump-davos-2", "trump-davos-5", "trump-davos-6", "trump-davos-9", "trump-davos-10", "trump-davos-11", "trump-davos-12", "trump-davos-13", "trump-davos-14", "trump-davos-15", "trump-davos-16", "trump-davos-17", "trump-davos-18", "trump-davos-19", "trump-davos-20", "trump-davos-21", "trump-davos-22", "trump-davos-25"]
# files = ["british-officials-do-not-rule-1","british-officials-do-not-rule-2","british-officials-do-not-rule-3","british-officials-do-not-rule-4","british-officials-do-not-rule-5","british-officials-do-not-rule-6","british-officials-do-not-rule-7","british-officials-do-not-rule-8","british-officials-do-not-rule-9","british-officials-do-not-rule-10","british-officials-do-not-rule-11"]

# parse_document(files, "bbc")