def judge(t):
    for i in t:
        if i!=t[0]:
            return True
    return False

a = input()

print('Yes') if judge(a) else print('No')