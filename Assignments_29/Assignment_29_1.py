#***************************************************************************************************
#                     Check File exist or not               
#***************************************************************************************************
import os
import sys

def main():
    if(len(sys.argv) != 2):
            print("File Name is not provided")
            sys.exit(1)
    filename = sys.argv[1]
    
    if(os.path.exists(filename)):
        print(f"{filename} exist")
    else:
        print(f"{filename} not exist")
if(__name__=="__main__"):
    main()