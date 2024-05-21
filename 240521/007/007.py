class code:
    def __init__(self,sc, mp, t):
        self.sc = sc
        self.mp = mp
        self.t = t


arr = input().split()
p1 = code(arr[0],arr[1],arr[2])
print('secret code :',p1.sc)
print('meeting point :'p1.mp)
print('time :',p1.t)