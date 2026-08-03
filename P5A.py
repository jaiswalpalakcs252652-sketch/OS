import threading
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")
numbers = [1, 2, 3]
threads = []
print("Multi-threaded Factorial Program\n")
for num in numbers:
    t = threading.Thread(target=factorial, args=(num,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("\nAll threads completed.")

