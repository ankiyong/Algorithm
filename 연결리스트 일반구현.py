class Node():
    def __init__(self):
        self.data = None
        self.link = None
memory = []
head, pre, current = None,None,None

node = Node()
node.data = input('이름입력')
head = node
memory.append(node)

pre = current
node = Node()
node.data = input('입력 : ')
p

