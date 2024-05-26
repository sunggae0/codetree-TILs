class std():
    def __init__(self,height,weight,num):
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())
arr = [std(*list(map(int,input().split())),i+1) for i in range(n)]

arr.sort(key = lambda x: (-x.height,-x.weight,x.num))

for i in arr:
    print(i.height, i.weight, i.num)