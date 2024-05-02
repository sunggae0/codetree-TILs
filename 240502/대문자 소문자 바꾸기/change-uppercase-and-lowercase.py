t = input()
for i in t:
    if 65<=ord(i)<=90:
        print(chr(ord(i)+32),end='')
    else:
        print(chr(ord(i)-32),end='')