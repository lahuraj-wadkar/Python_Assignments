#***************************************************************************************************
#                  Using Reduce and lambda find maximum number from list                                      
#***************************************************************************************************
from functools import reduce
Max = lambda x,y:(x if x>y else y)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    max = int(reduce(Max, lst))
    print("Maximum number of from list  :", max)

if(__name__=="__main__"):
    main()