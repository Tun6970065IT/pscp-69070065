"""cal"""

def calo():
    """calo"""
    total_cal = 0
    while True:
        fruits = input()
        if fruits == "1":
            total_cal += 100
        elif fruits == "2":
            total_cal += 120
        elif fruits == "3" :
            total_cal += 200
        elif fruits == "4":
            total_cal += 60
        elif fruits == "5":
            break
    print("Bye Bye")
    print(f"Total Calories: {total_cal}")

calo()
