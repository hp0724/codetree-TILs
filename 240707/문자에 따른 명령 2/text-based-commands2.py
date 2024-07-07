x = 0 
y = 0 

direction = [[0,-1],[1,0],[0,1],[-1,0]]
cmd = list(input())
idx = 0 

for c in cmd:
    if c == "L":
        idx -= 1 
        if idx < 0 :
            idx += 4 
    elif c == "R":
        idx += 1 
        if idx > 3 :
            idx -= 4 
        
    elif c == "F":
        x += direction[idx][0]
        y += direction[idx][1]

print(x,y)