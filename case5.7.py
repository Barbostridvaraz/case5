
N,i,j = [int(i) for i in input().split()]
m = min((j - i)%N, (i - j)%N) - 1
print(m)