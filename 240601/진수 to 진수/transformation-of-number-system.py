# 입력 받기
a, b = map(int, input().split())
n = input().strip()

# a진수 수를 10진수로 변환
decimal_value = int(n, a)

# 10진수 수를 b진수로 변환
def decimal_to_base(decimal_value, base):
    if decimal_value == 0:
        return "0"
    digits = []
    while decimal_value:
        digits.append(int(decimal_value % base))
        decimal_value //= base
    digits.reverse()
    return ''.join(str(digit) for digit in digits)

# 결과 출력
print(decimal_to_base(decimal_value, b))