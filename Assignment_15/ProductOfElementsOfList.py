#***************************************************************************************************
#                  Print product of elements of list                                      
#***************************************************************************************************
from functools import reduce
product = lambda x,y:(x*y)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    prod = int(reduce(product, lst))
    print("Product of elements of List is :", prod)

if(__name__=="__main__"):
    main()