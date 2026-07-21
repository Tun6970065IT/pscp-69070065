"""docstring"""

def main():
    """elo"""
    ra = int(input())
    rb = int(input())
    string = input()

    if string == "A":
        Ea = 1 / (1+10 ** ((rb - ra)/400))
        print(f"{Ea:.2f}")
    if string == "B":
        Eb = 1 / (1+10 ** ((ra - rb)/400))
        print(f"{Eb:.2f}")

main()
