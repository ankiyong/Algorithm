friend = ['다현', '정연', '쯔위', '안기용', '사나', '지효', '모모']

def delData(position):
    friend[position] = None
    fLen = len(friend)
    for i in range(position,fLen-1):
        friend[i] = friend[i+1]
        friend[i+1] = None
    del(friend[fLen-1])
delData(3)
print(friend)