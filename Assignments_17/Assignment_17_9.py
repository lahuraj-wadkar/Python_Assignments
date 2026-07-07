def countDigits(val):
    digit = 0
    while(val > 0):
        digit += 1
        val = int(val/10)
 
    print(f"No of Digits are {digit}")
def main():
    no = int(input("Enter number :"))
    countDigits(no)

if(__name__ == "__main__"):
    main()