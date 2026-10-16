"""FourDirections"""
def four():
    """FourDirections"""
    arrows = {
        'U': ["  *  ",
            " *** ",
            "* * *",
            "  *  ",
            "  *  "],
        'D': ["  *  ",
            "  *  ",
            "* * *",
            " *** ",
            "  *  "],
        'L': ["  *  ",
            " *   ",
            "*****",
            " *   ",
            "  *  "],
        'R': ["  *  ",
            "   * ",
            "*****",
            "   * ",
            "  *  "],
    }

    direction = input().strip()
    for row in range(5):
        line = ""
        for c in direction:
            line += arrows[c][row] + " "
        print(line)

four()
