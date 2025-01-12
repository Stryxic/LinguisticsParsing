#Handles conversion of incoming text into its discrete words. Should contain capability for parsing a document into paragraphs, paragraphs into sentences, and sentences into words.
import nltk
from nltk.corpus import wordnet
class TextParser():

    def __init__(self) -> None: 
        self.text = ""
        self.paragraphs = []
        self.sentences = []
        self.para_dict = {}

    
    def set_text(self, text):
        self.text = text

    def split_paragraphs(self, input):
        paragraphs = input.split("\n\n")
        return paragraphs
    
    def split_sentences(self, input):
        sentences = input.split(". ")
        sentences = [x.strip() + "." for x in sentences]
        return sentences
    
    def process_text(self):
        para_count = 0
        self.paragraphs = self.split_paragraphs(self.text)
        for paragraph in self.paragraphs:
            self.sentences += self.split_sentences(paragraph)
            self.para_dict[para_count] = self.split_sentences(paragraph)
            para_count +=1

    def get_paragraphs(self):
        return self.paragraphs
    
    def get_sentences(self):
        return self.sentences
    
    def get_para_dict(self):
        return self.para_dict

    def extract_nouns(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        pos_tags = nltk.pos_tag(tokens)
        noun_tags = [x for x in pos_tags if x[1][0:2] == "NN"]
        return noun_tags

    def reset_fields(self):
        self.text = ""
        self.paragraphs = []
        self.sentences = []
        self.para_dict = {}