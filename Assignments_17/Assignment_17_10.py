def AdditionofDigits(val):
    sum = 0
    while(val > 0):
        sum = sum + (val%10)
        val = int(val/10)
 
    print(f"Sum of Digits are {sum}")
def main():
    no = int(input("Enter number :"))
    AdditionofDigits(no)

if(__name__ == "__main__"):
    main()