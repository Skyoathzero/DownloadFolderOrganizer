import os
import re
import shutil

listOfEntries=[] # currently serve no purpose
analizedFiles={}
listOfFoundFiles = []
count = 0 
sizeofdir = 0 
#This Function will look into a directory and list out all of the entries inside

def list_files(startpath,depth=1,search=None):
    global count 
    global sizeofdir 
    count = 0
    sizeofdir = 0
    
    maxdepth = depth
    result = """ """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        if level <= maxdepth:
            result+=('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                read_file(root,f,search)
                result += f"{subindent}{f}\n"
            if level == maxdepth:
                for d in dirs:
                    result += f"{subindent}{f}\n"
                    
    print(analizedFiles)
    print("Number of file is :"+str(count))
    print("The Size is "+ str(sizeofdir)+" Mb")
    if listOfFoundFiles != None:
        print(f"file is found : {len(listOfFoundFiles)} " + f" the search query is : -{search}-")
        print('\n'.join(listOfFoundFiles))
    foundfiles = '\n'.join(listOfFoundFiles)
    numberfoundfiles = len(listOfFoundFiles)
    
    return result , analizedFiles , count , sizeofdir , listOfFoundFiles ,foundfiles , numberfoundfiles
    # return analizedFiles , count , 
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
    sizeofdir += round(size/mb,3)

    if searchFile != None:
        searchword = re.compile(searchFile)
        if searchword.search(file) != None :
            listOfFoundFiles.append(path)

#organizer == {"filename":"extension" must be a list}
organizerdict = {}
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
                if level <= depth:
                    for file in files:
                        filepath = os.path.join(root,file)
                        newdirpath = os.path.join(dirpath,file)
                        for ext in organizer[dirname]:
                            if ext.startswith('.'):
                                if os.path.splitext(file)[1] == ext:
                                    print('\n')
                                    print(filepath)
                                    print('Moving To Another Dir : ')
                                    shutil.move(filepath,newdirpath)
                                    print(newdirpath)
                            else: 
                                searchword = re.compile(ext)
                                print(searchword)
                                print(file)
                                if searchword.search(file) != None:
                                    print('Yes')
                                    print('\n')
                                    print(filepath)
                                    print('Moving To Another Dir : ')
                                    shutil.move(filepath,newdirpath)
                                    print(newdirpath)


def format_input(foldername,extensionlist=list):
    organizerdict[str(foldername)] = [i for i in extensionlist ]

def get_input():
    isdone = False
    extensionmode=True
    name = str(input('Put in Folder Name :'))
    list_of_extension = []
    while isdone == False:
        i = str(input('Enter the name of the extension to be organized,enter a changemode to input filename that want to be organized, enter f to finish:'))
        if i == 'f':
            isdone == True
            break
        if i == 'a' :
            extensionmode = not extensionmode
        if i != 'a': 
            if extensionmode == False:
                list_of_extension.append(i)
            if extensionmode == True:
                if i.startswith('.') == False:
                    i = '.'+i
                    list_of_extension.append(i)
                else: list_of_extension.append(i)
            
    return format_input(name,list_of_extension)

def stringToList(string):
    return string.split(',')

format_input('a',['a','b'])
print(organizerdict)
print(stringToList('a,b,.exe'))
target = r'C:/Users/NABEL/OneDrive/Desktop/Testing Folder - Copy'
# organizerinput = {'text':['text']}
# organizer(target,depth=1,organizer=organizerinput)