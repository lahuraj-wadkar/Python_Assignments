#***************************************************************************************************
#                  Prime and Non prime using Threads                         
#***************************************************************************************************

import time
import threading

def Prime(lst):
    pList = []
    for x in lst:
        isPrime = True
        if(x == 1):
            isPrime = False
        if(x == 2):
            pList.append(x)
        for i in range(2, int(((x/2)+1) + 1)):
            if(x%i == 0):
                isPrime = False
                break
        if isPrime == True :
            pList.append(x)
    print(f"Prime Numbers from the list are : {pList}")

def NonPrime(lst):
    pList = []
    for x in lst:
        if(x == 1 or x == 2):
            continue
        for i in range(2, int(((x/2)+1)+1)):
            if(x%i == 0):
                pList.append(x)
                break
    print(f"Non Prime Numbers from the list are : {pList}")

def main():
    lst =[]
    for i in range (10):
        lst.append(int(input("Enter the number :")))
    tobj1 = threading.Thread(target=Prime, args=(lst,))
    tobj2 = threading.Thread(target=NonPrime, args=(lst,))
    tobj2.start()
    tobj1.start()
    tobj1.join()
    tobj2.join()
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()