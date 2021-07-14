katok = ['다현', '정연', '쯔위', '사나', '지효','모모']

def insertData(position,name):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = name
insertData(3,'안기용')
print(katok)