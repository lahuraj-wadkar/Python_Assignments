#***************************************************************************************************
#                  Find Largest of 3 numbers using lambda                                      
#***************************************************************************************************
Max = lambda x,y,z:(x if(x>y and x>z) else(y if y>z else z))

def main():
    val1 = int(input("Enter value1 :"))
    val2 = int(input("Enter value2 :"))
    val3 = int(input("Enter value3 :"))
    print("Maximum is  :", Max(val1, val2, val3))

if(__name__=="__main__"):
    main()