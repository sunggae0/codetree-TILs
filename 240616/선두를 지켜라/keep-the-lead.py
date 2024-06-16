def find_lead_changes(N, M, A_moves, B_moves):
    # 각 사람의 이동 로그를 통해 누적 거리를 계산
    A_distance = []
    B_distance = []

    A_current_distance = 0
    for v, t in A_moves:
        for _ in range(t):
            A_current_distance += v
            A_distance.append(A_current_distance)
    
    B_current_distance = 0
    for v, t in B_moves:
        for _ in range(t):
            B_current_distance += v
            B_distance.append(B_current_distance)

    # 선두 변경 횟수를 계산
    lead_changes = 0
    current_lead = None
    
    for a, b in zip(A_distance, B_distance):
        if a > b:
            new_lead = 'A'
        elif b > a:
            new_lead = 'B'
        else:
            new_lead = 'Tied'
        
        if new_lead != current_lead and new_lead != 'Tied':
            if current_lead is not None:
                lead_changes += 1
            current_lead = new_lead
    
    return lead_changes

# 입력 받기
N, M = map(int, input().split())
A_moves = [tuple(map(int, input().split())) for _ in range(N)]
B_moves = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 출력
print(find_lead_changes(N, M, A_moves, B_moves))