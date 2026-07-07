#***************************************************************************************************
#                  Use of FMR - filter map reduce                       
#***************************************************************************************************
from functools import reduce

def Prime(x):
    if(x == 1):
        return False
    if(x == 2):
        return True
    for i in range(2, int((x/2)+1)):
        if(x%i == 0):
            return False
    return True
        
MultBy2 = lambda x : (2 * x)
Max = lambda x,y:(x if x > y else y)

def main():
    lst = []
    for i in range(10):
        lst.append(int(input("Enter number : ")))
    val = int(reduce(Max, list(map(MultBy2, list(filter(Prime, lst))))))
    print(f"Maximu number : {val}")

if (__name__ == "__main__"):
    main()