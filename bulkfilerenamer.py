import os 
import sys


def main_():
    global path_n, name, decn, ftype
    path_n = str(input("Enter full folder path target to bulk rename every file: ")) # Must have "/" and not "\" 
    name = input("Enter the Name: ")
    ftype = input("Enter file extention type (e.g; .txt, .png, etc)\n>> ")
    if ftype.startswith('.') == False:
        print("File exention type must start with a '.' in order to work")
        # { # Makes sure the path syntax is correct
    path_n = path_n.replace("\\", " / ")
    if path_n.endswith("\\"):   
        path_n.endswith("/")
        # }
main_()
input("Press 'enter' to bulk rename ")

def _main():
    global path, name, decn, ftype, path_n
    
    path = path_n
    x = 0
    current_file = os.path.basename(sys.argv[0]) # Refering to this current python file
  # { Loops through the given path
    for file in os.listdir(path):
        dest = name + str(x) + ftype # Name for each file
        src = path + file
        dest = path + dest
        if file == current_file: # Checks if the file is this this python program
            pass
        else:
            try:
                os.rename(src, dest) # Renames each file
            except FileNotFoundError:
                print("Failed to rename file. File not found error")
            except FileExistsError:     # Happens when the files 
                print("error")
            print("Successfuly renamed ", file, " --> ", dest)
        
        x += 1 # For numbering each file
        # }
    input("Press 'enter' to exit")

if __name__ == "__main__": 
    _main() 
