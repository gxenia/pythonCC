from itertools import permutations

def step1(message):
    message = message[1:] + message[:1]
    message = message[0::2] + message[1::2]
    message = message[1:] + message[:1]
    
    return message

def unstep1(original):
    original = original[len(original)-1:]+ original[:len(original)-1]

    half = len(original)//2
    first_half = original[:half]
    second_half = original[half:]
        
    n = ""
    for i in range(half):
        n += first_half[i] + second_half[i]
    original = n

    original = original[len(original)-1:]+ original[:len(original)-1]
    
    return original
    
    
def step2(message, key):
    res = ""
    for j in range(0, len(message), W):
        for k in range(W):
            res += message[j:j+W][key[k]]
    return res

def unstep2(message, key):
    res = ""
    for j in range(0, len(message), 7):
        empty = [0, 0, 0, 0, 0, 0, 0]
        for k in range(7):
            empty[key[k]] = message[j:j+7][k]
        res += ''.join(empty)
    return res

def scramble(message, key):
    W = len(key)
    while len(message) % (2*W):
        message += "#"

    for _ in range(128):
        message = message[1:] + message[:1]
        message = message[0::2] + message[1::2]
        message = message[1:] + message[:1]
        res = ""
        for j in range(0, len(message), W):
            for k in range(W):
                res += message[j:j+W][key[k]]
        message = res

    return message

    
'''
key = [1, 3, 6, 0, 2, 4, 5]
W = len(key)
message = "AcciderbolinaaAcciderbolinaaAcciderbolinaa"
print(scramble(message, key))

# Encryption
for _ in range(128):
    message = step1(message)
    message = step2(message, key)
print(message)
'''

encrypted = "l_4Tnb_3cnnbcg3r3slCCm4Id__gb4u}ct{0mr3sds"
key = list(range(7))
comb = [i for i in permutations(key)]
solutions = []

# Decryption    
for c in comb:
    message = encrypted
    c = list(c)
    for _ in range(128):
        message = unstep2(message, c)
        message = unstep1(message)
    print(message)
    if message[:4] == "CCIT":
        solutions.append((message, c))
    
print(solutions)


