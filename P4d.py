processes = ["P1", "P2", "P3", "P4"]
arrival = [0, 1, 2, 3]
burst = [5, 3, 8, 6]

n = len(processes)

waiting = [0] * n
turnaround = [0] * n
completion = [0] * n

completion[0] = arrival[0] + burst[0]
turnaround[0] = completion[0] - arrival[0]
waiting[0] = turnaround[0] - burst[0]

for i in range(1, n):
    if completion[i - 1] < arrival[i]:
        completion[i] = arrival[i] + burst[i]
    else:
        completion[i] = completion[i - 1] + burst[i]

    turnaround[i] = completion[i] - arrival[i]
    waiting[i] = turnaround[i] - burst[i]

print("Process\tAT\tBT\tWT\tTAT")
for i in range(n):
    print(processes[i], "\t", arrival[i], "\t", burst[i], "\t", waiting[i], "\t", turnaround[i])

print("\nAverage Waiting Time =", sum(waiting) / n)
print("Average Turnaround Time =", sum(turnaround) / n)

print("\nGantt Chart")
print("0", end="")
time = 0
for i in range(n):
    time += burst[i]
    print(" |", processes[i], "|", time, end="")
print()


