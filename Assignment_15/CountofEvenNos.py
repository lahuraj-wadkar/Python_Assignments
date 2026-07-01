#***************************************************************************************************
#                  Find count of Even numbers from list                                      
#***************************************************************************************************
from functools import reduce
isEven = lambda x:(x%2==0)

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    lst = list(filter(isEven, lst))
    print("Total count of even numbers from list :", len(lst))

if(__name__=="__main__"):
    main()