#***************************************************************************************************
#                  checkPrime for every  list member using multiprocessing Pool                       
#***************************************************************************************************


from multiprocessing import Pool
import os   
import time

def chkPrime(val):
    isPrime = True
    if val == 1:
        isPrime=False
    if(val == 2):
        isPrime=True
    for i in range(2,(int(val/2)+1)):
    #for i in range(2,val):
        if(val%i == 0):
            isPrime=False
            print(f"{val} is divisible by {i} so not a prime number")
            break
    if(isPrime == True):
        print(f"PID = {os.getpid()}: {val} is prime numeber")


def main():
    lst = [1000003, 5234779, 8765317, 9999937, 1000003, 1000003, 1000003, 2147483647, 512000009, 900000011]
    objPool = Pool()
    start = time.perf_counter()
    objPool.map(chkPrime, lst)
    objPool.close()
    objPool.join()
    end = time.perf_counter()
    print(f"Time taken = {end-start:.6f}")


if(__name__ == "__main__"):
    main()