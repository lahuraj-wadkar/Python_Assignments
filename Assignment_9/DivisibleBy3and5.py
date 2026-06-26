#***************************************************************************************************
#                     Find a number is divisible by 3 and 5                                         
#***************************************************************************************************

def IsDivisibleBy3And5(no1):
    if(no1%3==0 and no1%5==0):
        return True
    return False
       

def main():
    no1 = int(input("Enter First Number :"))
    print("Number <", no1, "> is divisible by 3 and 5 :<", IsDivisibleBy3And5(no1), ">")

if(__name__ == "__main__"):
    main()