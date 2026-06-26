#***************************************************************************************************
#                     Find factorial  of a given Number                                       
#***************************************************************************************************

def factorial(no1):
    fact = 1
    for i in range (1, no1+1):
        fact = fact*i
    print("Factorial of :", no1, "is :", fact)

def main():
    no1 = int(input("Enter First Number :"))
    factorial(no1)

if(__name__ == "__main__"):
    main()