a,b,c = map(int,input().split())
if a<=11 and b<=11 and c<11 :
    print(-1)
before_day = 11
before_hour = 11
before_min = 11 
time = 0
while True:
    if before_day == a and before_hour == b and before_min == c :
        break 
    time +=1 
    before_min += 1 
    if before_min > 60:
        before_min = 1
        before_hour +=1  
        if before_hour> 23:
            before_day += 1
            before_hour = 0

print(time)