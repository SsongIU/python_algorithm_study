from collections import deque


def solution():
    data = deque()
    while True:
        d = input("데이터 입력(나가기:q): ")

        try:
            data.append(int(d))
        except ValueError:
            data.append(0)

        if d == "q" or d == "Q":
            break

    try:
        data.remove(0)
    except Exception:
        pass

    total = 0
    while len(data):
        total += data.pop()

    return total


print(solution())
