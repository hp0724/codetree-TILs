month_day = [31,29,31,30,31,30,31,31,30,31,30,31]
day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1,d1,m2,d2 = map(int,input().split())
input_day_of_the_week = input()

result_idx = day_of_the_week.index(input_day_of_the_week)
print(result_idx)

# # 월요일 부터 입력 요일 까지 값 빼고 
# # 일주일 나누기 
# count = 0
# diff = (sum(month_day[:m2]) + d2) - (sum(month_day[:m1]) + d1)
# if diff - result_idx >= 0:
#     diff -= result_idx 
#     count += 1
#     if diff >= 7:
#         count += (diff // 7)

# print(count)