def refresh_list(arr,move):
    result = [0 for _ in range(move)] + arr
    return result

n = int(input())
arr=[]
offset = 0
pos=0
for i in range(n):
    x,comm = input().split()
    x=int(x)

    if comm=='R':
        temp = [pos,pos+x]
        for j in range(x):
            arr.append(0)
        pos+=x
    elif comm=='L':
        temp = [pos-x,pos]
        pos-=x
    
    if pos<0:
        move = pos*(-1)
        offset += move
        pos=0
        temp = [0,x]
        arr = refresh_list(arr,move)
    
    for j in range(temp[0],temp[1]):
        arr[j]+=1

cnt=0
for i in arr:
    if i>=2:
        cnt+=1
print(cnt)