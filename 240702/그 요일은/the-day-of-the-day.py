# 연도별 월의 일수를 리스트로 저장 (2024년은 윤년)
month_day = [0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 요일 목록
day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
input_day_of_the_week = input()

# 입력된 요일의 인덱스를 구함
target_day_index = day_of_the_week.index(input_day_of_the_week)

# 입력된 시작 날짜가 해당 년도의 몇 번째 일인지 계산
def day_of_year(month, day):
    return sum(month_day[1:month]) + day

start_day = day_of_year(m1, d1)
end_day = day_of_year(m2, d2)

# 시작 요일의 인덱스 구하기 (m1월 d1일이 월요일일 때의 요일 계산)
start_weekday_index = 0  # 월요일을 기준으로 0

# 입력된 요일이 처음으로 나타나는 날짜 계산
first_target_day = start_day + target_day_index

# 요일 카운트
count = 0
if first_target_day <= end_day:
    count = 1 + (end_day - first_target_day) // 7

# 결과 출력
print(count)