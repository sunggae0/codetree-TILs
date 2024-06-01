def days_since_start_of_year(month, day):
    """1월 1일부터 해당 월의 날짜까지의 총 일수를 계산하는 함수"""
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    for i in range(1, month):
        total_days += month_days[i]
    total_days += day - 1
    return total_days

def count_specific_weekday(m1, d1, m2, d2, start_day, target_day):
    """특정 요일의 빈도를 계산하는 함수"""
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    start_idx = weekdays.index(start_day)
    target_idx = weekdays.index(target_day)

    # 시작 날짜의 요일 계산
    start_days = days_since_start_of_year(m1, d1)
    start_weekday = (start_days + start_idx) % 7

    # 끝 날짜의 요일 계산
    end_days = days_since_start_of_year(m2, d2)
    end_weekday = (end_days + start_idx) % 7

    # 특정 요일의 빈도 계산
    count = 0
    for day_count in range(start_days, end_days + 1):
        if (day_count % 7) == target_idx:
            count += 1
    
    return count

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
start_day = input().strip()

# 결과 출력
result = count_specific_weekday(m1, d1, m2, d2, start_day, start_day)
print(result)