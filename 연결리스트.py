class Node():
    def __init__(self):
        self.data = None
        self.link = None
node1 = Node()
node1.data = '다현'


node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '선화'
node2.link = node3

node4 = Node()
node4.data = '효성'
node3.link = node4

new_node = Node()
new_node.data = '기용'
new_node.link = node1.link
node1.link = new_node

node2.link = node3.link
del(node3)

current = node1
print(current.data,end=" ")
while current.link != None:
    current = current.link
    print(current.data,end=" ")



