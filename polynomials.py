n, k = input().split()
n, k = int(n), int(k)

coefficients = input().split()
coefficients = list(map(lambda x : int(x), coefficients))

values = []

for i in range(n+1):
    value = coefficients[i]*(2**i)
    values.append(value)
    
total = sum(values)
counter = 0

for element in range(len(values)):
    # find the value of the total sum - the element we want to change
    without = total - values[element]
    
    # the difference is the number we need to change * -1
    wish = -1 * without
    
    # now we need to find the actual coefficient
    a = wish / (2**element)
    if wish // (2**element) == a:    
        if -k<= a <= k:
            counter += 1
        
print(counter)
