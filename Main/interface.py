import cmd
import os
from utility import run_files, analyse_file, generateGraphViz, pdf_to_text
from document import Document
from linguistic_engine import Linguistic_Engine
import nltk
import pandas as pd
from collections import defaultdict

class SignatureCLI(cmd.Cmd):
    prompt = ">> "
    intro = "Welcome to the Linguisitic Signature CLI. Type 'help' for available commands."

    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()
        self.engine = Linguistic_Engine()

    def greeting(self, line):
        print("Hello World!")
    
    def do_exit(self, line):
        return True
    
    def precmd(self, line):
        #Before execution
        print("Before command execution")
        return line #Modify line and return here
    
    def postcmd(self, stop, line):
        #After execution
        print("After command execution")
        return stop #Modify line and return here
    
    def preloop(self):
        # Add custom initialization here
        print("Initialization before the CLI loop")

    def postloop(self):
        # Add custom cleanup or finalization here
        print("Finalization after the CLI loop")

    def do_list(self, line):
        """List files and directories in the current directory."""
        files_and_dirs = os.listdir(self.current_directory + "/working_files")
        for item in files_and_dirs:
            print(item)

    def do_runAll(self, line):
        files_and_dirs = os.listdir(self.current_directory + "/working_files")
        run_files(self.current_directory+ "/working_files", files_and_dirs, "interface_output")

    def do_runIndividual(self, line):
        files_and_dirs = os.listdir(self.current_directory + "/working_files")
        #run_files(self.current_directory+ "/working_files", files_and_dirs, "output")
        file_count = 1
        for file in files_and_dirs:
            with open(f"{self.current_directory}/working_files/{file}", encoding="utf-8") as f:
                contents = f.read()
                analyse_file(contents, f"interface-output-{file_count}")
                file_count += 1

    def do_runFile(self, line):
        with open(f"{self.current_directory}/working_files/{line}", encoding="utf-8") as f:
            contents = f.read()
            analyse_file(contents, "interface_output") 

    def do_make_docs(self, line):
        files_and_dirs = os.listdir(self.current_directory + "/working_files")
        #run_files(self.current_directory+ "/working_files", files_and_dirs, "output")
        file_count = 1
        for file in files_and_dirs:
            small_name = file.split("-")[0:3]
            small_name.append(str(file_count))
            
            with open(f"{self.current_directory}/working_files/{file}", encoding="utf-8") as f:
                contents = f.read()
                if len(contents) > 100:
                    file_count += 1
                    self.engine.construct_document(contents, "-".join(small_name))    
        # self.engine.graph_engine()

    def do_list_docs(self, line):
        total_documents = self.engine.documents
        for id in total_documents:
            document = total_documents[id]
            print(id)
            print(document.total_nouns)
            # print(total_documents[id])

    def text_to_noun(self, text):
        text = text.replace("\n", " ")
        text = text.replace("\t", "")
        text = text.replace("  ", " ")
        sentences = text.split(". ")
        pairs = []
        for sentence in sentences:
            tokens = nltk.word_tokenize(sentence)
            pos_tags = nltk.pos_tag(tokens)
            noun_tags = [x for x in pos_tags if x[1][0:2] == "NN"]
            reduced_nouns = [x[0] for x in noun_tags]
            if len(reduced_nouns) > 1:
                for i in range (0, len(reduced_nouns)-1):
                    word_1 = reduced_nouns[i]
                    word_2 = reduced_nouns[i+1]
                    pairs.append([word_1, word_2])
        return pairs
            #print(reduced_nouns)

    def do_pdf_convert(self, line):
        input_file = line
        dir = "E:\Downloads\\"
        output_file = "E:\PhD\OpenSource\LinguisticsParsing\Main\\selections\\" + input_file[:-4]
        pdf_to_text(dir + input_file, output_file)

    def do_apply_signatures(self, line):
        total_documents = self.engine.documents
        total_nodes = []
        total_links = []
        old_name = ""
        total_counts = defaultdict(int)
        for id in total_documents:
            document = total_documents[id]
            document_content = document.text
            document_signature = document.total_nouns
            name = document.name
            # name = name[:-3]
            pairs = self.text_to_noun(document_content)
            found_pairs = set()
            occurance_dict = {}
            for pair in pairs:
                # print(pair)
                if pair[0] in document_signature:
                    child_items = document_signature[pair[0]]
                    if pair[1] in child_items:
                        found_pairs.add(pair[0] + " " + pair[1])
                        if pair[0] in occurance_dict:
                            occurance_dict[pair[0]] += 1
                        else:
                            occurance_dict[pair[0]] = 1
            sorted_items = sorted(occurance_dict.items(), key=lambda item: item[1], reverse=True)
            item_nodes = [x[0] for x in sorted_items]
            total_nodes = total_nodes + item_nodes
            viz_format_links = [x.split(" ") for x in found_pairs]
            total_links = total_links + viz_format_links
            document.set_graph_nodes(item_nodes)
            document.set_graph_links(viz_format_links)
            for word, count in document.noun_count.items():
                total_counts[word] += count
            counts = pd.DataFrame.from_dict(document.noun_count, orient='index')
            # print(total_counts, counts)
            # if type(total_counts) == None:
            #     total_counts = counts
            # else:    
            #     add_together = lambda s1, s2: s1+s2 if s1==s2 else max(s1,s2)
            #     total_counts.combine(counts, add_together)
            normalized = (counts/counts.sum())
            average = normalized.mean().values[0]
            weighting_dict = normalized.to_dict()[0]




            # print(document.noun_count)
            # if old_name != name:
            #     total_count  = pd.DataFrame.from_dict(total_counts, orient='index')
            #     normalized_all = (total_count/total_count.sum())
            #     average_all = normalized_all.mean().values[0]
            #     weighting_all = normalized_all.to_dict()[0]   
            #     id = 1
            #     generateGraphViz(total_nodes, total_links, f"{old_name}_total", weighting_all, average_all)
            #     total_nodes = []
            #     total_links = []
            #     old_name = name                


            # generateGraphViz(item_nodes, viz_format_links, f"{name}-{id}", weighting_dict, average)

        total_count  = pd.DataFrame.from_dict(total_counts, orient='index')
        normalized = (total_count/total_count.sum())
        average = normalized.mean().values[0]
        weighting_dict = normalized.to_dict()[0]


        # print(total_counts)
        generateGraphViz(total_nodes, total_links, f"corpus_output", weighting_dict, average)
            # document.generate_graph(f"output-{id}")
            # print(item_nodes)
            # print(viz_format_links)re
                    # print(child_items)
                # if pair[0] in document_signature and pair[1] in document_signature[pair[0]]:
                #     if pair[0] in occurance_dict:
                #         occurance_dict[pair[0]] += 1
                #     else:
                #         occurance_dict[pair[0][0]] = 1
            # print(document_content)
            # print(occurance_dict)       

    

if __name__ == '__main__':
    SignatureCLI().cmdloop()

