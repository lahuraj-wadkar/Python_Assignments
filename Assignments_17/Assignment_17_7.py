def displayPatterrn(val):
    for i in range(val):
        for j in range(1, val+1):
            print(j, end="  ")
        print()
def main():
    no = int(input("Enter number :"))
    ret = displayPatterrn(no)

if(__name__ == "__main__"):
    main()