#***************************************************************************************************
#                  Sum sum of squares from 1 to N for lst members using multicore Pool                       
#***************************************************************************************************


from multiprocessing import Pool
import os   
import time

def sumOfSquares(val):
    sum = 0
    for i in range(1, val+1):
        sum += (i*i)
    print(f"PID = {os.getpid()}: sum of squares from 1 to {val} is {sum}")


def main():
    lst = [10000000, 20000000, 30000000, 40000000, 50000000, 60000000]
    objPool = Pool()
    start = time.perf_counter()
    objPool.map(sumOfSquares, lst)
    objPool.close()
    objPool.join()
    end = time.perf_counter()
    print(f"Time taken = {end-start:.6f}")


if(__name__ == "__main__"):
    main()