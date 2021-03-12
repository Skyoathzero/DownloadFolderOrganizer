import os
listOfEntries=[] # currently serve no purpose
analizedFiles={}
count = 0 
#This Function will look into a directory and list out all of the entries inside

def list_files(startpath,depth=1):
    maxdepth = depth
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        if level <= maxdepth:
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                read_file(f)
                print('{}{}'.format(subindent, f))
            if level == maxdepth:
                for d in dirs:
                    print('{}{}'.format(subindent, d))
    print(analizedFiles)
    print(count)
def read_file(file):
    if not file[-4:] in analizedFiles :
        analizedFiles[file[-4:]] = 1
    elif file[-4:] in analizedFiles :
        analizedFiles[file[-4:]] +=1 
    global count 
    count += 1
    
list_files("C:/Users/NABEL/OneDrive/Documents/Test Folder")

    