#***************************************************************************************************
#                     Find a number is perfect Number or not                                      
#***************************************************************************************************

def PerfectNumber(no1):
    sum = 0
    for i in range (1, int(no1/2)+1):
        if(no1%i == 0):
            sum = sum + i
    if(sum == no1):
        print("Given number",no1,"is perfect Numer!")
    else:
        print("Given number",no1,"is not perfect Numer.")

def main():
    no1 = int(input("Enter Number :"))
    PerfectNumber(no1)

if(__name__ == "__main__"):
    main()