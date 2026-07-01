#***************************************************************************************************
#                  find Min of 2 numbers using lambda                                      
#***************************************************************************************************
Min = lambda x,y:(x if x<y else y)

def main():
    val1 = int(input("Enter value1 :"))
    val2 = int(input("Enter value2 :"))
    print("Minimum number is  :", Min(val1, val2))

if(__name__=="__main__"):
    main()