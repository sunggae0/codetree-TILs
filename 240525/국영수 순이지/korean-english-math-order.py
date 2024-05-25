class st():
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
arr = [st(*input().split()) for _ in range(n)]

arr.sort(key = lambda x:(-1*int(x.kor),-1*int(x.eng),-1*int(x.math)))

for i in arr:
    print(i.name,i.kor,i.eng,i.math)