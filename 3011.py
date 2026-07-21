"""docstring"""

def main():
    """color"""
    C1 = input()
    C2 = input()
    if C1 == "Red" and C2 == "Yellow":
        print("Orange")
    elif C1 == "Red" and C2 == "Blue":
        print("Violet")
    elif C1 == "Yellow" and C2 == "Blue":
        print("Green")
    elif C1 == "Yellow" and C2 == "Red":
        print("Orange")
    elif C1 == "Blue" and C2 == "Red":
        print("Violet")
    elif C1 == "Blue" and C2 == "Yellow":
        print("Green")
    elif C1 == "Red" and C2 == "Red":
        print("Red")
    elif C1 == "Yellow" and C2 == "Yellow":
        print("Yellow")
    elif C1 == "Blue" and C2 == "Blue":
        print("Blue")
    else:
        print ("Error")

main()
