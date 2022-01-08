def main():
    n = int(input())
    t = input()
    
    chars = set(t)
    frequences = dict()
    
    # Creation of a dictionary that stores every group of frequence
    for c in chars:
        counter = 0
        for s in t:
            if s == c: counter += 1
        if str(counter) in frequences:
            l = list(frequences[str(counter)])
            l.append(c)
            frequences[str(counter)] = l
        else:
            frequences[str(counter)] = list(c)
    
    for lenght in frequences:
        frequences[lenght] = sorted(frequences[lenght])
    
    
    # Find the changes
    changes = []
    for keys in frequences:
        group = frequences[keys]
        medium = len(group)//2
        
        for i in range(medium):
            
            changes.append((group[i], group[len(group)-1-i]))
            changes.append((group[len(group)-1-i], group[i]))
        if len(group) == 1: changes.append((group[0], group[0]))
        elif len(group) % 2 != 0: changes.append((group[len(group)//2], group[len(group)//2]))
    
    
    # Reverse
    t1 = ""
    for c in t:
        for change in changes:
            if c == change[0]:
                t1 = t1 + change[1]
                break
            
    print(t1)
    
    
main()
    