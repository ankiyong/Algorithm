#변수
size = 5
queue = [None for _ in range(size)]
front,rear = -1,-1

#함수
def isQueueFull():
    global  size, queue, front, rear
    if rear != size-1:
        return False
    elif rear == size-1 and front == -1:
        return True
    else:
        for i in range(front+1,size):
            queue[i-1] = queue[i]
            queue[i] = None
        rear-=1
        front-=1
        return
def isQueueEmpty():
    global size, queue, front, rear
    if front != rear:
        return False
    else:
        return True
def enQueue(data):
    global size, queue, front, rear
    if isQueueFull():
        print('큐 꽉!')
        return None
    rear+=1
    queue[rear] = data
    return
def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        print('큐 텅~')
        return None
    front +=1
    data = queue[front]
    queue[front] = None
    return data

print('출구',queue,'입구')
enQueue('화사')
enQueue('꼬북')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
print('출구',queue,'입구')
retData = deQueue()
print(retData)
print('출구',queue,'입구')
