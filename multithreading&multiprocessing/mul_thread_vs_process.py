import time
import threading
def some_task():
    time.sleep(1)
    print("Finished task")
if __name__ == "__main__":
    start = time.time()
    # Create two threads
    t1 = threading.Thread(target=some_task)
    t2 = threading.Thread(target=some_task)
    # Start running both threads
    t1.start()
    t2.start()
    # Wait until both threads are complete, and join the process into a single thread
    t1.join()
    t2.join()
    end = time.time()
    print(f"Finished process in {end - start} seconds")

# print("**************")

import time
import multiprocessing
def some_task():
    for _ in range(100_000_000):
        x = 1 + 1
    print("Finished task")
if __name__ == "__main__":
    start = time.time()
    # Create two threads
    p1 = multiprocessing.Process(target=some_task)
    p2 = multiprocessing.Process(target=some_task)
    # Start running both threads
    p1.start()
    p2.start()
    # Wait until both threads are complete, and join the process into a single thread
    p1.join()
    p2.join()
    end = time.time()
    print(f"Finished process in {end - start} seconds")