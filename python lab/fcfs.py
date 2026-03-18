print("Enter burst time for P1:")
b1 = int(input())

print("Enter burst time for P2:")
b2 = int(input())

print("Enter burst time for P3:")
b3 = int(input())

w1 = 0
w2 = b1
w3 = b1 + b2

t1 = b1 + w1
t2 = b2 + w2
t3 = b3 + w3

avg_w = (w1 + w2 + w3) / 3
avg_t = (t1 + t2 + t3) / 3

print("\nProcess  BT  WT  TAT")
print(f"P1       {b1}  {w1}   {t1}")
print(f"P2       {b2}  {w2}   {t2}")
print(f"P3       {b3}  {w3}   {t3}")

print("\nAverage Waiting Time =", avg_w)
print("Average Turnaround Time =", avg_t)