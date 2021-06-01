#!/usr/bin/env python
# coding: utf-8

a = []
for i in range(2, 100):
    flag = 0
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 1
            break
    if flag == 0:
        a.append(i)

a.reverse()

S__A = []
S__B = []

for i in range(len(a)):
    if (sum(S__A) >= sum(S__B)):
        S__B.append(a[i])
    else:
        S__A.append(a[i])

S__A.reverse()
S__B.reverse()

print('Sa =', S__A)
print('Sb =', S__B)
print('差の絶対値 =', abs(sum(S__A) - sum(S__B)))