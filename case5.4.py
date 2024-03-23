i = int(input())
if i%10 == 1:
    print(f"{i} попугай")
elif (i%10<5) and (i != 1):
    print(f"{i} попугая")
else:
    print(f"{i} попугаев")