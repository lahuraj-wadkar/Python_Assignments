#***************************************************************************************************
#                  Addition of 2 numbers using lambda                                      
#***************************************************************************************************
Addition = lambda x,y:(x+y)

def main():
    val1 = int(input("Enter value1 :"))
    val2 = int(input("Enter value2 :"))
    print("Addition  :", Addition(val1, val2))

if(__name__=="__main__"):
    main()