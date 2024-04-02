n = int(input())

arr = list(map(float,input().split()))
avr = sum(arr)/len(arr)
print("%.1f"% avr)
print("Good") if avr >= 3.0 else print("Poor")