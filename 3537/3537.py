"""Impostor"""

def main():
    """imposter"""
    clear_dict = {}
    while True:
        line = input()
        if line == "Start":
            break
        clear = line.replace("{" , "").replace("}" , "").replace('"', "")
        parts = clear.split(":")
        name = parts[0].strip()
        role = parts[1].strip()
        clear_dict[name] = role
    dead_dict = {}
    while True:
        dead = input()
        if dead == "End":
            break
        if dead in clear_dict:
            role = clear_dict.pop(dead)
            dead_dict[dead] = role
    imposter = list(clear_dict.values()).count("Impostor")
    print(f"{imposter} Impostor Remains")
    print("***Alive***")
    for name in sorted(clear_dict):
        print(f"{name} : {clear_dict[name]}")
    print("***Dead***")
    for name in sorted(dead_dict):
        print(f"{name} : {dead_dict[name]}")

main()
