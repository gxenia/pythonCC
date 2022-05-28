from itertools import permutations

def main():
    message = "l_4Tnb_3cnnbcg3r3slCCm4Id__gb4u}ct{0mr3sds"
    key = list(range(7))
    comb = [i for i in permutations(key)]
    for c in comb:
        print(c)
        flag = unscramble(message, c)
        print(flag, ''.join(flag[:4]))
        if ''.join(flag[:4]) == "CCIT":
            print(flag)
            
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


def unscramble(message, key):
    for _ in range(128):
        res = ""
        for j in range(0, len(message), 7):
            empty = [0, 0, 0, 0, 0, 0, 0]
            for k in range(7):
                empty[key[k]] = message[j:j+7][k]
            res += ''.join(empty)
        original = res
        original = original[len(original)-1:]+ original[:len(original)-1]
        
        half = len(original)//2
        first_half = original[:half]
        second_half = original[half:]
        
        message = ""
        for i in range(half):
            message += first_half[i] + second_half[i]
        original = message
        
        original = original[len(original)-1:]+ original[:len(original)-1]
        
        
        return ''.join(original)        
        
    

main()