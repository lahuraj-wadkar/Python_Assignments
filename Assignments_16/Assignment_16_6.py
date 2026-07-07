def chkNumber(no1):
    print(f"{"Positive" if (no1 > 0) else ("Negative" if no1 < 0 else "Zero" )}")
def main():
    no1 = int(input("Enter number :"))
    chkNumber(no1)
if(__name__ == "__main__"):
    main()