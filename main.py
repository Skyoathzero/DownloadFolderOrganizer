import os
listOfEntries=[] # currently serve no purpose
no = 0
#This Function will look into a directory and list out all of the entries inside

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        print(root)
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

        
list_files("C:/Users/NABEL/OneDrive/Documents/Test Folder")
    