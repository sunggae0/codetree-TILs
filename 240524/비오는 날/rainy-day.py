class data():
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

def select_date(arr):
    minn = 0
    for i in range(len(arr)):
        if arr[minn].date > arr[i].date:
            minn = i
    return minn

n = int(input())
arr = [data(*input().split()) for _ in range(n)]

state = ''
while True:
    picked = arr[select_date(arr)]
    if picked.weather == 'Rain':
        print(picked.date,picked.day,picked.weather)
        break
    else:
        del arr[select_date(arr)]