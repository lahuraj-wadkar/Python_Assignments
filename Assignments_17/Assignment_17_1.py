import Arithmetic
def main():
    no1 = int(input("Enter number :"))
    no2 = int(input("Enter number :"))
    print(f"Addition of {no1} and {no2} is {Arithmetic.Add(no1, no2)}")
    print(f"Substraction of {no1} and {no2} is {Arithmetic.Substraction(no1, no2)}")
    print(f"Multiplication of {no1} and {no2} is {Arithmetic.Mult(no1, no2)}")
    print(f"Division of {no1} and {no2} is {Arithmetic.Div(no1, no2)}")
    
if(__name__ == "__main__"):
    main()