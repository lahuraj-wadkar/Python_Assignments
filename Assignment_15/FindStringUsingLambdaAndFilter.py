#***************************************************************************************************
#                  Print all the strings having length greater than 5 from list                                      
#***************************************************************************************************
string_5 = lambda x:(len(x) > 5)

def main():
    lst = list()
    for i in range(0,10):
        val = input("Enter String :")
        lst.append(val)
    print("Given List", lst)
    lst = list(filter(string_5, lst))
    print("List with strings having length greater than 5  :", lst)

if(__name__=="__main__"):
    main()