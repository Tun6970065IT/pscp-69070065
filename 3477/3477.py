"""Pad Thai"""
def main():
    """Pad Thai"""
    ingredients = set()
    while True:
        item = input()
        if item == "Cook":
            break
        ingredients.add(item)

    tastes = set()
    while True:
        taste = input()
        if taste == "End":
            break
        tastes.add(taste)

    need = {
        "Pad Thai Sauce",
        "Tofu",
        "Pickle Turnip",
        "Shrimp",
        "Bean Sprouts",
        "Noodle",
        "Chives",
        "Lime",
        "Egg",
        "Oil",
        "Peanuts"
    }

    tastes_need = {"Sweet", "Sour", "Salty"}

    if ingredients - need:
        print("This is not Pad Thai!!!")
    elif ingredients != need:
        print("This is bad!")
    elif tastes == tastes_need:
        print("Delicious!")
    else:
        print("Not Bad...")

main()
