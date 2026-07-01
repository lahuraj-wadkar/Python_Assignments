#***************************************************************************************************
#                  Check if number is odd using lambda                                      
#***************************************************************************************************
isOdd = lambda x:(x%2!=0)

def main():
    val1 = int(input("Enter value1 :"))
    ret = isOdd(val1)
    if(ret == True):
        print("Odd Number")
    else:
        print("Even Number")

if(__name__=="__main__"):
    main()