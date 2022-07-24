from collections import deque


def solution():
    k = int(input())
    result_list = deque()

    for i in range(k):
        num = int(input())
        if num == 0:
            result_list.pop()
        else:
            result_list.append(num)

    result = 0

    while len(result_list):
        add = result_list.popleft()
        result += add

    print(result)


solution()
