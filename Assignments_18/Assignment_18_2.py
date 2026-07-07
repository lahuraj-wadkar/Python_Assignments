#***************************************************************************************************
#                  Find Max of  lst members                        
#***************************************************************************************************


def Maximum(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if(max < lst[i]):
            max = lst[i]
    print(f"Maximum from {lst} is {max}")


def main():
    lst = []
    no = int(input("Enter Input numbers :"))
    for i in range(no):
        lst.append(int(input("Enter number:")))
    Maximum(lst)


if(__name__ == "__main__"):
    main()