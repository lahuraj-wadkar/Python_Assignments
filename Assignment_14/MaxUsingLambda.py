#***************************************************************************************************
#                  find Max of 2 numbers using lambda                                      
#***************************************************************************************************
Max = lambda x,y:(x if x>y else y)

def main():
    val1 = int(input("Enter value1 :"))
    val2 = int(input("Enter value2 :"))
    print("Maximum number is  :", Max(val1, val2))

if(__name__=="__main__"):
    main()