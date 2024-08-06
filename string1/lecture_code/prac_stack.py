stack = []
stack.append(1)     # push(1)
stack.append(2)     # push(2)
stack.append(3)     # push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())

# stack_algorithm
STACK_SIZE = 10
stack = [0] * STACK_SIZE
top = -1

top += 1    # push(1)
stack[top] = 1
top += 1    # push(2)
stack[top] = 2
top += 1    # push(3)
stack[top] = 3

top -= 1    # pop
print(stack[top+1])
print(stack[top])
top -= 1
print(stack[top])
top -= 1


# stack_2
def f2(c, d):
    return c - d


def f1(a, b):
    c = a + b
    d = 10
    return f2(c, d)


a = 10
b = 20
print(f1(a, b))

