##전역변수
size = 5
queue = [None for _ in range(size)]
front,rear = 0,0


#함수

def isQueueFull():
    global queue, front, rear, size
    if (rear+1)%size == front:
        return True
    else:
        return False
def isQueueEmpty():
    global queue, front, rear, size
    if rear == front:
        return True
    else:
        return False
def enQueue(data):
    global queue, front, rear, size
    if isQueueFull():
        return None
    rear = (rear+1)%size
    queue[rear] = data
def deQueue():
    global queue, front, rear, size
    if isQueueEmpty():
        return None
    front = (front+1) % size
    data = queue[front]
    queue[front] = None
    return data
