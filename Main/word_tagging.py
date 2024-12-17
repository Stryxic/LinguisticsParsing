#This will handle the conversion of text into a series of nouns. This task is done a lot and will be a frequent test case, so it is implemented now.
import nltk
from nltk.corpus import wordnet

class Converter():
    text = ""
    sentences = []
    tags = []
    sentence_tags = []

    def __init__(self, text) -> None:
        self.text = text
        self.sentences = text.split(".")

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
