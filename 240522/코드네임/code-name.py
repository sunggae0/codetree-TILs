class p():
    def __init__(self,code,point):
        self.code = code
        self.point = point
    
arr = [p(*(input().split())) for _ in range(5)]

minn = 0
result = 0
for i in range(5):
    pt = int(arr[i].point)
    if i!= 0:
        if pt < minn:
            minn = pt
            result = i
    else:
        minn = pt
    
print(arr[result].code, arr[result].point)