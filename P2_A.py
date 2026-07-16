from multiprocessing import Process, Queue
import time
import random

def producer(queue):
    for i in range(5):
        item = random.randint(1, 100)
        print(f"Producer wants to produce: {item}")
        queue.put(item)  
        print(f"Producer produced: {item}")
        time.sleep(0.5) 

def consumer(queue):
    for i in range(5):
        print("Consumer is waiting for an item...")
        item = queue.get()  
        print(f"Consumer consumed: {item}")
        time.sleep(2)  

if __name__ == "__main__":
    q = Queue(maxsize=3)
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Producer and Consumer have finished.")
