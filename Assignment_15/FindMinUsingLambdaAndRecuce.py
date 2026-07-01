#***************************************************************************************************
#                  Using Reduce and lambda find maximum number from list                                      
#***************************************************************************************************
from functools import reduce
Min = lambda x,y:(x if x<y else y)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    min = int(reduce(Min, lst))
    print("Maximum number of from list  :", min)

if(__name__=="__main__"):
    main()