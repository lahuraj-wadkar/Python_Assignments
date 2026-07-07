#***************************************************************************************************
#                  Find Min of  lst members                        
#***************************************************************************************************
import MarvellousNum

def ListPrime(lst):
    sum = 0
    for x in lst:
        ret = MarvellousNum.chkPrime(x)
        if(ret == True):
            sum += x
    print(f"Addition of prime numebrs form list is {sum}")


def main():
    lst = []
    no = int(input("Enter Input numbers :"))
    for i in range(no):
        lst.append(int(input("Enter number:")))
    ListPrime(lst)


if(__name__ == "__main__"):
    main()