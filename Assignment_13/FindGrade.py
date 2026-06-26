#***************************************************************************************************
#                     Find a Grade as per Marks obtained                                      
#***************************************************************************************************

def FindGrade(marks):
    if(marks >= 75):
        print("You got Distinction!")
    elif(marks < 75 and marks >= 60):
        print("You got First Class!")
    elif(marks < 60 and marks >= 50):
        print("You got second class!")
    else:
        print("You are Fail.")

def main():
    no1 = int(input("Enter obtained Marks :"))
    FindGrade(no1)

if(__name__ == "__main__"):
    main()