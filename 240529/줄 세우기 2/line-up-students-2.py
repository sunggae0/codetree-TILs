def sort_students():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    students = []

    index = 1
    for i in range(N):
        h = int(data[index])
        w = int(data[index + 1])
        students.append((h, w, i + 1))
        index += 2
    
    # Sort by height first, and by weight in reverse order second
    students.sort(key=lambda x: (x[0], -x[1]))

    for student in students:
        print(student[0], student[1], student[2])

# Test the function with sample input
from io import StringIO
import sys

# Sample input
input_data = """4
1 5
1 7
3 6
1 10
"""

# Redirect stdin to the sample input
sys.stdin = StringIO(input_data)

# Run the function
sort_students()