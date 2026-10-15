"""Muddled Menu"""

def main():
    """Muddled Menu"""
    menu = []
    while True:
        text = input()
        if text == "DONE":
            break
        if text == "CLOSED":
            menu = []
            break
        if text == "SOMETHING'S WRONG":
            menu = []
        elif text.startswith("Can't do: "):
            remove_Food = text[len("Can't do: "):]
            if remove_Food in menu:
                menu.remove(remove_Food)
        else:
            cos = ""
            food_name = ""
            true_food = text.rsplit(" #",1)
            if len(true_food) == 2:
                food_name = true_food[0]
                cos = true_food[1]
            if cos == "N":
                menu.append(food_name)
            else:
                index = int(cos) - 1
                menu.insert(index , food_name)
    reversed_menu = list(reversed(menu))
    print(f"Full Course: {menu} Reversed: {reversed_menu}")

main()
