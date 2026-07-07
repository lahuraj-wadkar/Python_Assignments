#***************************************************************************************************
#                  sum of EvenFactor and OddFactor using threads                         
#***************************************************************************************************

import time
import threading

def sumEvenFactors(no):
    sum = 0
    for i in range(1, no+1):
        if((no%i == 0) and (i%2 == 0)):
            sum = sum+i
    print(f"Sum of even factors are {sum}")

def sumOddFactors(no):
    sum = 0
    for i in range(1, no+1):
        if((no%i == 0) and (i%2 != 0)):
            sum = sum+i
    print(f"Sum of odd factors are {sum}")

def main():
    no = int(input("Enter the number :"))
    tobj1 = threading.Thread(target=sumEvenFactors, args=(no,))
    tobj2 = threading.Thread(target=sumOddFactors, args=(no,))
    
    tobj1.start()
    tobj2.start()
    tobj1.join()
    tobj2.join()
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()