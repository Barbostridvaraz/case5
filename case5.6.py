p = int(input())
i = int(input())
j = int(input())
if p == i or p == j:
    print("2")
elif p == i and p == j:
    print("3")
else:
    print("1")