"""filter"""

def main():
    """filter"""
    dict_str = input()
    need = float(input())
    student = dict_str.replace('{', '').replace('}', '').strip()

    filtered = []
    if student:
        for i in student.split(","):
            uid_raw , score_raw = i.split(":")

            uid = uid_raw.strip().strip("'").strip('"')
            score = float(score_raw.strip())
            if score >= need:
                filtered.append((uid , score))
    if not filtered:
        print("Nope")
    else:
        filtered.sort()
        for uid , score in filtered:
            print(f"{uid}\t{score:.2f}")

main()
