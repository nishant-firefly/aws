import random, time
"""
Multiprocessing: Differen process, no memory share 
"""
def print_details(name, count, greeting="Hello"):
    for i in range(count):
        #time.sleep(random.randint(1,10))
        print(f"{greeting}, {name}: {i}")

#################### IO Bound : Multithreading 
## Example file download from network, 1 process same memory. due to GIL one thread, so not true parallelism.
def multi_threading_example():
    import threading
    # Create threads and pass arguments using `args` and `kwargs`
    thread1 = threading.Thread(target=print_details, args=("Thread 1", 5), kwargs={"greeting": "Hi"})
    thread2 = threading.Thread(target=print_details, args=("Thread 2", 3), kwargs={"greeting": "Hey"})
    threads = [thread1, thread2]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

#################### CPU Bound : Multiprocessing
# Different thread, withou __main__ its issue. CPU bound data process in parallel. need external data to cordinate.
# e.g. parallely process different Ids data with foreign Key and cumulate in aggrgator table
import multiprocessing
def multi_processing_example():
    # Create processes and pass arguments using `args` and `kwargs`
    process1 = multiprocessing.Process(target=print_details, args=("Process 1", 5), kwargs={"greeting": "Hi"})
    process2 = multiprocessing.Process(target=print_details, args=("Process 2", 3), kwargs={"greeting": "Hey"})
    processes = [process1, process2]
    for process in processes:
        process.start()

    for process in processes:
        process.join()

#### Async Example: Want to run single thread or porcess and do not want to interrupt execution. Send Email when user register
import asyncio

async def greet(name, delay):
    # Must havve await inside. 
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")


if __name__ == "__main__":

    ## Without If __name__==> __main__ => An attempt has been made to start a new process before the current process has finished its bootstrapping phase.
    print("MP")
    multi_processing_example()
    print("MT")
    multi_threading_example()
    print("AS")







