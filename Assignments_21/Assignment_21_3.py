#***************************************************************************************************
#                  Find minimum and maximum from list using Threads                         
#***************************************************************************************************

import time
import threading

def IncrementCounter(counter, lock):
        with lock:
            for i in range(5):
                counter["value"] += 1
                print(f"Thread id : {threading.get_ident()}, Thread Name = {threading.current_thread().name} counter = {counter["value"]}")


def main():
    counter = {"value": 0} 

    ThreadList = []
    lock = threading.Lock()
    for i in range(10):
        ThreadList.append(threading.Thread(target=IncrementCounter, args=(counter,lock), name=("T"+str(i))))
    for i in range(10):
        ThreadList[i].start()
    for i in range(10):
        ThreadList[i].join()
    print("Exit from main")
    
if(__name__ == "__main__"):
    main()