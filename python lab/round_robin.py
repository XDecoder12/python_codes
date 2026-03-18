processes = ["P1", "P2", "P3"]

b1 = int(input("Enter burst time for P1: "))
b2 = int(input("Enter burst time for P2: "))
b3 = int(input("Enter burst time for P3: "))
q = int(input("Enter time quantum: "))

burst = [b1, b2, b3]
remaining = burst.copy()
waiting = [0, 0, 0]
time = 0

while True:
    done = True
    for i in range(3):
        if remaining[i] > 0:
            done = False
            if remaining[i] > q:
                time += q
                remaining[i] -= q
            else:
                time += remaining[i]
                waiting[i] = time - burst[i]
                remaining[i] = 0
    if done:
        break

turnaround = [burst[i] + waiting[i] for i in range(3)]

print("\nProcess  BT  WT  TAT")
print(f"P1       {burst[0]}   {waiting[0]}   {turnaround[0]}")
print(f"P2       {burst[1]}   {waiting[1]}   {turnaround[1]}")
print(f"P3       {burst[2]}   {waiting[2]}   {turnaround[2]}")

avg_wt = sum(waiting) / 3
avg_tat = sum(turnaround) / 3

print("\nAverage Waiting Time =", avg_wt)
print("Average Turnaround Time =", avg_tat)