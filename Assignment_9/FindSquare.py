#***************************************************************************************************
#                                        Find Square of a Number                                         
#***************************************************************************************************

def Square(no1):
    return no1*no1
       

def main():
    no1 = int(input("Enter First Number :"))
    print("Square of a Number <", no1, "> is :<", Square(no1), ">")

if(__name__ == "__main__"):
    main()