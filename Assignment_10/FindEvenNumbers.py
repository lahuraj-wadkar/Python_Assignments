#***************************************************************************************************
#                     Find even numbers till given number                                       
#***************************************************************************************************

def FindAllEven(no1):
    print("All even numbers till :", no1, "are below :")
    for i in range (2, no1+1, 2):
        print(i, end=" ")

def main():
    no1 = int(input("Enter First Number :"))
    FindAllEven(no1)

if(__name__ == "__main__"):
    main()