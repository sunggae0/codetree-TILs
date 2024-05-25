def main():
    n = int(input().strip())
    students = []

    for _ in range(n):
        data = input().strip().split()
        name = data[0]
        scores = list(map(int, data[1:]))
        total_score = sum(scores)
        students.append((total_score, name, scores))

    # 총점을 기준으로 정렬
    students.sort()

    # 정렬된 결과 출력
    for student in students:
        print(f"{student[1]} {' '.join(map(str, student[2]))}")

if __name__ == "__main__":
    main()