def proMove(tasks):
    
    first = 0
    p1 = 0
    
    second = 0
    p2 = 0
    
    # The maximum difference is the sum of the 2 highest values
    # Finding the first highest
    
    for i in range(len(tasks)):
        if tasks[i] > first:
            first = tasks[i]
            p1 = i
            
    for i in range(len(tasks)):
        if tasks[i] > second and tasks[i] != first:
            second = tasks[i]
            p2 = i
            
    tasks[p1] = tasks[p1] + tasks[p2]
    tasks[p2] = 0
    
    return tasks[p1]    
        

n, k = input().split()
n, k = int(n), int(k)

tasks = input().split()
for i in range(n):
    tasks[i] = int(tasks[i])

for i in range(k):
    answer = proMove(tasks)
    
print(answer)
