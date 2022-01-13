from tkinter import *
import tkinter.font as tkFont
import json
import xml.dom.minidom
from tkinter.filedialog import asksaveasfile
import random, string, os
import time


window = Tk()
# application title


Font = tkFont.Font(family="Licorice", size=12)
window.title("Beautify")
# characteristics
window.geometry("550x1200")


def InstallDependancies():
    package = "pyminizip"
    try:
        import pyminizip
    except:
        os.system("pip install " + package)
        Output.insert('1.0',
                      "The package pyminizip was unable to install meaning you cannot save data into password protected files using this app.")


def welcomeMessage():
    Output.insert("1.0",
                  "Hello there!\nWelcome to the built-in XML and JSON beautifer.\nThere is no data sent across the internet, so you can use personal information without worrying about your data rights 😉")


def generate_random_file_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(16))
    return password


def Encrypt():
    contents = Output.get('1.0', END)
    new_file = asksaveasfile(title="Save file", defaultextension=".txt",
                             filetypes=(("Text files", "*.txt"),))
    if new_file:
        new_file.write(contents)
        new_file.close()
    filename = new_file.name
    # now compress and encrypt
    output = f"{filename}.zip"
    compression_level = 5
    Thepassword = generate_random_file_password()
    pyminizip.compress(filename, None, output,
                       Thepassword, compression_level)

    Output.delete('1.0', END)
    Output.insert(END, f"A compressed file has been created. \nThe password is {Thepassword}")

    # now lets delete the original unencrypted file
    if filename:
        os.remove(filename)
    else:
        pass


def Minify():
    INPUT = inputtxt.get("1.0", "end")
    if INPUT is not None:
        if INPUT.startswith('{') | INPUT.startswith('['):
            minify = json.loads(INPUT)
            newMinify = json.dumps(minify)
            Output.delete('1.0', END)
            Output.insert(END, RunAgain(newMinify))
            Output.clipboard_append(newMinify)
        elif INPUT.startswith('<'):
            Beautify1 = xml.dom.minidom.parseString(INPUT)
            NewBeautified = Beautify1.toprettyxml()
            replaceNewLines = NewBeautified.replace("\n", "")
            NoTabsTabls = replaceNewLines.replace("\t", "")
            Output.delete('1.0', END)
            Output.insert(END, RunAgain(NoTabsTabls))
            Output.clipboard_append(NoTabsTabls)
        else:
            Unformatted = INPUT.replace(" ", "")
            stripWhiteSpaceBeforeAndAfter = Unformatted.strip()
            NoNewLinesUnformatted = stripWhiteSpaceBeforeAndAfter.replace("\n", "")
            NoTabs = NoNewLinesUnformatted.replace("\t", "")
            Output.delete('1.0', END)
            Output.insert(END, RunAgain(NoTabs))


def JsonFormat():
    INPUT = inputtxt.get("1.0", "end")
    try:
        if INPUT.startswith('{') | INPUT.startswith('['):
            Beautify = json.loads(INPUT)
            NewBeautified = (json.dumps(Beautify, indent=4))
            Output.delete('1.0', END)
            Output.insert(END, RunAgain(NewBeautified))
            Output.clipboard_append(NewBeautified)
    except:
        Output.delete('1.0', END)
        Output.insert('1.0', "The Json  you have entered has syntax Errors")


def XmlFormat():
    INPUT = inputtxt.get("1.0", "end")
    try:
        if INPUT.startswith('<'):
            Beautify1 = xml.dom.minidom.parseString(INPUT)
            NewBeautified = Beautify1.toprettyxml()
            Output.delete('1.0', END)
            Output.insert(END, RunAgain(NewBeautified))
            Output.clipboard_append(NewBeautified)
    except:
        Output.delete('1.0', END)
        Output.insert('1.0', "The XML you have entered has syntax Errors")


def clean():
    if inputtxt is not None:
        inputtxt.delete('1.0', END)
    else:
        pass


def RunAgain(NewBeautified):
    return NewBeautified


def SaveToFile():
    contents = Output.get('1.0', END)
    new_file = asksaveasfile(title="Save file", defaultextension=".txt",
                             filetypes=(("Text files", "*.txt"),))
    if new_file:
        new_file.write(contents)
        new_file.close()
    Output.insert('1.0', f"Your file has been saved here:{new_file.name}")



def UpperCharacter(s):
    res = ""
    i = True
    for char in s:
        if i:
            res += char.upper()
        else:
            res += char.lower()
        i = not i
    Output.delete("1.0", END)
    Output.insert("1.0", res)


click = 0


def Dark():
    global click
    if click % 2 == 1:
        click += 1
        Json.configure(bg="White", fg="black")
        Xml.configure(bg="White", fg="black")
        Unformat.configure(bg="White", fg="black")
        SpongebobText.configure(bg="White", fg="black")
        Save.configure(bg="White", fg="black")
        Clear.configure(bg="White", fg="black")
        Encryption.configure(bg="White", fg="black")
        DarkTheme.configure(bg="White", fg="black")
        l.configure(bg="White", fg="black")
        inputtxt.configure(bg="White", fg="black")
        Output.configure(bg="White", fg="black")
        Output.delete("1.0", END)
        Output.insert("1.0", "Light theme")
    elif click % 2 == 0:
        click += 1
        Json.configure(bg="black", fg="White")
        Xml.configure(bg="black", fg="White")
        Unformat.configure(bg="black", fg="White")
        SpongebobText.configure(bg="black", fg="White")
        Save.configure(bg="black", fg="White")
        Clear.configure(bg="black", fg="White")
        Encryption.configure(bg="black", fg="White")
        DarkTheme.configure(bg="black", fg="White")
        l.configure(bg="black", fg="White")
        inputtxt.configure(bg="black", fg="White")
        Output.configure(bg="black", fg="White")
        Output.delete("1.0", END)
        Output.insert("1.0", "Dark theme")

    else:
        Output.delete("1.0", END)
        Output.insert("1.0", "Something went wrong. Please restart")




# Here we define the buttons, labels, text boxes and their respective functions which we defined above ^.
l = Label(text="Please place your JSON or XML in this top box", width=399, fg="white", background="black", )
inputtxt = Text(window, bg="black", font=Font, fg="white")
Output = Text(window, bg="black", font=Font, fg="white")

Json = Button(window, text="JSON Format", fg="white", background="black",
              command=lambda: JsonFormat())
Xml = Button(window, text="XML Format", fg="white", background="black",
             command=lambda: XmlFormat())
Unformat = Button(window, text="Minify", fg="white", background="black",
                  command=lambda: Minify())
SpongebobText = Button(window, text="Spongebob Text", fg="white", background="black",
                       command=lambda: UpperCharacter(inputtxt.get("1.0", "end")))
Save = Button(window, text="Save to file", fg="white", background="black",
              command=lambda: SaveToFile())
Clear = Button(window, text="Clear input", fg="white", background="black",
               command=lambda: clean())
Encryption = Button(window, text="Password protect data", fg="white", background="black",
                    command=lambda: Encrypt())
DarkTheme = Button(window, text="Change theme", fg="white", background="black",
                   command=lambda: Dark())

InstallDependancies()
welcomeMessage()
# -- It matters the order which we initialise these functions, as buttons will spawn in that order. -- #
# initialise the label
l.pack()
# initalise text input
inputtxt.pack(expand=True, fill=BOTH)
# initialise buttons
Clear.pack(fill=X)
Json.pack(fill=X)
Xml.pack(fill=X)
SpongebobText.pack(fill=X)
Unformat.pack(fill=X)
Encryption.pack(fill=X)
DarkTheme.pack(fill=X)
# initialise the output
Output.pack(expand=True, fill=BOTH)
# initisalise the save output at the bottom of the page
Save.pack(fill=X)

# loop the program (keep app open)
window.mainloop()
