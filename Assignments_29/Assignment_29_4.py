#***************************************************************************************************
#                    Compare file into another file                               
#***************************************************************************************************

import os
import sys

def main():
    if(len(sys.argv) != 3):
            print("Usage: python Assignment_29_4.py InputFile1 InputFile2")
            sys.exit(1)
    inputFile1 = sys.argv[1]
    inputFile2 = sys.argv[2]
    
    if(os.path.exists(inputFile1) and os.path.exists(inputFile2)):
        fobj = open(inputFile1, "r", encoding="utf-8")
        fobj1 = open(inputFile2, "r", encoding="utf-8")
        if(fobj.read() == fobj1.read()):
            print(f"content of {inputFile1} and {inputFile1} are equal")
        else:
             print(f"content of {inputFile1} and {inputFile1} are not equal")
    else:
         print(f"{inputFile1} and|or {inputFile2} not exist")
if(__name__=="__main__"):
    main()