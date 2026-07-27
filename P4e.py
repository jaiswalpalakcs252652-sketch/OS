processes = [
    ["P1", 0, 7],
    ["P2", 2, 4],
    ["P3", 4, 1],
    ["P4", 5, 4]
]

time = 0
completed = 0
n = len(processes)
visited = [False] * n

result = []

while completed < n:
    idx = -1
    minimum = 999

    for i in range(n):
        if processes[i][1] <= time and not visited[i]:
            if processes[i][2] < minimum:
                minimum = processes[i][2]
                idx = i

    if idx == -1:
        time += 1
        continue

    start = time
    finish = start + processes[idx][2]

    wt = start - processes[idx][1]
    tat = finish - processes[idx][1]

    result.append([processes[idx][0], processes[idx][1], processes[idx][2], wt, tat, start, finish])

    time = finish
    visited[idx] = True
    completed += 1

print("Process\tAT\tBT\tWT\tTAT")

total_wt = 0
total_tat = 0

for r in result:
    print(r[0], "\t", r[1], "\t", r[2], "\t", r[3], "\t", r[4])
    total_wt += r[3]
    total_tat += r[4]

print("\nAverage Waiting Time =", total_wt / n)
print("Average Turnaround Time =", total_tat / n)

print("\nGantt Chart")
print("0", end="")
for r in result:
    print(" |", r[0], "|", r[6], end="")
print()
