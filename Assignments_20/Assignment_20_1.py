#***************************************************************************************************
#                  Dispay EVen and Odd using threads                          
#***************************************************************************************************

import time
import threading

def Even(no):
    print("First 10 even nos are :")
    for i in range(2, no*2+1, 2):
        print(i, end=" ")
    print()
        

def Odd(no):
    print("First 10 odd nos are :")
    for i in range(1, no*2+1, 2):
        print(i, end=" ")
    print()

def main():
    no = 10
    tobj1 = threading.Thread(target=Even, args=(no,))
    tobj2 = threading.Thread(target=Odd, args=(no,))
    
    tobj1.start()
    tobj2.start()
    tobj1.join()
    tobj2.join()
    
if(__name__ == "__main__"):
    main()