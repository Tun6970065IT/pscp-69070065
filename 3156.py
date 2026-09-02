"""Conan"""

text = input()
skip = int(input())
ans = ""
for _ in text:
    posi = ord(_) - ord("a")
    re_posi = (posi + skip) % 26
    new_ascii = re_posi + ord("a")
    re_char = chr(new_ascii)
    ans += re_char
print(ans)
