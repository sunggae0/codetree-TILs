def func1(n):
    if n == 0:
        return
    func1(n-1)
    print(n,end=' ')

def func2(n):
    if n== 0:
        return
    print(n,end = ' ')
    func2(n-1)


n = int(input())

func1(n)
print()
func2(n)