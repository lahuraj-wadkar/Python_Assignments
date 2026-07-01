#***************************************************************************************************
#                  Using filter and lambda print even numbers from list                                      
#***************************************************************************************************
isEven = lambda x:(x%2==0)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    lst = list(filter(isEven, lst))
    print("After square of each number List is :", lst)

if(__name__=="__main__"):
    main()