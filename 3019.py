"""docstring"""

def main():
    """safepass"""
    word = input()
    num = int(input())
    if word == "H" and num == 4567:
        print("safe unlocked")
    elif word == "H" and num != 4567:
        print("safe locked - change digit")
    elif word != "H" and num == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")

main()
