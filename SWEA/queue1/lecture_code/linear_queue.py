N = 10
q = [0] * N
front = -1
rear = -1

rear += 1       # enqueue()
q[rear] = 1
rear += 1       # enqueue()
q[rear] = 2
rear += 1       # enqueue()
q[rear] = 3

front += 1      # dequeue()
print(q[front])
front += 1      # dequeue()
print(q[front])
front += 1      # dequeue()
print(q[front])


q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))
print(q2.pop(0))
