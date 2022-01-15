k = int(input())

'''
GRID
3 5 3
5 8 5
3 5 3
'''

n3 = 4 # The number of "3" in the initial grid
n5 = 4 # The number of "5" in the initial grid
n8 = 1 # The number of "8" in the initial grid
values = [n3, n5, n8]

combinations = 0

for i in range(k):
    n3 = 2*values[1] + 4*values[2]
    n5 = 2*values[0] + 2*values[1] + 4*values[2]
    n8 = values[0] + values[1]
    
    values = [n3, n5, n8]
    combinations += n3 + n5 + n8
    
print(combinations)
    
    