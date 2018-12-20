#!/usr/bin/python

from tkinter import ttk, filedialog, Button, Frame, Label, W, Tk

import os, subprocess
import webbrowser as browser

import stackley

window = Tk()
window.title("Stackley")

window.configure(background = '#3E4149')

about = False
paths = []
arguments = []

def openStackList():
    '''Open File'''
    subprocess.call(["open", "stackList.txt"])

def git():
    '''Open repository in the standard browser'''
    browser.open('https://github.com/M4RC-3L/Stackley')

def addPath():
    '''Use a filechooser to add a path'''
    directory_selected = filedialog.askdirectory()
    global paths
    paths.append(directory_selected)

    paths_text = ""

    for path in paths:
        paths_text += "\n" + path

    label_paths.config(text = paths_text)

def clearPaths():
    '''Clear paths used with Stackley'''
    global paths
    paths.clear()
    label_paths.config(text = "Paths cleared")

def toggleAboutHelp():
    '''Toggle the textfield for instructions'''
    global textHelp
    global textAbout
    global label_text
    global button_aboutHelp
    global about
    status = about
    if (status == False):
        label_text.config(text = textAbout)
        button_aboutHelp.config(text = "Help")
        about = True
    else:
        label_text.config(text = textHelp)
        button_aboutHelp.config(text = "About")
        about = False

def startStackley(argument):
    '''Start Stackley'''
    global arguments
    arguments.clear()
    
    if argument != 'placeholder1':
        arguments.append(argument)
    arguments = arguments + paths
    stackley.setArgvAndRun(arguments)
    argument = ""
    arguments.clear()

stackley

'''top UI elements'''
label_paths = Label(window, padx = 20, pady = 20,  background = "#3E4149", foreground = "#FF0DFF", justify = 'left', text = "Choose Paths to use with Stackley!")
label_paths.grid(row = 0, column = 0, sticky = W)
    
frame_buttons1 = Frame(window, bg='#3E4149')
frame_buttons1.grid(row=1, column=0)

button_configure = Button(frame_buttons1, text = "Configure", highlightbackground='#3E4149', command = openStackList, height = 1, width = 10)
button_configure.grid(row = 1, column = 0)

button_addPath = Button(frame_buttons1, text = "Add path", highlightbackground='#3E4149', command = addPath, height = 1, width = 10)
button_addPath.grid(row = 1, column = 1)

button_clearPaths= Button(frame_buttons1, text = "Clear paths", highlightbackground='#3E4149', command = clearPaths, height = 1, width = 10)
button_clearPaths.grid(row = 1, column = 2)

frame_buttons2 = Frame(window, bg='#3E4149')
frame_buttons2.grid(row=2, column=0)

button_aboutHelp= Button(frame_buttons2, text = "About", highlightbackground='#3E4149', command = toggleAboutHelp, height = 1, width = 10)
button_aboutHelp.grid(row = 1, column = 3)

button_goto= Button(frame_buttons2, text = "GitHub", highlightbackground='#3E4149', command = git, height = 1, width = 10)
button_goto.grid(row = 1, column = 4)

'''bottom UI elements'''
textHelp = "How to use Stackley correctly:\n\n- Configure: Change the behavior of Stackley by changing the list.\nStick to this notation so Stackley works without problems: directory_name|extention1|extention2|...|extention10\n\n- Add paths: Add paths Stackley should use.\n- Clear paths: Reset the list of paths Stackley should use.\n\n- RUN: sort all paths as configured.\n- COPY: Copy all Stackley directories from path1 to path2\n- REMOVE: Remove remote Stackley directories, but keep their contents in the parent directory.\n- DELETE: Remove remote Stackley directories and their contents."
textAbout = "Stackley\n\nLanguage: Python 3.7.0\nVersion: 1 2018\nDeveloper: M4RC-3L\n\n\n\nStackUI\n\nLanguage: Python 3.7.0\nUI-Libary: tkinter\nVersion: 1 2018\nDeveloper: M4RC-3L"

label_text = Label(window, padx = 20, pady = 20,  background = "#3E4149", foreground = "#4F74F1", justify = 'left', text = textHelp)
label_text.grid(row = 3, column = 0, sticky = W)

frame_buttons3 = Frame(window, bg='#3E4149')
frame_buttons3.grid(row=4, column=0)

button_run = Button(frame_buttons3, text = "RUN", highlightbackground='#3E4149', command = lambda:startStackley('placeholder1'), height = 1, width = 10)
button_run.grid(row = 0, column = 0)

button_copy = Button(frame_buttons3, text = "COPY", highlightbackground='#3E4149', command = lambda:startStackley('-c'), height = 1, width = 10)
button_copy.grid(row = 0, column = 1)

button_remove = Button(frame_buttons3, text = "REMOVE", highlightbackground='#3E4149', command = lambda:startStackley('-r'), height = 1, width = 10)
button_remove.grid(row = 0, column = 2)

button_delete = Button(frame_buttons3, text = "DELETE", highlightbackground='#3E4149', command = lambda:startStackley('-d'), height = 1, width = 10)
button_delete.grid(row = 0, column = 3)

window.mainloop()
