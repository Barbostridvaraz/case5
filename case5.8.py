i = int(input())
s = i // 29
i = i - s*29
g = s // 17
s = s - g*17
if g > 0:
    print(f"{g} галлеонов")
if s > 0:
    print(f"{s} сиклей")
if i > 0:
    print(f"{i} кнатов")