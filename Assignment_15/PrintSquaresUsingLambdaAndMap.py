#***************************************************************************************************
#                  Using map and lambda print square of each number                                      
#***************************************************************************************************
square = lambda x:(x*x)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    lst = list(map(square, lst))
    print("After square of each number List is :", lst)

if(__name__=="__main__"):
    main()