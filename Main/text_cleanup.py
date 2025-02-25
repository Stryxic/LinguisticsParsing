import os
from main import parse_document
from utility import *
import re
from langdetect import detect

def sanitize_file(filename, parser, distinct_nodes, viz_links):
    with open(f"articles/{filename}.txt", encoding="utf-8") as f:
        contents = f.read()
    total_sentences = contents.split("\n")
    illegal_strings = ["©","advertising", "non-advertising","cookies","cookie","terms","conditions",
                       "privacy", "Advertising", "device","setAttribute",
                         "iframe", "site", "sites", "adverts","advertising", "analytics", "website", "newsletter", "privacy",
                           "notice", "subscription", "ads", "subscribe", "newsletter"]
    content = []
    # print("\n\n##\n\n")
    for sentence in total_sentences:
        clean_sentence = re.sub("[“|”|'|&|’]", "", sentence)
        ascii_str = "".join([x for x in sentence if x.isascii()])
        clean_sentence = re.sub("[?|!]", ".", clean_sentence)
        expression = re.compile("[^\u0000-\u007F]+")
        regex_check = re.search(expression,clean_sentence)
        diacritics = re.compile("[À-ÖØ-öø-įĴ-őŔ-žǍ-ǰǴ-ǵǸ-țȞ-ȟȤ-ȳɃɆ-ɏḀ-ẞƀ-ƓƗ-ƚƝ-ơƤ-ƥƫ-ưƲ-ƶẠ-ỿ]")
        diacritics_check = re.search(diacritics, clean_sentence)
        word_subset = [x for x in illegal_strings if x.lower() in clean_sentence.lower()]
        if clean_sentence:
            try:
                langauge = detect(clean_sentence)
            except:
                langauge = ""
        else:
            langauge = ""
        # print(word_subset)
        if word_subset == [] and langauge == "en":
            #clean_sentence = sentence.replace("  ", " ")
            # clean_sentence = re.sub("[“|”|'|&|’]", "", sentence)
            # clean_sentence = re.sub("[?|!]", ".", clean_sentence)
            # clean_sentence = clean_sentence.replace("“", "")
            # clean_sentence = clean_sentence.replace("”", "")
            # clean_sentence = clean_sentence.replace("'", "")
            # clean_sentence = clean_sentence.replace('"', "")
            clean_sentence = clean_sentence.replace("[", "")
            clean_sentence = clean_sentence.replace("]", "")
            clean_sentence = clean_sentence.replace('"', "")
            clean_sentence = clean_sentence.replace("  ", " ")
            # clean_sentence = clean_sentence.replace('&', "")
            # clean_sentence = clean_sentence.replace("?", ".")
            # clean_sentence = clean_sentence.replace("!", ".")
            content.append(clean_sentence)
        # else:
        #     print(f"Sentence Removed: {sentence}")
    

    content = "\n ".join(content)
    content.replace("  ", " ")
    if content:
        with open(f"cleaned_articles/{filename}.txt", "w", encoding="utf-8") as f:
            f.write(content)




    # if content:
    #     try:
    #         distinct_nodes, viz_links = process_file(content, parser, distinct_nodes, viz_links)
    #         # generateGraphViz(distinct_nodes, viz_links, filename)
    #     except IndexError:
    #         print("Error")
    #     except TypeError:
    #         print("Error")

    



    # print(content)
        # if "Privacy Policy" not in sentence:
        #     words = set(sentence.split(" "))        
        #     if not words.intersection(illegal_strings):
        #         clean_sentence = sentence.replace("  ", " ")
        #         print(clean_sentence)
    

def cleanup(directory):
    file_names = os.listdir(directory)
    article_names = set(["-".join(x.split("-")[0:5]) for x in file_names])
    for article in article_names:
        parser = TextParser()
        distinct_nodes = set()
        viz_links = []        
        article_subset = [x.split(".")[0] for x in file_names if article in x]
        article_ids = [int(x.split("-")[-1].split(".")[0]) for x in article_subset]
        #print(article_subset)
        #print(article_ids)
        for file in article_subset:
            # with open(f"cleaned_articles/{file}.txt", encoding="utf-8") as f:
            #     contents = f.read()
            # if contents:
            #     process_file(contents,parser,distinct_nodes,viz_links)
            sanitize_file(file, parser, distinct_nodes, viz_links)

        #     process_file()
        # parse_document(article_subset, f"{article}-output_clean")

    #print(article_names)
    
def load_trees(directory):
    file_names = os.listdir(directory)
    for file in file_names:
        load_tree_from_signature(file)
        


dir = "E:\PhD\OpenSource\LinguisticsParsing\Main\\articles\\"
cleanup(dir)
# dir = "E:\PhD\OpenSource\LinguisticsParsing\Main\\json_signatures\\"
# load_trees(dir)
# parse_document()



# analyse_file(content, "gender_care-3")