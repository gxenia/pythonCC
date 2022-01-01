def main():
    
    # Ask for the input
    n, m = list(map(int, input().split()))
    card = []
    for _ in range(n):
        card.append(list(input()))
    pad = []
    for _ in range(m):
        pad.append(list(input()))
    
    card90 = rotate(n, card)
    card180 = rotate(n, card90)
    card270 = rotate(n, card180)
    
    match = []
    
    for row in range(m):
        for coloumn in range(m):
            sub = []
            if row + n <= m and coloumn + n <= m:
                for j in range(n):
                    subRow = pad[row+j][coloumn:coloumn+n]
                    sub.append(subRow)
                    
            if sub == card90:
                match.append((row, coloumn, 90))
            elif sub == card180:
                match.append((row, coloumn, 180))
            elif sub == card270:
                match.append((row, coloumn, 270))
    
    #print(match)
    if len(match) == 0: print("err")
    else:
        values = [n, n, 270]
        for i in range(len(match)) :
            if match[i][0] == values[0] and match[i][1] == values[1] :
                if match[i][2] < values[2] :
                    values[0] = match[i][0]
                    values[1] = match[i][1]
                    values[2] = match[i][2]       

            if match[i][0] < values[0] and match[i][1] < values[1] :
                values[0] = match[i][0]
                values[1] = match[i][1]
                values[2] = match[i][2]
        print(*values, sep = " ")
            


def rotate(n, card):
    newCard= []
    for coloumn in range(n):
        newRow = []
        for row in range(n-1, -1, -1):
            newRow.append(card[row][coloumn])
        newCard.append(newRow)
    return newCard
    
main()