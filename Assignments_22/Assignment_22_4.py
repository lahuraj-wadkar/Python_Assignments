#***************************************************************************************************
#                  sum power to 5 from 1 to N of lst members using multicore Pool                       
#***************************************************************************************************


from multiprocessing import Pool
import os   
import time

def power(val):
    sum = 0
    for i in range(1, val+1):
        sum += i**5
    print(f"PID = {os.getpid()}: Sum of 1 to N (power 5) {val} is {sum}")


def main():
    lst = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000]
    objPool = Pool()
    start = time.perf_counter()
    objPool.map(power, lst)
    objPool.close()
    objPool.join()
    end = time.perf_counter()
    print(f"Time taken = {end-start:.6f}")


if(__name__ == "__main__"):
    main()