def PrintReverse(no1):
    for i in range(no1, 0, -1):
        print(i, end=" ")
    print()
def main():
    no1 = int(input("Enter number :"))
    PrintReverse(no1)
if(__name__ == "__main__"):
    main()