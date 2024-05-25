class p():
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = [p(*input().split()) for _ in range(n)]

arr.sort(lambda x: x.height)

for i in arr:
    print(i.name,i.height,i.weight)