class player():
    def __init__(self, username='codetree',lv=10):
        self.name = username
        self.lv = lv
n,lv = input().split()
p1 = player()
p2 = player(n,lv)

print('user',p1.name,'lv',p1.lv)
print('user',p2.name,'lv',p2.lv)