import os

listOfEntries=[] # currently serve no purpose
analizedFiles={}
count = 0 
sizeofdir = 0 
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
                read_file(root,f)
                print(f'{subindent}{f}')
            if level == maxdepth:
                for d in dirs:
                    print(f'{subindent}{d}')
    print(analizedFiles)
    print(count)
    print(str(sizeofdir)+" Mb")

def read_file(root,file):
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
    
list_files(r"C:/Users/NABEL/Downloads")

