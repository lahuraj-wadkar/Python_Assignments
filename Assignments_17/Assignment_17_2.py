def displayPatterrn(val):
    for i in range(val):
        print("*    "*val)
def main():
    no = int(input("Enter number :"))
    ret = displayPatterrn(no)

if(__name__ == "__main__"):
    main()