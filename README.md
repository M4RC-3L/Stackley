# Stackley

A customizable tool for sorting file types into automatically generated directories. Written in Python.

### If your directories look like this ...<br>
<img src="https://github.com/M4RC-3L/Stackley/blob/master/demo/demo1.png" height="300"/><br>
### ... but could look like that.<br>
<img src="https://github.com/M4RC-3L/Stackley/blob/master/demo/demo2.png" height="300"/><br>

Stackley sorts your directories based on a list that you can edit by defining names for subdirectories and their contents.
You can sort all files by the file extension. For example, collect all images, music files, developer files or 3D models.

## Configure Stackley
Use "stackList.txt" and define your rules. This could look like this, for example:
```
photos|jpg|png|jpeg|ps|ai
developer|java|py
documents|pages|doc|docs|numbers|keynote|pdf|rtf|docx|txt
applications|app
music|mp3|wav|ceol|mp3
movies|mp4|mpv|mov
3D|mtl|obj
Web|webloc
```

## Use Stackley

Go to the directory where you downloaded Stackley and use:
`python3 stackley.py [arguments]`

Use the following commands to use Stackley's functions.<br>

- `[path1] [path2] [path...] [path4]` Stackley cleans up your directories.
- `-r [path1] [path2] [path...] [path4]` Stackley directories are deleted and their content is moved to the parent directory.
- `-d [path1] [path2] [path...] [path4]` Stackley directories are deleted with their contents.
- `-c [path1] [path2]` Stackley directories are copied from one path to another.
- `-h` For an explanation of how Stackley can be used.

## Use Stackley with tkinter GUI:

Go to the directory where you downloaded Stackley and use:
`python3 stackUI.py`

A window will magically open and show you the Stackley commands in simple button form. So you no longer have to tediously tapping but can click comfortably. :)

<img src="https://github.com/M4RC-3L/Stackley/blob/master/demo/demo3.png" height="300"/>

Click on "Configure" to open stackList.txt in your standard text editor and edit your Stackley rules.
