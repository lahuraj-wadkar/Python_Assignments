#***************************************************************************************************
#                                         Check Greater Number                                         
#***************************************************************************************************

def ChkGreater(no1, no2):
    greater = no2
    if no1 > no2 :
        greater = no1
    elif(no1 == no2):
        print("Both Numbers are Equal")
        return
    print("Greater Number :", greater)
       

def main():
    no1 = int(input("Enter First Number :"))
    no2 = int(input("Enter Second Number :"))
    ChkGreater(no1, no2)

if(__name__ == "__main__"):
    main()