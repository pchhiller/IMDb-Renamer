# TMW
from imdbpie import Imdb
import os
imdb = Imdb()
#List to help determine movie files
ListOfExtensions = ['avi','mp4','mkv','wmv']
#Function to check if extension of the file belongs to ListOfExtensions
def checkMovie(name):
    flag=0
    for ext in ListOfExtensions:
        if ext in name:
            flag=1
            break
    return flag

#Replaces common keywords from list2 with nothing. Also deletes the name after the Year. eg. if name is '5 days of war 2011 dvdrip ac3 xvid-ep1c' , it returns to '5 days of war 2011'
def replaceUseless(name):
    list2=['brrip','dvdrip','xvid','hdrip','x264','ac3','h264']
    print "Name to test :" + name
    for remove in list2:
        if remove in name:
            name = name.replace(remove," ")
    for i in range(0,len(name)):
        if((name[i]=='1' and name[i+1]=='9' and name[i+2].isdigit and name[i+3].isdigit) or (name[i]=='2' and name[i+1]=='0' and name[i+2].isdigit and name[i+3].isdigit)):
            name=name[:i+4]
            break

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
            Title=Title.replace("["," ")
            Title=Title.lower()
            Title=replaceUseless(Title)
            try:
                print "Searching for <"+ Title + "> on IMDb"
                print imdb.search_for_title(Title)
            except:
                j=0
