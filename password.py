def isPermutation(original, subset):
    letter1 = ""
    count1 = 0
    count2 = 0
    
    for i in original:
        
        letter1 = i
        for letter in original:
            if letter == letter1: count1 += 1
        for element in subset:
            if element == letter1: count2 += 1
            
        if count1 != count2:
            return 0
    
    return 1



t = int(input())
results = []

for i in range(t):
    p = input()
    h = input()
    verified = False

    for i in range(len(h)):
        if (i+len(p)) <= len(h):
            if isPermutation(p, h[i:i+len(p)]):
                verified = True
                results.append(1)
                break
        
    if not verified: results.append(0)
    
for i in results:
    print(i)
