"""card"""
def poker():
    """card"""
    card = input().strip().upper()

    p = card[:-1]
    g = card[-1]

    if p == "A":
        p = "Ace"
    elif p =="J":
        p = "Jack"
    elif p == "Q":
        p = "Queen"
    elif p == "K":
        p = "King"

    if g == "D":
        g = "Diamonds"
    elif g == "H":
        g =  "Hearts"
    elif g == "S":
        g = "Spades"
    elif g == "C":
        g = "Clubs"

    print(f"{p} of {g}")
poker()
