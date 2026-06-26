#***************************************************************************************************
#                     Find sum of digits in a given number                                      
#***************************************************************************************************

def FindSumofDigits(no1):
    sum = 0
    while(no1 > 0):
        dig = no1%10
        no1 = int(no1/10);
        sum = sum + dig
    return sum

def main():
    no1 = int(input("Enter Number :"))
    print("Sum of digints in a", no1, "are :", FindSumofDigits(no1))

if(__name__ == "__main__"):
    main()