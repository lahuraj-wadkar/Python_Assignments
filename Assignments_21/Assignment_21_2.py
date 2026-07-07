#***************************************************************************************************
#                  Find minimum and maximum from list using Threads                         
#***************************************************************************************************

import time
import threading

def finMin(lst):
    min = lst[0]
    for i in range(1, len(lst)):
        if(min > lst[i]):
            min = lst[i]
    print(f"Minimum Element from list is  : {min}")

def finMax(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if(max < lst[i]):
            max = lst[i]
    print(f"Maximum Element from list is  : {max}")

def main():
    lst =[]
    for i in range (10):
        lst.append(int(input("Enter the number :")))
    tobj1 = threading.Thread(target=finMin, args=(lst,))
    tobj2 = threading.Thread(target=finMax, args=(lst,))
    tobj2.start()
    tobj1.start()
    tobj1.join()
    tobj2.join()
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()