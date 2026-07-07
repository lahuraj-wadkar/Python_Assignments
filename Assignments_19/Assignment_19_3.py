#***************************************************************************************************
#                  Use of FMR - filter map reduce                       
#***************************************************************************************************
from functools import reduce

greaterThan70=lambda x:(x >= 70)
increaseBy10 = lambda x : (x + 10)
product = lambda x,y:(x*y)

def main():
    lst = []
    for i in range(10):
        lst.append(int(input("Enter number : ")))
    prod = int(reduce(product, list(map(increaseBy10, list(filter(greaterThan70, lst))))))
    print(f"Product od list elements after operations are : {prod}")

if (__name__ == "__main__"):
    main()