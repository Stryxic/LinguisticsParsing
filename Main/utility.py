#This will hold the most used functions across all of the documents, the core functionality.


#Node - The basic unit of anything in the system. Very generic, abstract.

import math
import pandas as pd

class Node():

    #Each node has an identity (an ID number), a name, zero to many links, and whatever it contains. The contents are generic, links are a specific type, id is an int, and name is a string.
    id = 0
    name = ""
    links = []
    content = None


    def __init__(self, id) -> None:
        self.id = id
        self.links = []
        self.content = None
        self.name = ""
    
    def __init_subclass__(cls) -> None:
        pass


    def __repr__(self) -> str:
        return str(self.id)

    def __str__(self) -> str:
        return str(f"{self.id}-{self.name}")

    def __eq__(self, __value: object) -> bool:
        if self.name == __value.name and self.content == __value.content and self.links == __value.links:
            return True
        else:
            return False

    def set_contents(self, contents):
        self.content = contents

    def set_name(self, name):
        self.name = name

    def change_id(self, id):
        self.id = id


    #A link is a different object. It contains a start point, an end point, and a type. The link can either be from or to the node. 
    def add_link(self, link):
        self.links.append(link)

    def get_children(self) -> object:
        children = []
        for link in self.links:
            if link == "child":
                children.append(link)
        return children

    def get_name(self):
        return self.name
    
    def get_contents(self):
        return self.content


#Link - Any connection between one Node and another Node
    
class Link():
    id = 0
    nature = None
    start = None
    end = None

    #all links must at the least have a starting node. A link with no terminal is a possible, but not actualised, connection.
    def __init__(self, node, id) -> None:
        self.start = node
        self.id = id
        self.nature = None
        self.end = None

    def __repr__(self) -> str:
        return f"{self.id}:{self.nature}"

    def __str__(self) -> str:
        return f"{self.start}-[{self.nature}]->{self.end}"
    
    

    #terminal of the link. Each link can only have one starting node, and one ending node. These nodes can also act as greater subgroup of several nodes.
    def set_end(self, node) -> None:
        self.end = node

    def get_end(self) -> Node:
        return self.end
    
    def get_start(self) -> Node:
        return self.start
    
    def get_id(self) -> int:
        return self.id

    def get_terminals(self):
        if self.end:
            return [self.start.get_contents(), self.end.get_contents()]
        else:
            return [self.start.get_contents()]

    #A nature is a type of fixed, limited domain of features. It would be best represented as some type of enum.
    def set_nature(self, nature) -> None:
        self.nature = nature

    #A link is equal to another link if its start, end, and nature are equivalent. 
    def __eq__(self, __value: object) -> bool:
        if __value.start:
            if self.nature == __value.nature and self.start == __value.start and self.end == __value.end:
                return True
            else:
                return False
        else:
            return False



#Tree - The collection of Links and Nodes
        

class Tree():
    id = 0
    nodes = []
    links = []


    #The minimal tree is a Node -> Node
    def __init__(self, node_1:Node, node_2:Node, link:Link, id) -> None:
        self.nodes = []
        self.links = []
        self.nodes.append(node_1)
        self.nodes.append(node_2)
        self.links.append(link)
        self.id = id
        
    def get_nodes(self) -> Node:
        return self.nodes
        
    def get_links(self) -> Link:
        return self.links
    
    def add_node(self, node:Node):
        self.nodes.append(node)
    
    def remove_node(self, id):
        removal = None
        for node in self.nodes:
            if node.id == id:
                removal = node
                break
        if removal:
            self.nodes.remove(removal)

    def add_link(self, link:Link):
        if link.end:
            if link.get_end() not in self.nodes:
                self.add_node(link.get_end())
        self.links.append(link)
    
    def remove_link(self, id):
        pos = 0
        for i in range (0, len(self.links)):
            link = self.links[i]
            if link.get_id() == id:
                pos = i
        if pos:
            self.links.pop(pos)


    def __str__(self) -> str:
        tree_str = ""
        for link in self.links:
            tree_str += str(link) + "\n"

        tree_str = tree_str.strip()
        return tree_str
    
    #Gives a better representation for the whole tree, without overriding _repr_ if I need it later.
    def traverse_tree(self) -> str:
        output_str = ""
        for link in self.links:
            terminals = link.get_terminals()
            if len(terminals) == 2:
                if output_str:
                    output_str += f"{terminals[1]}#{link.get_end().get_name()}->"
                else:
                    output_str += f"{terminals[0]}#{link.get_start().get_name()}->{terminals[1]}#{link.get_end().get_name()}->"
        return output_str


#Parsing the tree we just made.
class TreeParser():
    tree = None
    noun_list = []
    noun_dict = {}
    noun_ratios = {}
    #Storing a list of all nouns, and the count.
    def __init__(self, tree):
        self.tree = tree
        self.noun_list = []
        self.noun_dict = {}

    #Check what kind of node it is, and parse it.
    def parse_tree(self):
        links = self.tree.get_links()
        for link in links:
            start_node = link.get_start()
            end_node = link.get_end()
            self.parse_node(start_node, 1)
            if end_node:
                self.parse_node(end_node, 2)
        self.count_nouns()

    #Trees have nodes to be parsed, so recusrively call the parse node function
    def parse_tree_node(self, node):
        tree = node.get_contents()
        node_links = tree.get_links()
        if node_links: 
            for link in node_links:
                first_node = link.get_start()
                second_node = link.get_end()
                self.parse_node(first_node, 1)
                if second_node:
                    self.parse_node(second_node, 2)

    #Text contains a noun, and a noun type
    def parse_text_node(self, node):
        noun_type = node.get_name()
        noun = node.get_contents()
        self.noun_list.append([noun,noun_type])

    #A node can either be a tree, or text.
    def parse_node(self, node, pos):
        node_name = node.get_name()
        if pos == 1:
            if node_name == "Tree":
                self.parse_tree_node(node)
            else:
                self.parse_text_node(node)

    def get_nouns(self):
        return self.noun_list
    
    #Simple pythonic invocation to convert a list into a count
    def count_nouns(self):
        for noun in self.noun_list:
            noun = noun[0].lower()
            if noun in self.noun_dict.keys():
                self.noun_dict[noun] += 1
            else:
                self.noun_dict[noun] = 1
                
    def get_counts(self):
        return self.noun_dict
    

    #Find the sum of all the counts, then divide each element and add it to a new dict
    def find_ratios(self):
        total_count = 0
        for noun in self.noun_dict.keys():
            total_count += self.noun_dict[noun]
        for noun in self.noun_dict.keys():
            self.noun_ratios[noun] = self.noun_dict[noun]/total_count
    
    def get_ratios(self):
        return self.noun_ratios

#Creating implementation of a document. It has text, statistics, and processes those.
class Document():
    text = ""
    sentences = []
    ratios = {}
    dataframe = None
    current_ratio = 0
    definitions = {}
    read_words = []
    tree = None
    #Definitions are going to be a special case for a sentence with only two nouns. They are directly related, and so a preposition is formed from them.

    def __init__(self, text):
        self.text = text
        self.sentences = []
        self.ratios = {}
        self.dataframe = None
        self.definitions = {}
        self.read_words = []
        self.tree = None

    def find_sentences(self):
        sentences = self.text.split(".")
        self.sentences = sentences

    def set_ratios(self, ratios):
        self.ratios = ratios

    def get_tree(self):
        return self.tree

    def find_avg(self):
        dataframe = pd.DataFrame.from_dict(self.ratios, orient = 'index')
        dataframe = (dataframe - dataframe.mean())/dataframe.std()
        self.dataframe = dataframe

    def find_min_diff(self, item, items):
        print("")
        # item_index = items.index(item)
        # del items[item_index]
        # print(item, items)


    #Small temporary function which should take in each row of the dataframe and comput similarity.
    def find_diff(self, val):
        squared_val = val**2 - self.current_ratio**2
        return math.sqrt(abs(squared_val))


    #Main function to process the text stored in the document. 
    #It requires self.ratios to function, and converts the written text
    #into a series of initial definitions based on the text+ratios.
    #It does not need to return anything, as it is operating on self.
    
    def process_text(self):
        #Defining an array to hold each word in the document
        #read_words = []
        #Iterating through each sentence in the paragraph
        for sentence in self.sentences:
            print("------")
            #Array for each word in the sentence
            sentence_words = []
            words = sentence.lower().split(" ")
            cleaned_words = [x.strip() for x in words if x]
            #removing whitespace
            for word in cleaned_words:
                #If there is a relation known
                if word in self.ratios:
                    #find the ratio of word occurence in the overall document
                    ratio = self.dataframe.loc[word]
                    value = ratio.values[0]
                    #Add it to the total list, and current iteration list
                    self.read_words.append([word, value])
                    sentence_words.append([word, value])
            #When iterating through, we store the prior words.
            prior_words = []
            for i in range(0, len(sentence_words)-1):
                word = sentence_words[i]
                word = word[0]
                prior_words.append(word)

            #If there are nouns in the sentence
            if sentence_words:
                print(f"Prior words: {prior_words} | Last word: {sentence_words[-1]}")
                available_links = {}
                #Last noun = last word in the sentence
                last_word = sentence_words[-1]
                #Each word is checked against all the words that have come before it in that sentence
                for word in prior_words:
                    value = self.dataframe.loc[word].values[0]
                    available_links[word] = value
                link_df = pd.DataFrame.from_dict(available_links, orient="index")
                self.current_ratio = last_word[1]
                outputs = [self.find_diff(x[0]) for x in link_df.values]
                outputs_nonzero = [x for x in outputs if x > 0]
                #Finding the similarity between the last words value, and each prior word. Selecting the smallest difference.
                if outputs_nonzero:
                    min_val = min(outputs_nonzero)
                else:
                    min_val = 0
                
                #If no nonzero value is found, defaults to the first noun in the sentence.
                occurance = outputs.index(min_val)

                #Finds its position in the list
                linked_word = sentence_words[occurance]
                # If a sentence is of the form x is y, that is a simple, base case relation. If there are more words, then either it uses a prior definition, or the new word.
                if len(sentence_words) == 2:
                    self.definitions[linked_word[0]] = last_word[0]
                else:
                    if last_word[0] in self.definitions.values():
                        pos = list(self.definitions.values()).index(last_word[0])
                        key_word = list(self.definitions.keys())[pos]
                        self.definitions[linked_word[0]] = key_word
                    else:
                        self.definitions[linked_word[0]]=last_word[0]
    
    def build_root(self):
        #Converting all nouns into just the ones which we have links for.
        word_order = [x[0] for x in self.read_words if x[0] in self.definitions.keys()]
        word_nodes = []
        word_links = []
        word_node_dict = {}
        node_id = 1
        for word in word_order:
            word_node = Node(node_id)
            if word not in word_node_dict.keys():
                node_id+=1
                word_node.set_contents(word)
                word_node.set_name("Word")
                word_node_dict[word] = word_node
                word_nodes.append(word_node)
            else:
                word_node = word_node_dict[word]
            
            related_word = self.definitions[word]

            related_node = Node(node_id)
            if related_word not in word_node_dict.keys():
                node_id+=1
                related_node.set_contents(word)
                related_node.set_name("Word")
                word_node_dict[related_word] = related_node
                word_nodes.append(related_node)
            else:
                related_node = word_node_dict[related_word]



            # print(word, related_word)
            # print(word_node, related_node)
        node_contents = [x.get_contents() for x in word_nodes]
        unique_words = []
        tree_node_id = 1
        link_id = 1
        node_one = word_nodes[0]
        node_one.change_id(tree_node_id)
        tree_node_id += 1
        first_link = Link(node_one, link_id)
        first_link.set_nature("->")
        link_id += 1
        node_two = None
        tree_nodes = {}

        tree_nodes[node_one.get_contents()] = node_one
        for content in node_contents:
            if content not in unique_words:
                unique_words.append(content)
                if len(unique_words) == 2:
                    node_two = word_nodes[node_contents.index(content)]
                    node_two.change_id(tree_node_id)
                    tree_nodes[content] = node_two
                    first_link.set_end(node_two)
                    self.tree = Tree(node_one, node_two, first_link, 1)
                if self.tree:
                    tree_node = Node(tree_node_id)
                    tree_node_id += 1
                    tree_node.set_name("Word")
                    tree_node.set_contents(content)
                    self.tree.add_node(tree_node)
                    new_link = Link(tree_node, link_id)
                    link_id+=1
                    new_link.set_nature("->")
                    related_word = self.definitions[content]
                    if related_word not in unique_words:
                        related_node = Node(tree_node_id)
                        tree_node_id+=1
                        related_node.set_contents(related_word)
                        related_node.set_name("Word")
                        self.tree.add_node(related_node)
                        new_link.set_end(related_node)
                        self.tree.add_link(new_link)
                    else:
                        related_node = tree_nodes[related_word]
                        new_link.set_end(related_node)
                        self.tree.add_link(new_link)

            

                # print(node_contents.index(content))
        
        # print(word_nodes)
        # print(word_node_dict)
        # print(node_contents)
        # print(unique_words)
        # print(self.tree)
        # print(self.tree.traverse_tree())







