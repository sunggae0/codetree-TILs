class p():
    def __init__(self,code,point):
        self.code = code
        self.point = point
    
arr = [p(*(input().split())) for _ in range(5)]

minn = 0
result = 0
for i in range(5):
    pt = int(arr[i].point)
    if pt < minn and i!=0:
        minn = pt
        result = i
    
print(arr[minn].code, arr[minn].point)