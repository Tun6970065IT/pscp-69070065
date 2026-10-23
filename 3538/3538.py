"""B-fullypair"""

def main():
    """B-fullypair"""
    text = input().strip()
    unpair = []
    found = set()
    for char in text:
        if char not in found:
            found.add(char)
            if text.count(char) % 2:
                unpair.append(char)
    if not unpair:
        print("fully paired")
    else:
        print("".join(unpair))

main()
