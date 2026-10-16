"""Cuteneko"""

def main():
    """CuteNeko"""
    n = int(input())
    cute = {}
    for _ in range(n):
        nameNcode = input().strip()
        nameNcode = nameNcode.replace("{", "").replace("}", "").replace('"', "").replace("'", "")
        parts = nameNcode.split(":")

        name = parts[0].strip()
        code = parts[1].strip()
        cute[name] = code

    havecat01 = False
    havefox01 = False
    for val in cute.values():
        if val == "Cat01":
            havecat01 = True
        elif val == "Fox01":
            havefox01 = True
    if not havecat01:
        cute["Garfield"] = "Cat01"
    if not havefox01:
        cute["Fubuki"] = "Fox01"

    cats = {}
    foxes = {}
    for name , code in cute.items():
        if code.startswith("Cat"):
            cats[name] = code
        elif code.startswith("Fox"):
            foxes[name] = code
    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")

    sorted_cat = sorted(cats.items() , key=lambda x: x[1])
    for name , code in sorted_cat:
        print(f"{name} : {code}")

    sorted_fox = sorted(foxes.items() , key=lambda x: x[1])
    for name , code in sorted_fox:
        print(f"{name} : {code}")

main()
