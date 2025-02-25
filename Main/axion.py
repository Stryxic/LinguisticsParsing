import re
import nltk
from ordered_set import OrderedSet
import json
import os

def parse(msg):
    #To convert a message: 
    # - Remove all whitespace from newline up until the first character
    # - Remove all double newlines, replace with single newlines
    # - Merge newlines with single characters up
    cleaned_msg = re.sub("\n\s*", "\n", msg)
    cleaned_msg = re.sub("\n\n+", "\n", cleaned_msg)
    cleaned_msg = re.sub("\n(.)\n", ".\1", cleaned_msg)
    cleaned_msg = re.sub("(\s)\s+", ".\1", cleaned_msg)
    cleaned_msg = re.sub("https://", " ", cleaned_msg)
    cleaned_msg = re.sub("[?|!]", ".", cleaned_msg)
    cleaned_msg = re.sub("\n\s+", "\n", cleaned_msg)
    cleaned_msg = re.sub("\n", ". \n", cleaned_msg)
    cleaned_msg = re.sub("\.\.+", ".", cleaned_msg)
    cleaned_msg = re.sub("['|’]", "", cleaned_msg)
    cleaned_msg = re.sub("/", " ", cleaned_msg)
    cleaned_msg = re.sub("\n\.*\n", "", cleaned_msg)
    cleaned_msg = re.sub('\."\.', ".", cleaned_msg)
    return cleaned_msg

def check_msg(msg, count):
    cleaned_text = parse(msg)
    #Cleaned text will convert it into a list of arrays of nouns
    signature = []
    #Parse the message here, break it into the nouns for the signature
    lines = cleaned_text.split(".")
    messages = [x.strip().replace("\x01", "").lower() for x in lines if x.strip()]
    total_nouns = []
    pair_strings = []
    output_json = []
    for message in messages:
        nouns = extract_nouns(message)
        total_nouns.append(nouns)

    for nouns in total_nouns:
        words = [x[0].lower() for x in nouns]
        if len(words) > 1:
            pair_strings.append(words)

    visited_items = set()
    word_positions = {}

    def insert_item(object, item_1, item_2):
        object_keys = object.keys()
        object_items = [object[x] for x in object] #[1,2,3] ["a", "b", "c"] [{}, {}, {}]

        if item_2 in object:
            object = {item_1:object}
            return object
        
        if item_1 in object:
            items = [x for x in object if item_1 in x]
            object[f"{item_1}.{len(items)}"] = item_2


        for key in object:
            item = object[key]
            if item_1 == item:
                object[key] = {item_1:item_2}

            if type(item) == dict:
                output = insert_item(item, item_1, item_2)
                if output:
                    return output
        
    def build_pairs(pair_string, pair_set):
        # total_pairs = set()
        for i in range(0, len(pair_string)-1):
            item_1 = pair_string[i]
            item_2 = pair_string[i+1]     
            pair_set.add((item_1, item_2))


    total_output = OrderedSet()
    for pairs in pair_strings:
        build_pairs(pairs, total_output)
    # print(total_output)

    if total_output:
        #Get the first item. If there's only one, there will only be one pair in the output.
        first_pair = total_output[0]
        output_json.append({first_pair[0]:first_pair[1]})
        total_output = total_output[1:]
        word_positions[first_pair[0]] = 0
        word_positions[first_pair[1]] = 0
        visited_items.add(first_pair[0])
        visited_items.add(first_pair[1])
        pair_index = 1
        # print(total_output)
        for pair in total_output:
            item_1 = pair[0]
            item_2 = pair[1]
            if item_1 in visited_items and item_2 in visited_items:
                continue
            item_dict = {item_1:item_2}
            if item_1 in visited_items:
                if item_1 not in word_positions:
                    continue
                # print(item_1, item_2, word_positions)
                found_pos = word_positions[item_1]
                word_positions[item_2] = found_pos
                visited_items.add(item_2)
                # print(f"Inserting [{item_1}, {item_2} at {found_pos}]")
                insert_item(output_json[found_pos], item_1, item_2)
                continue


            if item_2 in visited_items:
                if item_2 not in word_positions:
                    continue
                found_pos = word_positions[item_2]
                parent_tree = output_json[found_pos]
                visited_items.add(item_1)
                # insert_item(parent_tree, item_1, item_2)

                continue


            output_json.append({item_1:item_2})
            word_positions[pair[0]] = pair_index
            word_positions[pair[1]] = pair_index
            visited_items.add(pair[0])
            visited_items.add(pair[1])
            pair_index+=1


    # print(output_json)
    with open(f"signatures/total-{count}.json", "w") as json_file:
        json.dump(output_json, json_file, indent=4)
    # print("-----")



def extract_nouns(msg):
    tokens = nltk.word_tokenize(msg)
    pos_tags = nltk.pos_tag(tokens)
    noun_tags = [x for x in pos_tags if x[1][0:2] == "NN"]
    return noun_tags


def run_test():
    filename = "E:\PhD\OpenSource\LinguisticsParsing\Main\working_files\\automod_test.txt"
    with open(filename, "r", encoding="utf-8") as f:
        messages = f.read()
        messages = messages.split("#-#")
        message_count = 1
        for message in messages:
            lines = message.split("\n")
            content = "\n".join(lines[2:])

            clean_msg = parse(content)
            check_msg(clean_msg, message_count)
            message_count += 1
        # print(messages)


# run_test()


def test_files():
    dir = "E:\PhD\OpenSource\LinguisticsParsing\Main\\working_files\\"
    file_names = os.listdir(dir)
    message_count = 1
    for file in file_names:
        with open(f"{dir}\{file}", "r", encoding="utf-8") as f:
            content = f.read()
            clean_msg = parse(content)
            check_msg(clean_msg, message_count)
            message_count += 1
        # load_tree_from_signature(file)
        


def parse_content(content, id):
    clean_msg = parse(content)
    check_msg(clean_msg, id)

def combine_signatures(signatures):
    for sig in signatures:
        print(sig)
test_files()