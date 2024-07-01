m1,d1,m2,d2 = map(int,input().split())
 
elapsed_days = 0 

num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    if month == m2 and day == d2:
        break 
    
    elapsed_days += 1 
    d1 += 1 
    if day > num_of_days[month]:
        m1 += 1 
        d1 = 1