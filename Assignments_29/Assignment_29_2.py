#***************************************************************************************************
#                     Display content of file line by line                                   
#***************************************************************************************************

import os
import sys

def main():
    if(len(sys.argv) != 2):
            print("File Name is not provided")
            sys.exit(1)
    filename = sys.argv[1]
    
    if(os.path.exists(filename)):
        fobj = open(filename, "r", encoding="utf-8")
        print(fobj.read())
        fobj.close()
    else:
         print(f"{filename} not exist")
if(__name__=="__main__"):
    main()