#***************************************************************************************************
#                     Frequency a word in a file                          
#***************************************************************************************************

import os
import sys

def main():
    if(len(sys.argv) != 3):
            print("Usage: python Assignment_28_5.py <InputFile> <wordtoSearch>")
            sys.exit(1)
    inputFile = sys.argv[1]
    searchword = sys.argv[2]
    
    if(os.path.exists(inputFile)):
        fobj = open(inputFile, "r", encoding="utf-8")
        
        content = fobj.read()
        pos = content.count(searchword)
        if(pos > 0):
             print(f"{searchword} is found in file {inputFile}, Number of occurances are {pos}")
        else:
             print(f"{searchword} is not found in file {inputFile}")
    else:
         print(f"{inputFile} not exist")
if(__name__=="__main__"):
    main()