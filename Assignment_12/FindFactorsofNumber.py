#***************************************************************************************************
#                     Find a all factors of a number                                       
#***************************************************************************************************

def findFactors(no1):
    print("Factors of a number", no1, "are :", end = " ")
    for i in range (1, no1+1):
        if(no1%i == 0):
            print(i, end=" ")
    print()

def main():
    no1 = int(input("Enter Number :"))
    findFactors(no1)

if(__name__ == "__main__"):
    main()