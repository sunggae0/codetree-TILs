def find_meeting_time(N, M, movements_A, movements_B):
    # Initialize positions and times
    position_A = 0
    position_B = 0
    time = 0
    time_index_A = 0
    time_index_B = 0
    
    # Prepare to iterate over the movements
    movements_A.append(('R', 0))  # Sentinel to avoid index error
    movements_B.append(('R', 0))  # Sentinel to avoid index error
    
    current_move_A = movements_A[0]
    current_move_B = movements_B[0]
    direction_A = 1 if current_move_A[0] == 'R' else -1
    direction_B = 1 if current_move_B[0] == 'R' else -1
    
    remaining_time_A = current_move_A[1]
    remaining_time_B = current_move_B[1]
    
    # Iterate until the total time
    total_time = sum([t for _, t in movements_A])  # or movements_B since they are the same
    
    for t in range(1, total_time + 1):
        if remaining_time_A == 0:
            time_index_A += 1
            current_move_A = movements_A[time_index_A]
            direction_A = 1 if current_move_A[0] == 'R' else -1
            remaining_time_A = current_move_A[1]
        
        if remaining_time_B == 0:
            time_index_B += 1
            current_move_B = movements_B[time_index_B]
            direction_B = 1 if current_move_B[0] == 'R' else -1
            remaining_time_B = current_move_B[1]
        
        # Move A and B
        position_A += direction_A
        position_B += direction_B
        
        # Decrement the remaining times
        remaining_time_A -= 1
        remaining_time_B -= 1
        
        # Check if they meet
        if position_A == position_B:
            return t
    
    # If they never meet
    return -1

# Example usage
N,M=map(int,input().split())

movements_A = []
movements_B = []
for i in range(N):
    movements_A.append(tuple(input().split()))
    movements_A[i][1] = int(movements_A[i][1])
for i in range(M):
    movements_B.append(tuple(input().split()))
    movements_B[i][1] = int(movements_B[i][1])


print(find_meeting_time(N, M, movements_A, movements_B))  # Output: 12