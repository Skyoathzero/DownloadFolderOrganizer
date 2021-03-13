import os
import re

listOfEntries=[] # currently serve no purpose
analizedFiles={}
listOfFoundFiles = []
count = 0 
sizeofdir = 0 
#This Function will look into a directory and list out all of the entries inside

def list_files(startpath,depth=1,sEntry=None):
    maxdepth = depth
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        if level <= maxdepth:
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                read_file(root,f,sEntry)
                print(f'{subindent}{f}')
            if level == maxdepth:
                for d in dirs:
                    print(f'{subindent}{d}')
    print(analizedFiles)
    print("Number of file is :"+str(count))
    print("The Size is "+ str(sizeofdir)+" Mb")
    if listOfFoundFiles != None:
        print(f"file is found : {len(listOfFoundFiles)} " + f" the search query is : -{sEntry}-")
        print('\n'.join(listOfFoundFiles))

def read_file(root,file,searchFile):
    mb = 1048576
    path = os.path.join(root,file)
    size = os.path.getsize(path)
    filename , file_extension = os.path.splitext(path)
    if not file_extension in analizedFiles :
        analizedFiles[file_extension] = 1
    elif file_extension in analizedFiles :
        analizedFiles[file_extension] +=1 
    global count 
    count += 1
    global sizeofdir
    sizeofdir += round(size/mb,2)
    if searchFile != None:
        searchword = re.compile(searchFile)
        if searchword.search(file) :
            listOfFoundFiles.append(path)

    
list_files(r"C:/Users/NABEL/Downloads",sEntry = "Gen")

