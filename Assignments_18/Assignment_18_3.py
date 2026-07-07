#***************************************************************************************************
#                  Find Min of  lst members                        
#***************************************************************************************************


def Minimum(lst):
    min = lst[0]
    for i in range(1, len(lst)):
        if(min > lst[i]):
            min = lst[i]
    print(f"Minimum from {lst} is {min}")


def main():
    lst = []
    no = int(input("Enter Input numbers :"))
    for i in range(no):
        lst.append(int(input("Enter number:")))
    Minimum(lst)


if(__name__ == "__main__"):
    main()