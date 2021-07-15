#변수
memory = []
dataAray = ['다현','정연','쯔위','사나','지효']
pre, heat, current = None,None,None

#함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    print(current.data,end=" ")
    while current.link != None:
        current = current.link
        print(current.data,end=" ")
    print()
def insertNode(find,insert):
    #첫 노드 앞에 삽입
    global pre, head, current, memory
    if find == head.data:
        node = Node()
        node.data = insert
        node.link = head
        head = node
        return
    #다른 노드 앞에 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if find == current.data:
            node = Node()
            node.data = insert
            node.link = current
            pre.link = node
            return
    node = Node()
    node.data = insert
    current.link = node
    return
def delNode(data):
    global pre, heat, current, memory
    current = head
    pre = current
    if data == current.data:
        pre.link = current.link
        del(current)


node = Node()
node.data = dataAray[0]
head = node
memory.append(node)

for datas in dataAray[1:]:
    pre = node
    node = Node()
    node.data = datas
    pre.link = node
    memory.append(datas)

printNode(head)
insertNode(0,'기용')



printNode(head)