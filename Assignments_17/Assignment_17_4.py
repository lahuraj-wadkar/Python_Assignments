def AdditionOfFactors(no1):
    sum = 0
    for i in range(1, no1+1):
        if(no1%i == 0):
            sum += i
    print("Addition of Factors is  :", sum)
def main():
    no = int(input("Enter number :"))
    AdditionOfFactors(no)
if(__name__ == "__main__"):
    main()