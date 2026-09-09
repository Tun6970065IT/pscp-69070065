"""card"""
def poker():
    """card"""
    card = input().strip().upper()

    p = card[:-1]
    g = card[-1]

    if p == "A":
        p = "ace"
    elif p =="J":
        p = "jack"
    elif p == "Q":
        p = "queen"
    elif p == "K":
        p = "king"

    if g == "D":
        g = "diamonds"
    elif g == "H":
        g =  "hearts"
    elif g == "S":
        g = "spades"
    elif g == "C":
        g = "clubs"

    print(f"{p} of {g}")
poker()
