"""มาเป็นทีม"""

def main():
    """มาเป็นทีม"""
    hed = input().split()
    if len(hed) != 2:
        print("Data Incorrect")
        return
    n = int(hed[0])
    m = int(hed[1])
    if not(1 <= n <= 10 and 1<= m <= 20):
        print("Data Incorrect")
        return
    teams = []
    total_score = 0
    for _ in range(n):
        team_score = list(map(int,input().split()))
        if len(team_score) != m:
            print("Data Incorrect")
            return
        for i in team_score:
            if not(0 <= i <= 100):
                print("Data Incorrect")
                return
        teams.append(team_score)

    for j in range(n):
        cur_team = teams[j]
        team_sum = sum(cur_team)
        avg = team_sum / len(cur_team)
        max_score = max(cur_team)
        total_score += team_sum

        print(f"Team {j+1}: Average = {avg:.2f}, Max = {max_score}")

    print(f"Total Score of All Teams = {total_score}")

main()
