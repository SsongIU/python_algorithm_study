from collections import deque


def solution(num):
    card_deck = deque()

    for i in range(1, num + 1):
        card_deck.append(i)

    for j in range(num - 1):
        card_deck.popleft()
        card_deck.rotate(-1)

    return card_deck[0]


print(solution(50000))
