"""Resistor"""

def resis():
    """Resistor"""
    digit = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3,
    "Yellow": 4, "Green": 5, "Blue": 6, "Purple": 7,
    "Grey": 8, "White": 9
    }

    multiplier = {
        "Black": 1, "Brown": 10, "Red": 100, "Orange": 1000,
        "Yellow": 10000, "Green": 100000, "Blue": 1000000,
        "Purple": 10000000, "Gold": 0.1, "Silver": 0.01
    }

    tolerance = {
        "Brown": 1, "Red": 2, "Green": 0.5, "Blue": 0.25,
        "Purple": 0.10, "Grey": 0.05, "Gold": 5, "Silver": 10
    }

    c1 = input()
    c2 = input()
    c3 = input()
    c4 = input()
    if c1 not in digit or c2 not in digit or c3 not in multiplier or c4 not in tolerance:
        print("Error")
    else:
        r = (digit[c1] * 10 + digit[c2]) * multiplier[c3]
        t = tolerance[c4] / 100
        ans1 = r * (1-t)
        ans2 = r * (1+t)

        print(f"{ans1:.4f}")
        print(f"{ans2:.4f}")

resis()
