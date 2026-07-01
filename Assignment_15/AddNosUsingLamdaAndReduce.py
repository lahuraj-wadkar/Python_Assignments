#***************************************************************************************************
#                  Using Reduce and lambda print addition of  numbers from list                                      
#***************************************************************************************************
from functools import reduce
add = lambda x,y:(x+y)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    addition = int(reduce(add, lst))
    print("Addition of list ny=umbers  :", addition)

if(__name__=="__main__"):
    main()