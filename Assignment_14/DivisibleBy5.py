#***************************************************************************************************
#                  Check if number is divisible by 5                                      
#***************************************************************************************************
isDivBy5 = lambda x:(x%5==0)

def main():
    val1 = int(input("Enter value1 :"))
    ret = isDivBy5(val1)
    if(ret == True):
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")

if(__name__=="__main__"):
    main()