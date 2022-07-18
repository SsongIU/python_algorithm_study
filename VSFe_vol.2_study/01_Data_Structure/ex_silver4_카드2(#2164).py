from collections import deque

a = int(input("숫자 입력: "))


def solution(num):
    card_deck = deque([i for i in range(1, num + 1)])

    for j in range(num - 1):
        card_deck.popleft()
        card_deck.rotate(-1)

    return card_deck[0]


print(solution(a))
