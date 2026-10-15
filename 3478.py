"""Easy histrogram"""

def main():
    """East histrogram"""
    text = input()
    for char in "abcdefghijklmnopqrstuvwxyz":
        low = text.count(char)
        if low:
            print(f"{char} = {low}")
        up = text.count(char.upper())
        if up:
            print(f"{char.upper()} = {up}")
main()
