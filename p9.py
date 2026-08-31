def fifo(pages, frames):
    memory = []
    hits = 0
    misses = 0
    print("\n===== FIFO PAGE REPLACEMENT =====")
    for page in pages:
        if page in memory:
            hits += 1
            print("Page", page, "-> HIT   Memory:", memory)
        else:
            misses += 1
            if len(memory) == frames:
                memory.pop(0)
            memory.append(page)
            print("Page", page, "-> MISS  Memory:", memory)
    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)
    print("\nFIFO Results")
    print("Hits       =", hits)
    print("Misses     =", misses)
    print("Hit Ratio  =", round(hit_ratio * 100, 2), "%")
    print("Miss Ratio =", round(miss_ratio * 100, 2), "%")
def lru(pages, frames):
    memory = []
    hits = 0
    misses = 0
    print("\n===== LRU PAGE REPLACEMENT =====")
    for page in pages:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
            print("Page", page, "-> HIT   Memory:", memory)
        else:
            misses += 1
            if len(memory) == frames:
              memory.pop(0)
            memory.append(page)
            print("Page", page, "-> MISS  Memory:", memory)
    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)
    print("\nLRU Results")
    print("Hits       =", hits)
    print("Misses     =", misses)
    print("Hit Ratio  =", round(hit_ratio * 100, 2), "%")
    print("Miss Ratio =", round(miss_ratio * 100, 2), "%")
pages = [1, 2, 3, 1, 4, 5, 2, 1, 2, 3]
frames = 3
print("Palak S089")
print("======================================")
print("   MEMORY MANAGEMENT TECHNIQUES")
print("======================================")
print("\nPage Reference String:")
print(pages)
print("Number of Frames:", frames)
fifo(pages, frames)
lru(pages, frames)
