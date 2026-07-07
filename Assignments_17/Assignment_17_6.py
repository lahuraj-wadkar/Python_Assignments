def displayPatterrn(val):
    for i in range(val, 0, -1):
        print("*    "*i)
def main():
    no = int(input("Enter number :"))
    ret = displayPatterrn(no)

if(__name__ == "__main__"):
    main()