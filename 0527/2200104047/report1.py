S=[]
for i in range(2,101):
    flag = 0
    for j in range(1,i+1):
        if i%j == 0:
            flag = flag + 1
    if flag==2:
        S.append(i)
S.reverse()

A=[]
B=[]
for i, name in enumerate(S):
    if i == len(S)-1 or i%4==1 or i%4==2:
        B.append(name)
    else:
        A.append(name)
print(A)
print(B)
print(sum(A))
print(sum(B))
print(sum(A)-sum(B))        
