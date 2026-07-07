def chkPrime(val):
    isPrime = True
    if val == 1:
        isPrime=False
    if(val == 2):
        isPrime=True
    for i in range(2,(int(val/2)+1)):
        if(val%i == 0):
            isPrime=False
            break
    return isPrime 
def main():
    no = int(input("Enter number :"))
    ret = chkPrime(no)
    print(f"{"Prime Number" if (ret == True) else "Not Prime"}")

if(__name__ == "__main__"):
    main()