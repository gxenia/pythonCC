def main():
    N = int(input())
    ret = []
    for i in range(N):
        new, old = input().split()
        if check_password(new, old): ret.append('1')
        else: ret.append('0')
    for r in ret: print(r)

def check_password(new_password, old_password):
    if len(new_password) < 8 or len(new_password) > 16: 
        return False
    elif not upper_lower(new_password):
        return False
    elif not special_chars(new_password):
        return False
    elif repeated(new_password):
        return False
    elif len(set(new_password).difference(set(old_password))) <= 1:
        return False
    else: return True

def upper_lower(stringa):
    upper = False
    lower = False
    counter = 0
    while (not upper and not lower) and counter <= len(stringa):
        for letter in stringa:
            if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': upper = True
            elif letter in 'abcdefghijklmnopqrstuvwxyz': lower = True
        counter += 1
    return upper and lower

def special_chars(stringa):
    digits = False
    special = False
    for letter in stringa:
        if letter in '1234567890': digits = True
        elif not letter.isalpha(): special = True
    return digits and special 
            
def repeated(stringa):
    previous = stringa[0]
    for i in range(1, len(stringa)):
        if previous == stringa[i]:
            return True
        previous = stringa[i]
    return False

main()

