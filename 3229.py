"""scoregame"""

def count_score():
    """scoregame"""
    score = int(input())
    bonus = int(input())
    streak = int(input())
    total = 0
    board = 0
    special = 0
    if streak > 3:
        total = (score + bonus) * 1.5
    else:
        total = score + bonus
    if total >= 1500:
        board = 5
    elif total >= 1000:
        board = 4
    elif total >= 500:
        board = 3
    elif total >= 200:
        board = 2
    else:
        board = 1
    if board == 5 and streak >= 7:
        special = 99
    elif board == 4 and bonus > 300:
        special = 88
    else:
        special = 0
    print(int(total))
    print(board)
    print(special)
count_score()
