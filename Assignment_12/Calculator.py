#***************************************************************************************************
#                     Addition, Subtraction, Multiplication, Division                                      
#***************************************************************************************************
def Calculate(no1, no2):
    def Addition(no1, no2):
        return no1+no2

    def Subtraction(no1, no2):
        return no1-no2

    def Multiplication(no1, no2):
        return no1*no2

    def Division(no1, no2):
        return no1/no2
    
    print("Addition of :",no1,"and", no2,"is :", Addition(no1, no2))
    print("Subtraction of :",no1, "and", no2,"is :", Subtraction(no1, no2))
    print("Multiplication of :",no1, "and", no2,"is :", Multiplication(no1, no2))
    print("Division of :",no1, "and", no2,"is :", Division(no1, no2))

def main():
    no1 = int(input("Enter first Number :"))
    no2 = int(input("Enter second Number :"))
    Calculate(no1, no2)

if(__name__ == "__main__"):
    main()