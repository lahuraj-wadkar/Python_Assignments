#***************************************************************************************************
#                     Print binary equivalent of a number                                     
#***************************************************************************************************

def printBinary(no1):
    binary = []
    print("Binary Equivalent of a number :", no1, "is <", end=" ")
    while(no1 > 0):
        binary.append(no1%2);
        no1 = int(no1/2)
    for i in range(len(binary), 0, -1):
        print(binary[i-1], end="")
    print()

def main():
    no1 = int(input("Enter Number :"))
    printBinary(no1)

if(__name__ == "__main__"):
    main()