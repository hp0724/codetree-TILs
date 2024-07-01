# 첫 번째 줄에 m1, d1, m2, d2가 공백을 사이에 두고 주어집니다.
m1,d1,m2,d2 = map(int,input().split())
month_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day_string = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]

diff = (sum(month_day[0:m2]) + d2) - (sum(month_day[0:m1]) + d1)
# print(diff)
if diff < 0 :
    while diff > 0:
        diff += 7 
    diff %= 7 
else:
    diff %= 7 

print(day_string[diff])