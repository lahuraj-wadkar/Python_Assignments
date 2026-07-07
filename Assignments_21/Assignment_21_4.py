#***************************************************************************************************
#                  Sum of elements and product of elements using threads                       
#***************************************************************************************************

import threading

def finSum(lst, result):
    sum = 0;
    for x in lst:
        sum = sum + x
    result["Sum"] = sum

def finProduct(lst, result):
    prod = 1;
    for x in lst:
        prod = prod * x
    result["Prod"] = prod

def main():
    lst =[]
    sumResult = {"Sum":0}
    prodResult = {"Prod":0}
    for i in range (10):
        lst.append(int(input("Enter the number :")))
    threading.Thread()
    tobj1 = threading.Thread(target=finSum, args=(lst,sumResult))
    tobj2 = threading.Thread(target=finProduct, args=(lst,prodResult))
    tobj2.start()
    tobj1.start()
    tobj1.join()
    tobj2.join()
    print(f"Sum of elemnets is : {sumResult["Sum"]}")
    print(f"product of elemnets is : {prodResult["Prod"]}")
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()