def factorial(no1):
    fact = 1
    for i in range(1, no1+1):
        fact *= i
    print("Factorial  :", fact)
def main():
    no = int(input("Enter number :"))
    factorial(no)
if(__name__ == "__main__"):
    main()