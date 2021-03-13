import os
import re

listOfEntries=[] # currently serve no purpose
analizedFiles={}
listOfFoundFiles = []
count = 0 
sizeofdir = 0 
#This Function will look into a directory and list out all of the entries inside

def list_files(startpath,depth=1,search=None):
    maxdepth = depth
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        if level <= maxdepth:
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                read_file(root,f,search)
                print(f'{subindent}{f}')
            if level == maxdepth:
                for d in dirs:
                    print(f'{subindent}{d}')
    print(analizedFiles)
    print("Number of file is :"+str(count))
    print("The Size is "+ str(sizeofdir)+" Mb")
    if listOfFoundFiles != None:
        print(f"file is found : {len(listOfFoundFiles)} " + f" the search query is : -{search}-")
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

#organizer == {"filename":"extension" can be list / string}
analizer = {'text':['.txt']}
# for i in analizer: print(i)
def organizer(rootpath,depth=0,organizer=dict):
    for dirname in organizer:
        dirpath = os.path.join(rootpath,dirname)
        print(dirpath)
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
            print(dirname)
        else:
            print("dictionary already found")
            for root, dirs, files in os.walk(rootpath):
                level = root.replace(rootpath, '').count(os.sep)
                pass

# list_files(r"C:/Users/NABEL/OneDrive/Desktop/Testing Folder",search = "text")
organizer("C:/Users/NABEL/OneDrive/Desktop/Testing Folder",organizer=analizer)

