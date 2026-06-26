#***************************************************************************************************
#                     Find reverse of a given number                                      
#***************************************************************************************************

def FindReverse(no1):
    rev = ""
    if(no1 == 0):
        return "0"
    while(no1 > 0):
        dig = no1%10
        no1 = int(no1/10);
        rev = rev + str(dig)
    return rev

def main():
    no1 = int(input("Enter Number :"))
    print("Reverse of a Number :", no1, "is :", FindReverse(no1))

if(__name__ == "__main__"):
    main()