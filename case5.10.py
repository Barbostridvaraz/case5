i = str(input())
seen = ""
p = 0
for c in i:
    if c not in seen:
        seen += c
        if i.count(c)>1:
            p +=1
if len(i) == 4  and p == 0 and ((2051 < int(i)) or (int(i) < 1899)):
    print("OK")
else:
    print("ERROR")
