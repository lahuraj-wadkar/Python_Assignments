#***************************************************************************************************
#                  Find Frequency of a number from  list                       
#***************************************************************************************************


def Frequency(lst, val):
    freq = 0
    for i in lst:
        if(val == i):
            freq += 1
    print(f"Frequency of {val} in list is  {freq}")


def main():
    lst = []
    no = int(input("Enter Input numbers :"))
    for i in range(no):
        lst.append(int(input("Enter number:")))
    no = int(input("Enter number to search :"))
    Frequency(lst, no)


if(__name__ == "__main__"):
    main()