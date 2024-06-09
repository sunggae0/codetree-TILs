def refresh_list(arr,move):
    result = [[] for _ in range(move)] + arr
    return result

def count(var,arr):
    cnt=0
    for i in arr:
        if i == var:
            cnt+=1
    return cnt




n = int(input())
arr=[[]]
offset = 0
pos=0
color=1
for i in range(n):
    x,comm = input().split()
    x=int(x)

    if comm=='R':
        temp = [pos,pos+x]
        color=1
        if pos+x+1>len(arr):
            for j in range(pos+x-len(arr)):
                arr.append([])
        pos+=x-1
    elif comm=='L':
        temp = [pos-x+1,pos+1]
        color=0
        pos-=x-1
    
    if pos<0:
        move = pos*(-1)
        offset += move
        pos=0
        temp = [0,temp[1]+move]
        arr = refresh_list(arr,move)
    for j in range(temp[0],temp[1]):
        if len(arr[j]) > 0:
            if arr[j][-1] != 2:
                arr[j].append(color) #1 = black, 0 = white, 2 = gray
                if count(0,arr[j])>=2 and count(1,arr[j])>=2:
                    arr[j].append(2)
        else:
            arr[j].append(color) #1 = black, 0 = white, 2 = gray

cnt=[0,0,0]
for i in arr:
    cnt[i[-1]]+=1
print(*cnt,sep=' ')