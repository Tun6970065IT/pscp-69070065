"""HorizontalHistogram"""

def main():
    """HorizontalHistogram"""
    text = input()

    lower_char = [chr(i) for i in range(ord("a") , ord("z") + 1)]
    upper_char = [chr(i) for i in range(ord("A") , ord("Z") + 1)]
    allchar = lower_char + upper_char

    for char in  allchar:
        count = text.count(char)
        if count > 0:
            chart_bar = ""
            for j in range(1 , count + 1):
                chart_bar += "-"
                if not j % 5 and j < count:
                    chart_bar += "|"
            print(f"{char} : {chart_bar}")

main()
