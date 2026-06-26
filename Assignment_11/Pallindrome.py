#***************************************************************************************************
#                     Find if a given number is palindrome or not                                      
#***************************************************************************************************

def IsPalindrome(no1):
    rev = 0
    first_digit = True
    no = no1
    if(no1 == 0):
        return True
    while(no1 > 0):
        dig = no1%10
        no1 = int(no1/10);
        if first_digit:
            rev = dig
            first_digit = False
        else :
            rev = rev*10 + dig
    if(rev == no):
        return True
    return False

def main():
    no1 = int(input("Enter Number :"))
    if(IsPalindrome(no1) == True):
        print("Given number", no1, "is Palindrome number.")
    else:
        print("Given number", no1, "is Not a Palindrome number.")

if(__name__ == "__main__"):
    main()