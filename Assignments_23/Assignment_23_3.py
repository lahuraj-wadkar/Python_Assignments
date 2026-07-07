#***************************************************************************************************
#                  count even numbers from 1 to N for lst members using multicore Pool                       
#***************************************************************************************************


from multiprocessing import Pool
import os   
import time

def countEven(val):
    count = 0
    for i in range(2, val+1, 2):
        count += 1
    print(f"PID = {os.getpid()}: totam Even numbers from 1 to {val} is {count}")


def main():
    lst = [10000000, 20000000, 30000000, 40000000, 50000000, 60000000]
    objPool = Pool()
    start = time.perf_counter()
    objPool.map(countEven, lst)
    objPool.close()
    objPool.join()
    end = time.perf_counter()
    print(f"Time taken = {end-start:.6f}")


if(__name__ == "__main__"):
    main()