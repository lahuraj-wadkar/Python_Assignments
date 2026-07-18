#***************************************************************************************************
#                     Copy one file into another file                               
#***************************************************************************************************

import os
import sys

def main():
    if(len(sys.argv) != 3):
            print("Usage: python Assignment_29_3.py InputFile OutputFile")
            sys.exit(1)
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    
    if(os.path.exists(inputFile)):
        fobj = open(inputFile, "r", encoding="utf-8")
        fobj1 = open(outputFile, "w", encoding="utf-8")
        # for line in fobj.readlines():
        #     fobj1.write(line)
        fobj1.write(fobj.read())
        fobj.close()
        fobj1.close()
        print(f"content of {inputFile} copied in {outputFile}")
    else:
         print(f"{inputFile} not exist")
if(__name__=="__main__"):
    main()