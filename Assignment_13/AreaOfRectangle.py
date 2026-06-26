#***************************************************************************************************
#                     Find Area of Rectangle                                    
#***************************************************************************************************

def findArea(length, width):
    return length*width

def main():
    val1 = float(input("Enter length of rectangle :"))
    val2 = float(input("Enter width of rectangle :"))
    print("Area of a rectangle is :", findArea(val1, val2))

if(__name__ == "__main__"):
    main()