#***************************************************************************************************
#                     Find Number of digits in a given number                                      
#***************************************************************************************************

def FindNumberofDigits(no1):
    no_dig = 0
    while(no1 > 0):
        no1 = int(no1/10);
        no_dig = no_dig + 1
    return no_dig

def main():
    no1 = int(input("Enter Number :"))
    print("Number of digints in a", no1, "are :", FindNumberofDigits(no1))

if(__name__ == "__main__"):
    main()