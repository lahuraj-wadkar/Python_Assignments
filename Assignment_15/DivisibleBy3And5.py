#***************************************************************************************************
#                  Using filter and lambda print numbers divisible by 3 and 5 from list                                      
#***************************************************************************************************
isDivisibleBy3And5 = lambda x:((x%5==0) and (x%3==0))

def main():
    lst = list()
    for i in range(0,10):
        val = int(input("Enter value :"))
        lst.append(val)
    print("Given List", lst)
    lst = list(filter(isDivisibleBy3And5, lst))
    print("Numbers Divisble By 3 and 5 from List are :", lst)

if(__name__=="__main__"):
    main()