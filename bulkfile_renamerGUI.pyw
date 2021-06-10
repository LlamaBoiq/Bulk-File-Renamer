from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os 
import sys

msg_Pop = True

def Compile():
    global app, path_n, name, decn, ftype
    global path_ns, ftypes, names
    
    path_n = path_ns.get()
    name = names.get()       # Gets all the data and assigns them to the variable
    ftype = ftypes.get()

def Application():
    global app, path_n, name, decn, ftype, rnamebtn
    global path_ns, names, ftypes
    app = Tk()

    app.title("Bulk File Renamer")
    app.geometry("600x500")
    app.maxsize(height="500", width="600")    # Window Config
    app.minsize(height="500", width="600")

    path_ns = StringVar()
    names = StringVar()
    ftypes = StringVar()

    label = ttk.Label(app, text="Enter folder path", font = ("Arial", 15)).pack()
    tip = ttk.Label(app, text="You can enter 'this' to automatically get the current folder directory of this python script", font= ("Arial", 8)).pack()
    DirEntry = Entry(app,width=60, textvariable=path_ns).pack()

    space = ttk.Label(app, text=" ", font = ("Arial", 15)).pack() # space them out

    label2 = ttk.Label(app, text="Enter name of each file", font = ("Arial", 15)).pack()
    name_entered = Entry(app, textvariable=names).pack()

    space2 = ttk.Label(app, text=" ", font=("Arial", 15)).pack() # space them out
    
    label3 = ttk.Label(app, text="Enter file extension type (.png, .txt, etc)", font = ("Arial", 15)).pack()
    ftype_entered = Entry(app, width=5, textvariable=ftypes).pack()
    
    rnamebtn = Button(text="Rename", height="2", width="15",command=Rename).place(x=230, y=438)
    label4 = ttk.Label(app, text="Toggle whether you get a message for each file", font = ("Arial", 8)).place(x=360, y= 420)
    enablebtn = Button(text="Enabled", height="2", width="15",command=btn2).place(x=450, y=438)
    
    app.mainloop()

def Error(Title="Error", Message=None):
    messagebox.showerror(Title, Message)

def warning(Title="Warning", Message=None):
    messagebox.showwarning(Title, Message)

def successful(Title="Successful", Message=None):
    messagebox.showinfo(Title, Message)


def btn2():
    global msg_Pop
    if msg_Pop == False:
        msg_Pop = True
        setbtn2("Enabled")
    else:
        msg_Pop = False
        setbtn2("Disabled")

def setbtn2(text_=None):
    global msg_Pop
    enablebtn = Button(text=text_, height="2", width="15",command=btn2).place(x=450, y=438)

def setButton(state_=NORMAL):
    global rnamebtn
    rnamebtn = Button(text="Rename", height="2", width="15",command=Rename, state=state_).place(x=230, y=438)

def main():
    global app, path_n, name, decn, ftype, rnamebtn

    if path_n == "this":
        path_n = os.path.dirname(__file__)

    if ftype.startswith('.') == False:

        warning(Message="The file extension must start with a '.' in order for it to a valid file type")
        # { # Makes sure the path syntax is correct
    path_n = path_n.replace("\\", "/")
    if path_n.endswith("/") == False:
        path_n = path_n + "/"
        # }
    path = path_n
    x = 0
    current_file = os.path.basename(sys.argv[0]) # Refering to this current python file
  # { Loops through the given path
    try: 
        for file in os.listdir(path):
            dest = name + str(x) + ftype # Name for each file
            src = path + file
            dest = path + dest
            if len(path_n) <= 1:
                Error(Message="Paramaters for folder path is too short")
                setButton()
                return
            if file == current_file:  # Checks if the file is this this python program
                pass
            else:
                try:
                    os.rename(src, dest) # Renames each file
                except FileNotFoundError:
                    Error("File not found", "File wasnt found\n")
                    setButton()
                    return
                except FileExistsError:     # Happens when the files 
                    Error("File error", "File already exists\n" + dest)
                if msg_Pop == True:
                    successful(Message="Successfuly renamed " + file + " --> " + dest)  # Comment out if you dont want a window popping up for every file that is renamed
                
            x += 1 # For numbering each file      
            # }
    except FileNotFoundError:
        Error("Folder Directory Error", "Folder directory wasnt found\n")
        setButton()
        return
    except PermissionError:
        Error("Missing Permissions Error", "This python script doesnt have required permissions to make changes")     # Error handling when getting the system files
        setButton()
        return
    except MemoryError:
        Error("Missing Memory Error", "Insufficent memory allocated to bulk rename these files")
        setButton()
        return

    successful(Message="Successfully renamed all the files in " + path_n)
    setButton()
def Rename():
    setButton(DISABLED)
    Compile()
    main()

if __name__ == "__main__": 
    Application()