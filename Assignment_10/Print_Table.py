#***************************************************************************************************
#                     Print a Multiplication table  of a given Number                                       
#***************************************************************************************************

def Print_Mult_Table(no1):
    print("Multiplication Table of a number", no1 ,"is as below:")
    for i in range (1, 11):
        print(i*no1)
       

def main():
    no1 = int(input("Enter First Number :"))
    Print_Mult_Table(no1)

if(__name__ == "__main__"):
    main()