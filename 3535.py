"""Classify"""

def main():
    """Classify"""
    rec = {}
    while True:
        uid = input()
        if uid == "END":
            break
        year = uid[0 : 2]
        f = int(uid[2 : 4])
        if year not in rec:
            rec[year] = {}
        if f not in rec[year]:
            rec[year][f] = 0

        rec[year][f] += 1
    sorted_year = sorted(rec.keys())
    for year in sorted_year:
        sorted_f = sorted(rec[year].keys())
        first_year_row = True
        for f in sorted_f:
            count = rec[year][f]

            if first_year_row:
                print(f"{year} {f} {count}")
                first_year_row = False
            else:
                print(f"-- {f} {count}")

main()
