import threading
import time

BUFFER_SIZE = 5

buffer = [0] * BUFFER_SIZE
in_position = 0
out_position = 0

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

mutex = threading.Lock()
print("S089 Palak Jaiswal")
def producer():
    global in_position

    for i in range(1, 11):
        item = i

        empty.acquire()

        with mutex:
            buffer[in_position] = item
            print(f"Producer produced: {item} at position {in_position}")
            in_position = (in_position + 1) % BUFFER_SIZE

        full.release()
        time.sleep(1)

def consumer():
    global out_position

    for i in range(1, 11):
        full.acquire()

        with mutex:
            item = buffer[out_position]
            print(f"Consumer consumed: {item} from position {out_position}")
            out_position = (out_position + 1) % BUFFER_SIZE

        empty.release()
        time.sleep(2)

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("\nProgram completed successfully.")
