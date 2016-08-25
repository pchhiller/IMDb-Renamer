from imdbpie import Imdb
import os
imdb = Imdb()
list1=[]
for file in os.listdir("./"):
    list1.append(file)
print list1
ListOfExtensions = ['avi','mp4','mkv','wmv']
def checkMovie(name):
    flag=0
    for ext in ListOfExtensions:
        if ext in name:
            flag=1
            break
    return flag
def replaceUseless(name):
    list2=['brrip','dvdrip','xvid','hdrip','x264','ac3','h264']
    print "name to test " + name
    for i in range(0,len(name)):

        if((name[i]=='1' and name[i+1]=='9' and name[i+2].isdigit and name[i+3].isdigit) or (name[i]=='2' and name[i+1]=='0' and name[i+2].isdigit and name[i+3].isdigit)):
            name=name[:i+4]
            return name
from os import walk
mypath="./"
names = []
dir=[]
for (dirpath, dirnames, filenames) in walk(mypath):
    names.append(filenames)
    dir.append(dirpath)
#names contains a list of list of files in a folder
#dir contains a list of directories

print names
print dir
for i in range (0,len(names)):
    for file in names[i]:
        if checkMovie(file)==1:
            Title= file[:-4]
            Title=Title.replace("."," ")
            Title=Title.lower()
            Title=replaceUseless(Title)
            try:
                print "Searching for <"+ Title + "> on IMDb"
                print imdb.search_for_title(Title)
            except:
                j=0
