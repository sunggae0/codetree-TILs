class boom():
    def __init__(self,code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

arr = input().split()

b1 = boom(*arr)
print('code :',b1.code)
print('color :', b1.color)
print('second :',b1.sec)