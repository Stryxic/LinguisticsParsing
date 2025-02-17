#This is the overall wrapper which is called when the interface is loaded. It represents a single overaching object and can perform operations
#on all the contained loaded or parsed documents.
#
#It is intented to keep track of which documents are where, to help print them, operate on them, combine them, and pass them to the interface
from text_parser import TextParser
from tree_utility import nouns_to_tree, parse_list, link_nodes, recurse_list, read_tree, build_spanning_tree, build_links
from document import Document
from utility import extract_nouns, generateGraphViz


class Linguistic_Engine():

    def __init__(self):
        self.empty = True
        self.documents = {}
        self.total_links = set()
        self.total_nodes = set()

    def add_document(self, document):
        self.documents[document.id] = document

    def graph_engine(self):
        generateGraphViz(self.total_nodes, self.total_links, "engine")

    def parse_content(self, parser, content):
        parser.set_text(content)
        parser.process_text()   
        para_dict = parser.get_para_dict()
        parser_text = para_dict[0]
        noun_sentences = []
        for sentence in parser_text:
            noun_sentences.append(parser.extract_nouns(sentence)) 
        return noun_sentences 

    def construct_document(self, content, filename):
        #Initializes the text parser
        parser = TextParser()
        noun_sentences = self.parse_content(parser, content)
        total_trees = nouns_to_tree(noun_sentences)
        document = Document()
        document.set_trees(total_trees)
        output, node_dict = document.trees_reordering()
        contents_to_id = {}
        build_links(contents_to_id, node_dict, output)
        visited_ids = set()
        visited_contents = set()
        result_trees = []
        for i in range (1, len(node_dict)):
            if i not in visited_ids:
                if i in node_dict:
                    node_tree = document.recurse_node(node_dict[i], visited_ids, visited_contents, 0)[0]
                    result_trees.append(node_tree)
                #print(node_tree)

        total_nouns = {}


        total_read_trees = []
        span_trees = []
        # first_tree = result_trees[2]
        # output = read_tree(first_tree)
        # print(extract_nouns(output, "", 0))         
        for tree in result_trees:
            # print("------")
            node_positions = []
            visited_nodes = set()
            #print("####")
            #print(tree)
            #print("----")
            # reading_output = read_tree(tree)
            output = read_tree(tree)
            # print(output)
            noun_string = extract_nouns(output, "", 0)
            if noun_string:
                if len(noun_string) > 10:
                    segments = noun_string.split("  ")
                    stripped_segments = [x for x in segments if x not in ["", "'", "’", "”", "”"]]
                    for strip in stripped_segments:
                        words = strip.split(" ")
                        if len(words) > 1:
                            for i in range(0, len(words)-1):
                                first_word = words[i]
                                second_word = words[i+1]
                                # print(first_word, second_word)
                                if first_word.strip() and second_word.strip():
                                    if first_word in total_nouns:
                                        total_nouns[first_word].append(second_word)
                                    else:
                                        total_nouns[first_word] = [second_word]

                            # print(words)

            # total_read_trees.append(output)
            # print(tree)
            # print(output)
            #recurse_output = recurse_list(output, visited_nodes, 0, 0, node_positions)
            # print(build_spanning_tree(tree, node_dict))
            #print(read_tree(tree))

        # print(total_read_trees)

        # prior_word = ""
        # held_nouns = {}
        first_nouns = set({x for x in total_nouns.keys()})
        shared_nouns = set()
        for noun in first_nouns:
            items = total_nouns[noun]
            for item in items:
                if item in first_nouns:
                    shared_nouns.add(item)
        head_nouns = [x for x in first_nouns if x not in shared_nouns]
        

        
        def recurse_sequential(items, word_dict, visited_words):
            for item in items:
                if item not in visited_words:
                    visited_words.add(item)
                else:
                    return ""
                if item in word_dict:             
                    return f"{item} {recurse_sequential(word_dict[item], word_dict, visited_words)}"
                else:
                    return f"{item}"
                
        # distinct_words = set()
        # distint_links = set()

        # for head in head_nouns:
        #     items = total_nouns[head]
        #     visited_words = set()
        #     items = recurse_sequential(items, total_nouns, visited_words)
        #     words = items.split(" ")
        #     for i in range(0, len(words)-1):
        #         distinct_words.add(words[i])
        #         distinct_words.add(words[i+1])
        #         distint_links.add((words[i],words[i+1]))
        
        # # print(distinct_words)
        # # print(distint_links)

        # generateGraphViz(distinct_words, distint_links, filename)
        # document.set_graph_links(distint_links)
        # document.set_graph_nodes(distinct_words)

        # self.total_nodes = self.total_nodes.union(distinct_words)
        # self.total_links = self.total_links.union(distint_links)



        # self.add_document(document)
        
            # for word in words:
            #     distinct_words.add(word)
            

        # print(head_nouns)






        # for tree in total_read_trees:
        #     #extract_nouns(tree, "", held_nouns)
        #     print(tree)
            
        #     print("#####")
        #print(held_nouns)
        # print(span_trees)
       # print("\###########NEXT DOCUMENT###########\n")

