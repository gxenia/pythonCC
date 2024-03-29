def findMaxofMin(v, n, size):
    minimum = []
    
    for i in range(n):
        minimum.append(min(v[i:size]))
        size+=1
        if size > n: break
    
    return max(minimum)


n = int(input())
v = input().split()
v = list(map(lambda x: int(x), v))

sizes = []
for size in range(1, n+1):
    sizes.append(findMaxofMin(v, n, size))
    
print(*sizes, sep = " ")
