#***************************************************************************************************
#                     Find Area of Circle                                   
#***************************************************************************************************
PI = 3.14
def findArea(radius):
    return PI*radius*radius

def main():
    val1 = float(input("Enter radius of a circle :"))
    print("Area of a Circle is :", findArea(val1))

if(__name__ == "__main__"):
    main()