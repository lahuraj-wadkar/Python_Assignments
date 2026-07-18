#***************************************************************************************************
#                     Open a file and count number of lines                                
#***************************************************************************************************
import os
import sys

def main():
    if(len(sys.argv) != 2):
            print("File Name is not provided")
            sys.exit(1)
    filename = sys.argv[1]
    
    if(os.path.exists(filename)):
        fobj = open(filename, "r")
        print(f"{filename} Opened successfully")
        noLines = len(fobj.readlines())
        print(f"Number of lines in {filename} are : {noLines}")
        fobj.close();
    else:
         print(f"{filename} not exist")
if(__name__=="__main__"):
    main()