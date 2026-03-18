def bankers(processes, resources, allocation, max_need, available):
    n = processes
    m = resources
    finish = [False] * n
    safe_seq = []

    while len(safe_seq) < n:
        executed = False
        for i in range(n):
            if not finish[i]:
                need = [max_need[i][j] - allocation[i][j] for j in range(m)]
                if all(need[j] <= available[j] for j in range(m)):
                    available = [available[j] + allocation[i][j] for j in range(m)]
                    finish[i] = True
                    safe_seq.append(f"P{i}")
                    executed = True
        if not executed:
            print("System is NOT in safe state")
            return
    print("Safe Sequence:", " → ".join(safe_seq))


processes = int(input("Enter number of processes: "))
resources = int(input("Enter number of resources: "))

allocation = []
max_need = []

print("Enter Allocation Matrix:")
for i in range(processes):
    allocation.append(list(map(int, input().split())))

print("Enter Max Matrix:")
for i in range(processes):
    max_need.append(list(map(int, input().split())))

print("Enter Available Resources:")
available = list(map(int, input().split()))

print("\nBanker's Algorithm Result:\n")
bankers(processes, resources, allocation, max_need, available)