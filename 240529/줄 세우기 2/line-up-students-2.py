class Student:
    def __init__(self, height, weight, id):
        self.height = height
        self.weight = weight
        self.id = id

    def __repr__(self):
        return f"{self.height} {self.weight} {self.id}"

def sort_students(student_data):
    students = []
    
    # 학생 정보 객체를 생성하고 리스트에 추가
    for i, (h, w) in enumerate(student_data):
        students.append(Student(h, w, i + 1))
    
    # 정렬: 키 오름차순, 몸무게 내림차순
    students.sort(key=lambda student: (student.height, -student.weight))
    
    # 정렬된 학생 정보 출력
    for student in students:
        print(student)

# 입력 데이터: 각 튜플은 (키, 몸무게)를 나타냄
n = int(input())
input_data = [tuple(map(int,input().split())) for _ in range(n)]

# 함수 실행
sort_students(input_data)