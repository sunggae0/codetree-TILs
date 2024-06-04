def max_overlap(n, segments):
    events = []
    
    # 이벤트 리스트 생성 (시작점은 1, 끝점은 -1)
    for x1, x2 in segments:
        events.append((x1, 1))
        events.append((x2, -1))
    
    # 이벤트를 x 좌표 기준으로 정렬 (x가 같으면 끝점이 먼저 오도록 정렬)
    events.sort(key=lambda x: (x[0], x[1]))
    
    max_overlap_count = 0
    current_overlap_count = 0
    
    # 이벤트를 순회하면서 겹치는 선분의 수를 계산
    for event in events:
        current_overlap_count += event[1]
        if current_overlap_count > max_overlap_count:
            max_overlap_count = current_overlap_count
    
    return max_overlap_count

# 입력 받기
n = int(input().strip())
segments = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 결과 출력
print(max_overlap(n, segments))