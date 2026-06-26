#***************************************************************************************************
#                     Find a number is prime or not                                       
#***************************************************************************************************

def isPrime(no1):
    if(no1 == 1):
        return "is Not a Prime Number."
    if(no1 == 2):
        return "is Prime Number."
    for i in range (2, int(no1/2)+1):
        if(no1%i == 0):
            return "is Not a Prime Number."
    return "is Prime Number."

def main():
    no1 = int(input("Enter Number :"))
    print("Given number", no1, isPrime(no1))

if(__name__ == "__main__"):
    main()