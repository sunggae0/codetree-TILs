class dot():
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num

n = int(input())
arr = [dot(*list(map(int,input().split())),i+1) for i in range(n)]

arr.sort(key = lambda x: (abs(x.x) + abs(x.y), x.num))

for i in arr:
    print(i.num)