#변수
size = 5
stack = [None for _ in range(size)]
top = -1

#함수
def isStackFull():
    global size, stack, top
    if top == size-1:
        print('스택 꽉!')
        return True
    else:
        return False
def push(data):
    global size, stack, top
    if isStackFull():
        return None
    top+=1
    stack[top] = data
def isStackEmpty():
    global stack,size,top
    if top == -1:
        print('큐 텅~')
        return True
    else:
        return False
def pop():
    global size, stack, top
    if isStackEmpty():
        return None
    else:
        data = stack[top]
        stack[top] = None
        top-=1
        return data
push('커피')
push('커피1')
push('커피2')
push('커피3')
push('커피4')
print(stack)
data = pop()
print(data)
data = pop()
print(data)
data = pop()
print(data)
data = pop()
print(data)