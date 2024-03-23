N,i,j = [int(i) for i in input().split()]
print(max(N,i,j),(N+i+j)-min(N,i,j)-max(N,i,j),min(N,i,j))