#***************************************************************************************************
#                  Threads                         
#***************************************************************************************************

import time
import threading

def dispay():
    for i in range(51):
        print(i, end=" ")
    print()

def reverseDisplay():
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()

def main():
    tobj1 = threading.Thread(target=dispay)
    tobj1.start()
    tobj1.join()
    tobj2 = threading.Thread(target=reverseDisplay)
    tobj2.start()
    tobj2.join()
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()