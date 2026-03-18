num_of_processes = int(input("Enter the number of processes: "))
num_of_resources = int(input("Enter the number of resources: "))

print("Enter the Allocation Matrix:")
allocation_matrix = []
for i in range(num_of_processes):
    allocation_matrix.append(list(map(int, input().split())))

print("Enter the Max Matrix:")
max_matrix = []
for i in range(num_of_processes):
    max_matrix.append(list(map(int, input().split())))

print("Enter Available Vector:")
available_vector = list(map(int, input().split()))

def bankers(num_of_processes, num_of_resources, allocation_matrix, max_matrix, available_vector):
    n = num_of_processes
    r = num_of_resources
    end = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        executed = False
        for i in range(n):
            if not end[i]:
                need_matrix = [max_matrix[i][j] - allocation_matrix[i][j] for j in range(r)]
                if all(need_matrix[j] <= available_vector[j] for j in range(r)):
                    available_vector = [available_vector[j] + allocation_matrix[i][j] for j in range(r)]
                    end[i] = True
                    safe_sequence.append(i)
                    executed = True
        if not executed:
            print("System not in safe state")
            return
    print("System is in safe state")
    print(safe_sequence)

bankers(num_of_processes, num_of_resources, allocation_matrix, max_matrix, available_vector)