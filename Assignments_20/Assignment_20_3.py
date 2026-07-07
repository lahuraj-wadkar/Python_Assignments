#***************************************************************************************************
#                  sum of EvenList and OddList using threads                         
#***************************************************************************************************

import time
import threading

def sumEven(lst):
    sum = 0
    for i in lst:
        if(i%2 == 0):
            sum = sum+i
    print(f"Sum of even list members are {sum}")

def sumOdd(lst):
    sum = 0
    for i in lst:
        if(i%2 != 0):
            sum = sum+i
    print(f"Sum of odd list members are {sum}")

def main():
    lst =[]
    for i in range (10):
        lst.append(int(input("Enter the number :")))
    tobj1 = threading.Thread(target=sumEven, args=(lst,))
    tobj2 = threading.Thread(target=sumOdd, args=(lst,))
    
    tobj1.start()
    tobj2.start()
    tobj1.join()
    tobj2.join()
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()