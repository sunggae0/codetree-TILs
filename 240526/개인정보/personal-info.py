class std():
    def __init__(self,name,height,weight):
        self.height = height
        self.weight = weight
        self.name = name

arr = [std(*input().split()) for i in range(5)]

temp = sorted(arr, key = lambda x: (x.name))
print('name')
for i in temp:
    print(i.name, i.height, i.weight,)

temp = sorted(arr, key = lambda x: (-int(x.height)))
print('\nheight')
for i in temp:
    print(i.name, i.height, i.weight,)