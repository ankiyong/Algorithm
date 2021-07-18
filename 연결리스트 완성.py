#변수
memory =[]
dataArray = ['아이유','선미','청하','전효성','츄','현아']
pre, head, current = None,None,None
select = -1
#함수
class Node():
    def __init__(self):
        self.data =None
        self.link = None
def printData(start):
    current = start
    print(current.data,end=" ")
    while current.link != None:
        current = current.link
        print(current.data,end=" ")
    print()
def insertData(find,insert):
    global pre, head, current, memory
    #첫 노드
    if head.data == find:
        node = Node()
        node.data = insert
        node.link = head
        head = node
        return
    #그 외 노드
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == find:
            node = Node()
            node.data = insert
            node.link = pre.link
            pre.link = node
            return
    node = Node()
    node.data = insert
    current.link = node
def delData(deldata):
    global pre, head, current, memory
    if head.data == deldata:
        current = head
        head = head.link
        del(current)
        return
    #그외노드삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deldata:

            pre.link = current.link
            del(current)
            return
    return

node = Node()
node.data = dataArray[0]
head =node
memory.append(node)
for data in dataArray[1:]:
    pre = node
    node =Node()
    node.data = data
    pre.link = node
    memory.append(node)

while select != 3:
    select = int(input('숫자 입력 : '))
    if select == 1:
        find = input('이름 : ')
        name = input("이름 : ")
        insertData(find,name)

    elif select == 2:
        deldata = input('이름')
        delData(deldata)
    elif select == 3:
        pass

    else:
        print('1~3까지 입력 ! ')
    printData(head)