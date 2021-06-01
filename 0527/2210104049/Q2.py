#!/usr/bin/env python
# coding: utf-8

import sympy as spy

theta = spy.Symbol("theta", real = True)

a_x = 2
a_y = 0
p1_x = 5 * spy.cos(2 * theta)
p1_y = 5 * spy.sin(2 * theta)
p2_x = 10 * spy.cos(theta)
p2_y = 10 * spy.sin(theta)

S = spy.simplify((p1_x - a_x) * (p2_y - a_y) - (p2_x - a_x) * (p1_y - a_y)) / 2

S_ = spy.diff(S, theta)
theta_ = spy.solve(S_, theta)

answer = []

for i in theta_:
    x = S.subs(theta, i)
    answer.append(x)

print('面積Sの最大値 =', max(answer))