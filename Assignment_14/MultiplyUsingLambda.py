#***************************************************************************************************
#                  Multiplication of 2 numbers using lambda                                      
#***************************************************************************************************
Mult = lambda x,y:(x*y)

def main():
    val1 = int(input("Enter value1 :"))
    val2 = int(input("Enter value2 :"))
    print("Multiplication is  :", Mult(val1, val2))

if(__name__=="__main__"):
    main()