n = int(input("Enter the integer: "))

for x in range(1,n+1):
    for s in range(n-x):
        print(" ", end="")
    for i in range(1,x+1):
        print(i, end="")
    for i in range(x-1,0,-1):
        print(i, end="")
    print()

for y in range(n-1,0,-1):
    for s in range(n-y):
        print(" ", end="")
    for i in range(1,y+1):
        print(i, end="")
    for i in range(y-1,0,-1):
        print(i, end="")
    print()