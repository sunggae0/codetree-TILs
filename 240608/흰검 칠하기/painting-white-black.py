def refresh_list(arr,move):
    result = [[] for _ in range(move)] + arr
    return result


def count(var,arr):
    cnt = 0
    for i in arr:
        if i==var:
            cnt+=1
    return cnt



n = int(input())
arr=[]
offset = 0
pos=0
color = 0
for i in range(n):
    x,comm = input().split()
    x=int(x)

    if comm=='R':
        temp = [pos,pos+x]
        for j in range(x):
            arr.append([])
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
        arr[j].append(color%2) #even=black, odd=white
        if count(0,arr[j])>=2 and count(1,arr[j]) >= 2:
            arr[j].append(2) # gray
            
    color+=1

cnt=[0,0,0]
for i in arr:
    if len(i)>0:
        if i[-1] == 2:
            cnt[2]+=1
        elif i[-1] == 1:
            cnt[0]+=1
        else:
            cnt[1]+=1
print(*cnt,sep=' ')