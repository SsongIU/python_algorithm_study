from collections import deque

import numpy as np

data = deque(np.random.randint(-100, 100, size=100000))


def solution(data):
    result = deque()
    while len(data):
        result.append(data.pop())
    result.remove(0)
    while result:
        a = 0
        b = result.pop()
        a += b
    return a


print(solution(data))
