#***************************************************************************************************
#                     Find sum of first N natural numbers                                       
#***************************************************************************************************

def findSum(no1):
    sum = 0
    for i in range (1, no1+1):
        sum = sum + i
    print("Sum of first ", no1, "Natural Numbers is:", sum)

def main():
    no1 = int(input("Enter First Number :"))
    findSum(no1)

if(__name__ == "__main__"):
    main()