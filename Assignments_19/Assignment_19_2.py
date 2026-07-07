#***************************************************************************************************
#                  Use of lambda function                       
#***************************************************************************************************

mult=lambda x,y:(x*y)

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    ret = mult(no1, no2)
    print(f"{no1}  * {no2}  = {ret}")

if (__name__ == "__main__"):
    main()