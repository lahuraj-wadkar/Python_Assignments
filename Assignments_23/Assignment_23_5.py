#***************************************************************************************************
#                  factorial of  lst members using multicore Pool                       
#***************************************************************************************************


from multiprocessing import Pool
import os   
import time

def factorial(val):
    fact = 1
    for i in range(1, val+1):
        fact *= i
    print(f"PID = {os.getpid()}: factorial of {val} is {fact}")


def main():
    lst = [10, 15, 20, 25, 30, 35]
    objPool = Pool()
    start = time.perf_counter()
    objPool.map(factorial, lst)
    objPool.close()
    objPool.join()
    end = time.perf_counter()
    print(f"Time taken = {end-start:.6f}")


if(__name__ == "__main__"):
    main()