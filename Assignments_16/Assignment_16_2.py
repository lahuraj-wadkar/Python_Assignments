def chkNum(no):
    if(no%2 == 0):
        print("Even Number")
    else:
        print("Odd Number")
def main():
    no = int(input("Enter number :"))
    chkNum(no)
if(__name__ == "__main__"):
    main()