#This will handle the conversion of text into a series of nouns. This task is done a lot and will be a frequent test case, so it is implemented now.
import nltk
from nltk.corpus import wordnet
from utility import *

class Converter():
    text = ""
    sentences = []
    tags = []
    sentence_tags = []
    trees = []
    nodes = []
    node_id = 0
    link_id = 0
    tree_id = 0

    def __init__(self, text) -> None:
        self.text = text
        self.sentences = text.split(".")
        self.tags = []
        self.sentence_tags = []
        self.trees = []
        self.nodes = []
        self.node_id = 0
        self.link_id = 0
        self.tree_id = 0

    #Here I will add the nltk pos tagger, then iterate through all those nouns and add nodes. 
    def tag(self):
        tokens = nltk.word_tokenize(self.text)
        pos_tags = nltk.pos_tag(tokens)
        self.tags = pos_tags
        return pos_tags
    
    def tag_sentences(self):
        sentence_tags = []
        for sentence in self.sentences:
            tokens = nltk.word_tokenize(sentence)
            pos_tags = nltk.pos_tag(tokens)
            sentence_tags.append(pos_tags)
        self.sentence_tags = sentence_tags

    
    def get_nouns(self):
        noun_tags = [x for x in self.tags if x[1][0:2] == "NN"]
        return noun_tags
    
    def get_sentence_nouns(self):
        tagged_sentences = []
        for sentence in self.sentence_tags:
            noun_tags = [x for x in sentence if x[1][0:2] == "NN"]
            tagged_sentences.append(noun_tags)
        return(tagged_sentences)
    
    def build_nodes(self, sentence):
        nodes = []
        for pair in sentence:
            word = pair[0]
            noun_type = pair[1]
            self.node_id += 1
            word_node = Node(self.node_id)
            word_node.set_name(noun_type)
            word_node.set_contents(word)
            nodes.append(word_node)
        return nodes

    
    def build_links(self, nodes):
        links = []
        prior_link = None
        pos = ["START","END"]
        for i in range (0, len(nodes)):
            self.link_id +=1
            node = nodes[i]
            link = Link(node, self.link_id)
            link.set_nature("BEFORE")
            if prior_link:
                prior_link.set_end(node)
                links.append(prior_link)
            prior_link = link
        
        links.append(prior_link)
        return links

    def get_trees(self):
        return self.trees
        

