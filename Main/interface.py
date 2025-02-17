import cmd
import os
from utility import run_files, analyse_file
from document import Document
from linguistic_engine import Linguistic_Engine

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
        self.engine.graph_engine()

    

if __name__ == '__main__':
    SignatureCLI().cmdloop()

