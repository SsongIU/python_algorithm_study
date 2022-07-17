import queue
from collections import deque

# 리스트를 만들고 pop으로 꺼냄 => stack 방식
listQueue = []
for i in range(5):
    listQueue.append(i)

print(listQueue)
listQueue.pop(0)
print(listQueue)

# 큐 => 한방향 삽입, 삭제
normalQueue = queue.Queue()
for i in range(5):
    normalQueue.put(i)

while normalQueue.qsize():
    print(normalQueue.get())

if normalQueue.empty():
    print("Queue is empty!!", "\n")

# 덱 => 양쪽 방향 가능
dq = deque("1234")
dq.appendleft(0)

while len(dq):
    print(dq[0])
    dq.popleft()
print("\n")

# 덱 파악
dq = deque()
dq = deque("12345")

dq.append(6)
dq.appendleft(0)

removed = dq.pop()
print(removed)
removed = dq.popleft()
print(removed)

print(dq)
dq.rotate(1)
print(dq)
dq.rotate(-2)
print(dq)
