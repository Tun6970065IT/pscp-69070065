"""filter"""

def main():
    """filter"""
    emp_dict = {}
    bigdict = input()
    clear = bigdict.replace("{" , "").replace("}" , "").replace('"', "").replace(":" , "")
    parts = clear.split(", ")
    num = parts[0].strip()
    score = parts[1].strip()
    emp_dict[num] = score
    print(emp_dict)

main()
