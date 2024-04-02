n = int(input())

arr = list(map(float,input().split()))
avr = sum(arr)/len(arr)
print("%.1f"% avr)
if avr >= 4.0:
    print("Perfect") 
elif avr >= 3.0:
    print("Good")
else:
    print("Poor")