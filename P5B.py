import threading
def even_odd():
    print("Even Numbers:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(i, end=" ")
    print("\n\nOdd Numbers:")
    for i in range(1, 11):
        if i % 2 != 0:
            print(i, end=" ")
def reverse_string():
    text = "Python"
    print("\n\nOriginal String:", text)
    print("Reversed String:", text[::-1])
t1 = threading.Thread(target=even_odd)
t2 = threading.Thread(target=reverse_string)
print("Multithreading Example\n")
t1.start()
t2.start()
t1.join()
t2.join()
print("\n\nAll threads completed.")
