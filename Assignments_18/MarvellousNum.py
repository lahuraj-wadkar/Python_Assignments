#***************************************************************************************************
#                  Module to chek Prime Numbers                      
#***************************************************************************************************
def chkPrime(val):
    isPrime = True
    if val == 1:
        isPrime=False
    if(val == 2):
        isPrime=True
    for i in range(2,(int(val/2)+1)):
        if(val%i == 0):
            isPrime=False
            break
    return isPrime