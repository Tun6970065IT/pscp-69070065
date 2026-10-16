"""Demon hunter"""

def main():
    """Demon hunter"""
    Demons = [
    ("Spider Demon", 1),
    ("Swamp Demon", 2),
    ("Arrow Demon", 1),
    ("Hand Demon", 2),
    ("Drum Demon", 3),
    ("Mugen Train", 2),
    ("Upper Moon", 3)
    ]

    kills = 0
    attacks = 0
    i = 0
    while kills < 5:
        name , num = Demons[i % 7]
        print(name)

        success = False

        for _ in range(3):
            a = int(input())
            attacks += 1

            if a == num:
                print("kill")
                kills += 1
                success = True
                break

        if not success:
            print("back")

        i += 1

    print(attacks)

main()
