from tkinter import *
import json

DATA_FILE = "data.json"

def loadArray(fileName):
    try:
        with open(fileName, "r") as file:
            return(json.loads(file.read()))
    except:
        return []
    
def saveArray(fileName, array):
    with open(fileName, "w") as file:
        file.write(json.dumps(array))

def checkClipboard():
    storedArray = loadArray(DATA_FILE)
    clipboardText = root.clipboard_get()
    if clipboardText not in storedArray:
        storedArray.append(clipboardText)
        saveArray(DATA_FILE, storedArray)
        print(clipboardText)
    root.after(1000, checkClipboard)

bgColor = "#191919"

root = Tk()

root.title("Clipboard")
root.minsize(300, 500)
root.resizable(True, True)
root.config(bg=bgColor)

checkClipboard()

Label(root, text="Your clipboard", bg=bgColor, fg="White").grid(row=0, column=0)

root.mainloop()