import os 
import sys

def main_():
    global path_n, name, decn, ftype
    path_n = str(input("Enter full file path target to bulk rename every file: ")) # Must have "/" and not "\" 
    name = input("Enter the Name: ")
    ftype = input("Enter file extention type (e.g; .txt, .png, etc)\n>> ")
    path_n = path_n.replace("\\", " / ")
    if path_n.endswith("\\"):
        path_n.endswith("/")
main_()
input("Press 'enter' to bulk rename ")

def _main():
    global path, name, decn, ftype, path_n
    

    try:
        path = path_n
    except FileNotFoundError as e:
        return
    x = 0
    current_file = os.path.basename(sys.argv[0])

   for file in os.listdir(path):
        dest = name + str(x) + ftype
        src = path + file
        dest = path + dest
        if file == current_file:
            pass
        else:
            try:
                os.rename(src, dest)
            except FileNotFoundError:
                print("Failed to rename file. File not found error")
            except FileExistsError:
                print("Failed to rename file. File name already exists \n(try renaming everything to something else and then change it back)")
            print("Successfuly renamed ", file)
        
        x += 1
    input("Press 'enter' to exit")

if __name__ == "__main__":
    _main()