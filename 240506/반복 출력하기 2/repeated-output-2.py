def printHello(n):
    if n == 0:
        return
    
    printHello(n-1)
    print('HelloWorld')


printHello(4)