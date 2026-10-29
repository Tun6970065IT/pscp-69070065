"""game"""

def main():
    """game"""
    teamA = int(input())
    teamB = int(input())
    if teamA == 1 and teamB == 1:
        print(1)
    elif teamA == teamB:
        print(0)
    elif not teamA or not teamB:
        print(0)
    elif  teamA // teamB :
        print(teamA // teamB)
    else:
        print("Error")

main()
