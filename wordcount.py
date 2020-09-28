import sys
from os import path
filename=input("Enter the name of the file: ")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file=open(filename,"r")
while 1:
    line=file.readline() #Read next line from stdin into "line"
    print(line,end="") #Print line (end=" " skips extra linefeed)
    if line=="": #Quit while loop if line is empty
        break
    words.extend(line.split())
counts=Counter(words)
for i in counts:
    print("%2d: %s"%(counts[i],i)) 
