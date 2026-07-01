#***************************************************************************************************
#                  Using filter and lambda print Odd numbers from list                                      
#***************************************************************************************************
isOdd = lambda x:(x%2!=0)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    lst = list(filter(isOdd, lst))
    print("After square of each number List is :", lst)

if(__name__=="__main__"):
    main()