#!/usr/bin/python
import os, shutil, sys

'''UI integration'''
def setArgvAndRun(arguments):
    '''Launches Stackly with Arguments given by StackUI'''
    sys.argv.clear()
    sys.argv.append("placeholder")

    for argument in arguments:
        sys.argv.append(argument)

    main()
    sys.argv.clear()

'''stackley functions'''
def run(ext, path):
    '''Creates Stackley directories.'''
    dirName = ext[0]
    del ext[0]
    fPath = path + "/" + "[" + dirName + "]" 
    ifile = [s for s in os.listdir(path) if any(s.lower().endswith(extType) for extType in ext)]
    for f in ifile:
        if not os.path.exists(fPath):
            os.makedirs(fPath)
        o = path + "/" + f
        n = fPath + "/" + f
        rename(o, n, f, fPath, False)

def remove(path, delete):
    '''Removes Stackley directories and adds their content to the parent directory or clears the content if specified.'''
    dirs = os.listdir(path)
    stackDirs = [s for s in dirs if s.lower().endswith("]") and s.lower().startswith("[")]
    for stacks in stackDirs:
        stackPath = path + "/" + stacks
        if delete == True and os.path.exists(path):
            shutil.rmtree(stackPath)
        else:
            files = os.listdir(stackPath)
            for f in files:
                o = stackPath + "/" + f
                n = path + "/" + f
                rename(o, n, f, path, False)
        if(os.path.exists(stackPath)):
            os.rmdir(stackPath)

def rename(o, n, f, fPath, toCopy):
    '''Shifts a file by renaming.'''
    copyStr = "_copy"
    while os.path.exists(n):
        fileData = f.rsplit('.', 1)
        ext = ''
        if len(fileData) >= 2:
            ext = '.' + fileData[1]
            f = fileData[0] + copyStr + ext
        copyStr = copyStr + "_copy"
        n = fPath + "/" + f
    if (toCopy):
        if (os.path.isdir(o)):
            shutil.copytree(o, n)
        else:
            shutil.copy2(o, n)
    else:
        os.rename(o, n)

def copy(oPath, nPath):
    '''Copies Stackley directories with their content to another directory.'''
    dirs = os.listdir(oPath)
    stackDirs = [s for s in dirs if s.lower().endswith("]") and s.lower().startswith("[")]
    for stacks in stackDirs:
        oStackPath = oPath + "/" + stacks
        nStackPath = nPath + "/" + stacks
        if (os.path.exists(nStackPath)):
            files = os.listdir(oStackPath)
            for file in files:
                rename(oStackPath + "/" + file , nStackPath + "/" + file, file, nStackPath, True)
        else:
            shutil.copytree(oStackPath, nStackPath)

def main():
    #Reads list for directory name and contents from lists.txt!
    ext = list()
    with open("stackList.txt") as listfile:
        lines = listfile.read().splitlines()
        for typeList in lines:
            liste = typeList.split("|")
            ext.append(liste)


    #Checks command line arguments!
    removeStacks = False
    deleteStacks = False
    copyANDpaste = False

    paths = []

    if len(sys.argv) > 1:
        try:
            if sys.argv[1] == '-h':
                #help
                print("How to use Stackley:\n\n- Configure: Change the behavior of Stackley by changing the list.\nStick to this notation so Stackley works without problems: directory_name|extention1|extention2|...|extention10\n\n- Add paths: Add paths Stackley should use.\n- Clear paths: Reset the list of paths Stackley should use.\n\n- RUN: sort all paths as configured.\n- COPY: Copy all Stackley directories from path1 to path2\n- REMOVE: Remove remote Stackley directories, but keep their contents in the parent directory.\n- DELETE: Remove remote Stackley directories and their contents.")
            elif sys.argv[1] == '-r':
                #remove
                removeStacks = True 
            elif sys.argv[1] == '-d':
                #delete
                deleteStacks = True
            elif sys.argv[1] == '-c':
                #copyANDpaste
                copyANDpaste = True
                paths.append(sys.argv[2])
                paths.append(sys.argv[3])
            else:
                paths.clear()
                paths.append("placeholder")
                paths.append(sys.argv[1])

            if len(sys.argv) > 2 and not copyANDpaste:
                paths.clear()
                if removeStacks or deleteStacks:
                    sys.argv[:0] + sys.argv[1:]
                    sys.argv.pop(0)
                for arg in sys.argv:
                    if not any(arg in a for a in paths):
                        paths.append(arg)
        except:
            print("Warning! Please check your arguments")
            removeStacks = False
            deleteStacks = False
            copyANDpaste = False

    if (copyANDpaste and len(sys.argv) >= 2):
        copy(paths[0], paths[1])
    elif (copyANDpaste):
        print("You need two directories to use copy")
    else:
        paths = paths[1:]
        for currentPath in paths:
            if os.path.exists(currentPath):
                if removeStacks:
                    print("Remove Stackley directories in: " + currentPath + " with Stackly!")
                    remove(currentPath, False)
                elif deleteStacks:
                    print("Delete Stackley directories in: " + currentPath + " with Stackly!")
                    remove(currentPath, True)
                else:
                    print("Clean up: " + currentPath + " with Stackly!")
                    for currExt in ext:
                        run(currExt, currentPath)
            else: print("Path: " + currentPath + " does not exist")

if __name__ == "__main__":
    main()