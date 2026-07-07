#***************************************************************************************************
#                  Sum of odd numbers from 1 to N for lst members using multicore Pool                       
#***************************************************************************************************


from multiprocessing import Pool
import os   
import time

def sumOfOdd(val):
    sum = 0
    for i in range(1, val+1, 2):
        sum += i
    print(f"PID = {os.getpid()}: sum of Odd numbers from 1 to {val} is {sum}")


def main():
    lst = [10000000, 20000000, 30000000, 40000000, 50000000, 60000000]
    objPool = Pool()
    start = time.perf_counter()
    objPool.map(sumOfOdd, lst)
    objPool.close()
    objPool.join()
    end = time.perf_counter()
    print(f"Time taken = {end-start:.6f}")


if(__name__ == "__main__"):
    main()