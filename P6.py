from collections import deque

def fcfs(processes):
    current_time = 0
    print("\n========== FCFS ==========")
    print("PID\tAT\tBT\tCT\tTAT\tWT\tRT")
    total_wt = 0
    total_tat = 0
    total_rt = 0
    for p in processes:
        pid = p["pid"]
        arrival = p["arrival"]
        burst = p["burst"]
        if current_time < arrival:
            current_time = arrival
        response = current_time - arrival
        current_time += burst
        completion = current_time
        turnaround = completion - arrival
        waiting = turnaround - burst
        print(
            f"P{pid}\t{arrival}\t{burst}\t"
            f"{completion}\t{turnaround}\t"
            f"{waiting}\t{response}"
        )
        total_wt += waiting
        total_tat += turnaround
        total_rt += response
    n = len(processes)
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Response Time: {total_rt / n:.2f}")

def round_robin(processes, quantum):
    n = len(processes)
    remaining = [p["burst"] for p in processes]
    completion = [0] * n
    response = [-1] * n
    ready_queue = deque()
    current_time = 0
    completed = 0
    next_process = 0
    context_switches = 0
    last_process = -1
    print("\n========== ROUND ROBIN ==========")
    print("Time Quantum:", quantum)
    print("\nExecution Sequence:")
    while completed < n:
        while (
            next_process < n
            and processes[next_process]["arrival"] <= current_time
        ):
            ready_queue.append(next_process)
            next_process += 1
        if not ready_queue:
            if next_process < n:
                current_time = processes[next_process]["arrival"]
                continue
        index = ready_queue.popleft()
        pid = processes[index]["pid"]
        if response[index] == -1:
            response[index] = (
                current_time - processes[index]["arrival"]
            )
        if last_process != -1 and last_process != index:
            context_switches += 1
        start_time = current_time
        execution_time = min(
            quantum,
            remaining[index]
        )
        current_time += execution_time
        remaining[index] -= execution_time
        print(
            f"P{pid}: {start_time} -> {current_time}"
        )
        last_process = index
        while (
            next_process < n
            and processes[next_process]["arrival"] <= current_time
        ):
            ready_queue.append(next_process)
            next_process += 1
        if remaining[index] == 0:
            completed += 1
            completion[index] = current_time
        else:
            ready_queue.append(index)
    print("\nPID\tAT\tBT\tCT\tTAT\tWT\tRT")
    total_wt = 0
    total_tat = 0
    total_rt = 0
    for i in range(n):
        arrival = processes[i]["arrival"]
        burst = processes[i]["burst"]
        turnaround = completion[i] - arrival
        waiting = turnaround - burst
        print(
            f"P{processes[i]['pid']}\t"
            f"{arrival}\t"
            f"{burst}\t"
            f"{completion[i]}\t"
            f"{turnaround}\t"
            f"{waiting}\t"
            f"{response[i]}"
        )
        total_wt += waiting
        total_tat += turnaround
        total_rt += response[i]
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Response Time: {total_rt / n:.2f}")
    print("Context Switches:", context_switches)
n = int(input("Enter number of processes: "))
processes = []
print("\nEnter Arrival Time and Burst Time:")
for i in range(n):
    arrival = int(input(f"P{i + 1} Arrival Time: "))
    burst = int(input(f"P{i + 1} Burst Time: "))
    processes.append({
        "pid": i + 1,
        "arrival": arrival,
        "burst": burst
    })
quantum = int(input("\nEnter Time Quantum: "))
fcfs(processes)
round_robin(processes, quantum)
