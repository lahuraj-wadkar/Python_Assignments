#***************************************************************************************************
#                  Use of FMR - filter map reduce                       
#***************************************************************************************************
from functools import reduce

Even=lambda x:(x%2 == 0)
Square = lambda x : (x * x)
Addition = lambda x,y:(x + y)

def main():
    lst = []
    for i in range(10):
        lst.append(int(input("Enter number : ")))
    prod = int(reduce(Addition, list(map(Square, list(filter(Even, lst))))))
    print(f"Addition od list elements after operations are : {prod}")

if (__name__ == "__main__"):
    main()