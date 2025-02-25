import json
import os
import re
from ordered_set import OrderedSet

class Signature():
    def __init__(self, id):
        self.sig = None
        self.id = id
        self.total_words = set()
        self.word_locations = {}
        self.pairs = OrderedSet()

    def load_file(self, file):
        self.sig_json = json.load(file)


    def extract_words(self, object, prior_word):
        if type(object) == dict:
            for key in object:
                self.total_words.add(key)
                self.pairs.add((prior_word, key))
                self.word_locations[key] = object
                self.extract_words(object[key], key)

        if type(object) == list:
            for item in object:
                self.extract_words(item, prior_word)
            
        if type(object) == str:
            self.total_words.add(object)
            self.pairs.add((prior_word, object))

    def find_words(self):
        for element in self.reduced_json:
            self.extract_words(element, "")
        # print(self.total_words)
        print(self.pairs)
        self.word_keys = self.word_locations.keys()

    def reduce(self,filename):
        print("----")
        self.visited_words = set()
        output = []
        for tree in self.sig_json:
            #self.recurse_dict(tree)
            tree_result = self.recurse(tree)
            if tree_result:
                output.append(tree_result)
            #output.append(self.recurse(tree))


        # print(self.sig_json)
        # print(output)
        self.reduced_json = output
        with open(f"reductions/{filename}-{self.id}.json", "w") as json_file:
            json.dump(output, json_file, indent=4)
        
        # print(output)



    

    def recurse(self, current_dict):
        # print(current_dict)
        #Assuming that it's a dict, we get the first key and use this to check for the base case i,e {var:str}
        first_key = next(iter(current_dict.keys()))
        if type(current_dict[first_key]) == str:
            if len(current_dict) == 1:
                return current_dict
            else:
                return {first_key:[current_dict[x] for x in current_dict]}
        # if len(current_dict) == 1 and type(current_dict[first_key]) == str:
        #     return current_dict
        #Next case is when the item is another dict
        if len(current_dict) == 1:
            dict_output = self.recurse(current_dict[first_key])
            if dict_output:
                return {first_key:dict_output}
            else:
                return current_dict
        else:
            remaining_items = [x for x in current_dict.keys()][1:]
            # print(remaining_items)
            child_output = [self.recurse(current_dict[first_key])]
            # child_output = []
            for item in remaining_items:
                # print(item)
                contents = current_dict[item]
                if type(contents) == str:
                    child_output.append(contents)
                else:
                    child_output.append(self.recurse(contents))
            
            return {first_key:child_output}
        








        # print(dict)
        # if type(dict) == list:
        #     print(dict)
        #     return dict
        # dict_keys = dict.keys()
        # root_positions = {}
        # first_key = next(iter(dict.keys()))
        # first_item = dict[first_key]   
        # output = []
        # if len(dict_keys) == 1:
        #     if first_key in self.visited_words:
        #         return dict
        #     else:
        #         # return {first_key:self.recurse(first_item)}
        #         self.visited_words.add(first_key)
        #     if type(first_item) == str:
        #         return dict
        #     else:
        #         # print("FIRST ITEM:")
        #         # print(first_key)
        #         # print(first_item)
                
        #         # output = {}
        #         print(first_key)
        #         return {first_key:self.recurse(first_item)}

        # else:
        #     add_ons = [x for x in dict_keys if first_key in x and "." in x]
        #     # print(add_ons)
        #     for add_on in add_ons:
        #         if type(dict[add_on]) == {}:
        #             recurse_output = self.recurse(dict[add_on])
        #             print(recurse_output)
                # else:
                #     if type(dict[add_on]) == str:
                #         output.append(dict[add_on])
                    # else:
                    #     for x in dict[add_on]:
                    #         if type(x) == {}:
                    #             output.append(self.recurse(x))
                    #         else:
                    #             output.append(x)


            # extra_items = []
            # for extra in add_ons:
            #     item = dict[extra]
            #     if type(item) == type({}):
            #         extra_items.append(self.recurse(item))
            #     # print(item)
            #     else:
            #         extra_items.append(dict[extra])
            # # print(extra_items)
            # string_items = [x for x in extra_items if type(x) == str]
            # other_items = [x for x in extra_items if type(x) != str]
            # # print(string_items)
            # # print(other_items)
            # output += string_items
            # if other_items:
            #     # print(other_items)
            #     for item in other_items:
            #         if type(item) == type({}):
            #             variable = self.recurse(item)
            #             output.append(variable)
                #         print(variable)
                # print("\n\n")

            # for x in other_items:
            #     output.append(self.recurse(x))



            # for x in extra_items:
            #     if x not in output:
            #         if type(x)=={}:
            #             output.append(self.recurse(x))
            #         else:
            #             output.append(x)
            # output += extra_items
        # return {first_key:output}
            # print(dict_keys)
            # print(add_ons)
            # print(extra_items)


                # return dict

        # else:
            # extra_terms = [x for x in dict_keys if re.search("\.[1-9]", x)]
            # if extra_terms:
            #     base_terms = [x for x in dict_keys if x not in extra_terms]
            #     # print(extra_terms)
            #     # print(base_terms)
            #     output_index = 0
            #     for term in base_terms:
            #         item = dict[term]
            #         output = []
            #         root_positions[term] = output_index
            #         if type(item) == dict:
            #             output.append(self.recurse(item))
            #         else:
            #             output.append(item)


                # distinct_words = set([x.split(".")[0] for x in extra_terms])
                # print("Distinct words:")
                # print(distinct_words)

                # string_entries = {x:[dict[y] for y in extra_terms if x in y and type(dict[y]) == str] for x in distinct_words}
                    


                # secondary_outputs = {x:[dict[y] for y in extra_terms if x in y] for x in distinct_words}
                # print("Secondary Outputs:")
                # print(string_entries)
                # cleaned_outputs = []
                # if len(secondary_outputs) > 1:
                #     for sec_output in secondary_outputs:
                #         cleaned_outputs.append(sec_output)
                # for x in secondary_outputs:

                #     found_outputs = secondary_outputs[x]  


                #     # for element in found_outputs:
                #     #         cleaned_outputs.append(element)
                    
                #     if cleaned_outputs:
                #         print("Clean")
                #         print(cleaned_outputs)



                # for term in extra_terms:
                #     # print(extra_terms)
                #     root_term = term.split(".")[0]
                #     if "1" in term.split(".")[1]:
                #         output[root_positions[root_term]] = [output[root_positions[root_term]]]


                #     if type(dict[term]) == dict:
                #         output[root_positions[root_term]].append(self.recurse(item))
                #     else:
                #         # print(f"Appending {item}")
                #         output[root_positions[root_term]].append(item)

                


                # for x in cleaned_outputs:
                #     if type(x) == str:
                #         if len(x) > 1:
                #             output += x
                #     else:
                #         output += x
                # return output
            # else:
            #     print("End Case")
            #     print(dict)
            #     return dict        


    ####This is not used


    def recurse_dict(self, dict):
        dict_keys = dict.keys()
        root_words = {}
        extra_terms = [x for x in dict_keys if re.search("\.[1-9]", x)]
        # print(extra_terms)
        base_terms = []
        if extra_terms:
            for term in extra_terms:
                root_word = term.split(".")[0]
                found_dict = dict[term]
                if type(found_dict) == dict:
                    self.recurse_dict(found_dict)
                # else:
                #     root_words[root_word].append(found_dict)
                if root_word in root_words:
                    root_words[root_word].append(dict[term])
                else:
                    root_words[root_word] = [dict[term]]
        
        # print(root_words)
        for key, item in dict.items():
            print(f"Key: {key}")
            # print(key, item)
            if key in root_words:
                root_words[key] = [item] + root_words[key]
            else:
                if key not in extra_terms:
                    root_words[key] = [item]
                    if type(item) == dict:
                        self.recurse_dict(item)

            
            if type(item) == dict:
                self.recurse_dict(item)
            else:
                if key not in extra_terms:
                    root_words[key] = [item] + root_words[key]

            # print(root_words)




def merge_dict(d1, d2):
    """Recursively merges d2 into d1, ensuring each word is added only once."""
    for key, value in d2.items():
        if key in d1:
            if isinstance(d1[key], dict) and isinstance(value, dict):
                merge_dict(d1[key], value)
            elif isinstance(d1[key], list) and isinstance(value, list):
                d1[key] = list(set(d1[key] + value))  # Ensure uniqueness
            elif d1[key] != value:
                d1[key] = list(set([d1[key], value])) if not isinstance(d1[key], list) else list(set(d1[key] + [value]))
        else:
            d1[key] = value if not isinstance(value, list) else list(set(value))

def merge_json_files():
    merged_data = {}
    dir = "E:\PhD\OpenSource\LinguisticsParsing\Main\\reductions\\"
    file_names = os.listdir(dir)
    
    for file_path in file_names:
        with open(dir+"\\" + file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                merge_dict(merged_data, item)
    
    return merged_data



dir = "E:\PhD\OpenSource\LinguisticsParsing\Main\\signatures\\"
file_names = os.listdir(dir)
message_count = 1
signatures = []

for file in file_names:
    with open(f"{dir}\{file}", "r", encoding="utf-8") as f:
        # print("\n\n")
        signature = Signature(message_count)
        signature.load_file(f)
        signature.reduce(file)
        signature.find_words()
        signatures.append(signature)
        
        message_count += 1


total_output = {}


# for element in signatures:
#     if total_output == {}:
#         total_output = element.reduced_json
#     else:
#         new_keys




# output = [merge_json_files()]

# with open(f"total_sig.json", "w") as json_file:
#     json.dump(output, json_file, indent=4)