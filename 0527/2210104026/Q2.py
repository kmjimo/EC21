# -*- coding: utf-8 -*-
import sympy

#x = cosωt
x = sympy.Symbol('x',real=True)

#ヘロンの公式
a = 5*sqrt(5-4*x)
b = sqrt(49-40*x**2)
c = sqrt(104-40*x)
s = (a + b + c)/2
y = sqrt(s*(s-a)*(s-b)*(s-c))

#微分
g = sympy.diff(y,x)
#g=0なるxをyに代入
kai = solve(g)
Max = 0
for i in kai:
    if -1 <= i <= 1:
        if y.subs(x,i) > Max:
            Max = y.subs(x,i)

print('Max :',Max)