before_month,before_day,after_month,after_day = map(int,input().split())
 
elapsed_days = 1 
#                1  2  3  4  5  6  7  8  9  10 11 12 
num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    if before_month == after_month and before_day == after_day:
        break 
    
    elapsed_days += 1 
    before_day += 1 

    if before_day > num_of_days[before_month]:
        before_month += 1 
        before_day = 1

print(elapsed_days)