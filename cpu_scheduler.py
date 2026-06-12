from collections import deque


class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.completion = 0
        self.waiting = 0
        self.turnaround = 0


def print_results(processes):
    avg_wt = 0
    avg_tat = 0

    print("\n------------------------------------------------")
    print("PID\tAT\tBT\tCT\tWT\tTAT")
    print("------------------------------------------------")

    for p in processes:
        print(
            f"P{p.pid}\t{p.arrival}\t{p.burst}\t"
            f"{p.completion}\t{p.waiting}\t{p.turnaround}"
        )

        avg_wt += p.waiting
        avg_tat += p.turnaround

    print("\nAverage Waiting Time    :", round(avg_wt / len(processes), 2))
    print("Average Turnaround Time :", round(avg_tat / len(processes), 2))


def fcfs(processes):
    print("\n========== FCFS ==========")

    p = sorted(processes, key=lambda x: x.arrival)

    current_time = 0
    gantt = []

    for proc in p:
        if current_time < proc.arrival:
            current_time = proc.arrival

        current_time += proc.burst

        proc.completion = current_time
        proc.turnaround = proc.completion - proc.arrival
        proc.waiting = proc.turnaround - proc.burst

        gantt.append(f"P{proc.pid}")

    print("\nGantt Chart:")
    print(" | ".join(gantt))

    print_results(p)


def sjf(processes):
    print("\n========== SJF ==========")

    p = [Process(x.pid, x.arrival, x.burst) for x in processes]

    n = len(p)
    completed = 0
    current_time = 0
    done = [False] * n
    result = []
    gantt = []

    while completed < n:

        idx = -1
        min_burst = float('inf')

        for i in range(n):
            if (
                not done[i]
                and p[i].arrival <= current_time
                and p[i].burst < min_burst
            ):
                min_burst = p[i].burst
                idx = i

        if idx == -1:
            current_time += 1
            continue

        current_time += p[idx].burst

        p[idx].completion = current_time
        p[idx].turnaround = current_time - p[idx].arrival
        p[idx].waiting = p[idx].turnaround - p[idx].burst

        done[idx] = True
        completed += 1

        result.append(p[idx])
        gantt.append(f"P{p[idx].pid}")

    print("\nGantt Chart:")
    print(" | ".join(gantt))

    print_results(result)


def round_robin(processes, quantum):
    print("\n========== ROUND ROBIN ==========")

    p = sorted(
        [Process(x.pid, x.arrival, x.burst) for x in processes],
        key=lambda x: x.arrival
    )

    n = len(p)
    q = deque()

    current_time = 0
    index = 0
    completed = 0

    gantt = []

    while index < n and p[index].arrival <= current_time:
        q.append(index)
        index += 1

    if not q:
        q.append(0)
        current_time = p[0].arrival
        index = 1

    while completed < n:

        if not q:
            current_time = p[index].arrival
            q.append(index)
            index += 1

        i = q.popleft()

        if p[i].remaining > quantum:
            current_time += quantum
            p[i].remaining -= quantum

            gantt.append(f"P{p[i].pid}")
        else:
            current_time += p[i].remaining

            gantt.append(f"P{p[i].pid}")

            p[i].remaining = 0
            completed += 1

            p[i].completion = current_time
            p[i].turnaround = current_time - p[i].arrival
            p[i].waiting = p[i].turnaround - p[i].burst

        while index < n and p[index].arrival <= current_time:
            q.append(index)
            index += 1

        if p[i].remaining > 0:
            q.append(i)

    print("\nGantt Chart:")
    print(" | ".join(gantt))

    print_results(p)


def main():
    print("CPU Scheduling Simulator")

    n = int(input("Enter Number of Processes: "))

    processes = []

    for i in range(n):
        print(f"\nProcess P{i + 1}")

        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))

        processes.append(Process(i + 1, arrival, burst))

    fcfs([Process(x.pid, x.arrival, x.burst) for x in processes])

    sjf(processes)

    quantum = int(input("\nEnter Time Quantum for Round Robin: "))

    round_robin(processes, quantum)


if __name__ == "__main__":
    main()
