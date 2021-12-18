def moveBack(i, expression):
    for index in range(i-1, len(expression)-2):
        expression[index] = expression[index+2]
    expression[-2] = 0
    expression[-1] = 0
    
    return expression

def nZeros(expression):
    zeros = 0
    for i in range(len(expression)):
        if expression[i] == 0:
            zeros += 1
    return zeros    
        

n = int(input())
expression = input().split()
i = 0

while nZeros(expression) != n - 1:
    
    if expression[i] == "+":
        expression[i-2] = (int(expression[i-2])+int(expression[i-1]))
        expression = moveBack(i, expression)
        i-= 2
        
    elif expression[i] == "-":
        expression[i-2] = (int(expression[i-2])-int(expression[i-1]))
        expression = moveBack(i, expression)
        i-= 2
        
    elif expression[i] == "*":
        expression[i-2] = (int(expression[i-2])*int(expression[i-1]))
        expression = moveBack(i, expression)
        i-= 2
        
    i += 1
        
print(expression[0])