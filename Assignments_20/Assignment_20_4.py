#***************************************************************************************************
#                  Three Threads - small Capital and Digits                      
#***************************************************************************************************

import time
import threading

def smallLetters(s1):
    print(f"Threade name = {threading.current_thread().name} Thread id  = {threading.get_ident()}")
    scount = 0
    for char in s1:
        if(char >= 'a' and char <= 'z'):
            scount = scount + 1
    print(f"Number of small letters in {s1} are {scount}")


def capitalLettrs(str):
    print(f"Threade name = {threading.current_thread().name} Thread id  = {threading.get_ident()}")
    ccount = 0
    for char in str:
        if(char >= 'A' and char <= 'Z'):
            ccount = ccount + 1
    print(f"Number of capital letters in {str} are {ccount}")

def digits(s1):
    print(f"Threade name = {threading.current_thread().name} Thread id  = {threading.get_ident()}")
    dcount = 0
    for char in s1:
        if(char >= '0' and char <= '9'):
            dcount = dcount + 1
    print(f"Number of digits in {s1} are {dcount}")

def main():
    s1 = input("Enter string :")
    tobj1 = threading.Thread(target=smallLetters, args=(s1,), name="SmallLetterThread")
    tobj2 = threading.Thread(target=capitalLettrs, args=(s1,), name="CapitalLetterThread")
    tobj3 = threading.Thread(target=digits, args=(s1,), name = "DigitThread")
    
    tobj1.start()
    tobj2.start()
    tobj3.start()
    tobj1.join()
    tobj2.join()
    tobj3.join()
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()