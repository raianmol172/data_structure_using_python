from sys import maxsize


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, data):
    stack.append(data)
    print(data, "pushed to stack")


def pop(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)

    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    else:
        return stack[len(stack) - 1]


stack = createStack()
push(stack, 10)
push(stack, 20)
push(stack, 30)
print(stack)
pop(stack)
print(stack)
print(peek(stack))
print(isEmpty(stack))