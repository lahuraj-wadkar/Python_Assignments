#***************************************************************************************************
#                                        Find Cube of a Number                                         
#***************************************************************************************************

def Cube(no1):
    return no1*no1*no1
       

def main():
    no1 = int(input("Enter First Number :"))
    print("Cube of a Number <", no1, "> is :<", Cube(no1), ">")

if(__name__ == "__main__"):
    main()