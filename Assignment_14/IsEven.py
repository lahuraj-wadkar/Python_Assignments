#***************************************************************************************************
#                  Check if number is even using lambda                                      
#***************************************************************************************************
isEven = lambda x:(x%2==0)

def main():
    val1 = int(input("Enter value1 :"))
    ret = isEven(val1)
    if(ret == True):
        print("Even Number")
    else:
        print("Odd Number")

if(__name__=="__main__"):
    main()