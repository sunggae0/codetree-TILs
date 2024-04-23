def mult5(n):
    return n%2==0 and n%5==0

n = int(input())
if mult5(n):
    print('Yes')
else:
    print('No')