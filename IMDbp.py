from imdbpie import Imdb
import os
imdb = Imdb()
list1=[]
for file in os.listdir("./"):
    list1.append(file)
print list1
ListOfExtensions = ['avi','mp4','mkv','wmv']
from os import walk
mypath="./"
names = []
dir=[]
for (dirpath, dirnames, filenames) in walk(mypath):
    names.extend(filenames)
    dir.append(dirpath)


print names
print dir