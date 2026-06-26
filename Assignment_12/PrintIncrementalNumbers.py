#***************************************************************************************************
#                     Find a all numbers from 1 to givem number                                       
#***************************************************************************************************

def findAllNumbers(no1):
    for i in range (1, no1+1):
        print(i, end=" ")
    print()

def main():
    no1 = int(input("Enter Number :"))
    findAllNumbers(no1)

if(__name__ == "__main__"):
    main()