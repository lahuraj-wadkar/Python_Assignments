#***************************************************************************************************
#                     Find odd numbers till given number                                       
#***************************************************************************************************

def FindAllOdd(no1):
    print("All odd numbers till :", no1, "are below :")
    for i in range (1, no1+1, 2):
        print(i, end=" ")

def main():
    no1 = int(input("Enter First Number :"))
    FindAllOdd(no1)

if(__name__ == "__main__"):
    main()