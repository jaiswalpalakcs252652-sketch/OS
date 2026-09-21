def fcfs(requests, head):
    movement = 0
    current = head
    for request in requests:
        movement += abs(current - request)
        current = request
    return movement


def sstf(requests, head):
    requests = requests.copy()
    movement = 0
    current = head

    while requests:
        nearest = min(requests, key=lambda x: abs(current - x))
        movement += abs(current - nearest)
        current = nearest
        requests.remove(nearest)

    return movement


def cscan(requests, head, disk_size=200):
    requests = sorted(requests)
    left = [x for x in requests if x < head]
    right = [x for x in requests if x >= head]

    movement = 0
    current = head

    for x in right:
        movement += abs(current - x)
        current = x

    if left:
        movement += abs(current - (disk_size - 1))
        current = disk_size - 1
        movement += disk_size - 1
        current = 0

        for x in left:
            movement += abs(current - x)
            current = x

    return movement


def clook(requests, head):
    requests = sorted(requests)
    left = [x for x in requests if x < head]
    right = [x for x in requests if x >= head]

    movement = 0
    current = head

    for x in right:
        movement += abs(current - x)
        current = x

    if left:
        movement += abs(current - left[0])
        current = left[0]

        for x in left[1:]:
            movement += abs(current - x)
            current = x

    return movement


def rss(requests, head):
    import random

    requests = requests.copy()
    random.shuffle(requests)

    movement = 0
    current = head

    for request in requests:
        movement += abs(current - request)
        current = request

    return movement


class FileSystem:

    def __init__(self):
        self.files = {}
        self.blocks = {}

    def create(self, name, data):
        if name in self.files:
            print("File already exists!")
            return

        block = len(self.files) + 1
        self.files[name] = data
        self.blocks[name] = block
        print("File created successfully!")

    def read(self, name):
        if name in self.files:
            print("File Data:", self.files[name])
        else:
            print("File not found!")

    def delete(self, name):
        if name in self.files:
            del self.files[name]
            del self.blocks[name]
            print("File deleted successfully!")
        else:
            print("File not found!")

    def directory(self):
        if not self.files:
            print("Directory is empty!")
        else:
            print("\nDirectory:")
            for name in self.files:
                print(name, "-> Block", self.blocks[name])


requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53

print("===== DISK SCHEDULING =====")
print("Requests:", requests)
print("Initial Head:", head)

print("\nFCFS Head Movement:", fcfs(requests, head))
print("SSTF Head Movement:", sstf(requests, head))
print("C-SCAN Head Movement:", cscan(requests, head))
print("C-LOOK Head Movement:", clook(requests, head))
print("RSS Head Movement:", rss(requests, head))

print("\n===== SIMPLE FILE SYSTEM =====")

fs = FileSystem()

fs.create("file1.txt", "Hello World")
fs.create("file2.txt", "Operating System")

fs.directory()

print("\nReading file1.txt:")
fs.read("file1.txt")

print("\nDeleting file1.txt:")
fs.delete("file1.txt")

fs.directory()
