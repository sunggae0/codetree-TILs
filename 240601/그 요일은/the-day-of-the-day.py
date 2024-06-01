import datetime

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
A = input().strip()

# 요일 매핑
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
weekday_index = weekdays.index(A)

# 시작 날짜와 끝 날짜 설정
start_date = datetime.date(2024, m1, d1)
end_date = datetime.date(2024, m2, d2)

# A 요일이 몇 번 등장하는지 세기
count = 0
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() == weekday_index:
        count += 1
    current_date += datetime.timedelta(days=1)

# 결과 출력
print(count)