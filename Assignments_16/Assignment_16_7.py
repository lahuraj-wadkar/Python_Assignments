def divisibleBy5(no1):
    return (no1%5==0)
def main():
    no1 = int(input("Enter number :"))
    print({"Divisible by 5" if divisibleBy5(no1) else "Not divisible by 5"})
if(__name__ == "__main__"):
    main()