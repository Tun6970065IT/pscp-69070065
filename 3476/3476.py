"""Cuteneko"""

import json

def main():
    """CuteNeko"""
    n = int(input())
    cat01 = {}
    fox01 = {}
    for _ in range(n):
        catsfoxs = json.loads(input())
        for name, code in catsfoxs.items():
            if code.startswith("Cat"):
                cat01[name] = code
            elif code.startswith("Fox"):
                fox01[name] = code
    if "Cat01" not in cat01.values():
        cat01["Garfield"] = "Cat01"
    if "Fox01" not in fox01.values():
        fox01["Fubuki"] = "Fox01"
    sorted_cats = [(code , name) for name , code in cat01.items()]
    sorted_foxes = [(code , name) for name , code in fox01.items()]
    sorted_cats.sort()
    sorted_foxes.sort()
    print(f"Cat : {len(cat01)}")
    print(f"Fox : {len(fox01)}")

    for code , name in sorted_cats:
        print(f"{name} : {code}")
    for code , name in sorted_foxes:
        print(f"{name} : {code}")

main()
