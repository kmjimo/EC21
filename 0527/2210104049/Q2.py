#!/usr/bin/env python
# coding: utf-8

import sympy as spy

# Θを定義する
theta = spy.Symbol("theta", real = True)

# 座標を定義する
a_x = 2
a_y = 0
p1_x = 5 * spy.cos(2 * theta)
p1_y = 5 * spy.sin(2 * theta)
p2_x = 10 * spy.cos(theta)
p2_y = 10 * spy.sin(theta)

# 面積を計算して簡略化する
S = spy.simplify((p1_x - a_x) * (p2_y - a_y) - (p2_x - a_x) * (p1_y - a_y)) / 2

# 求まったSを微分, その後極致を持つΘを求める
S_ = sym.diff(S, theta)
theta_ = sym.solve(S_, theta)

# 絶対値を考えて解候補から最大値を求める
answer = []

for i in theta_:
    x = S.subs(theta, i)
    answer.append(x)

print('面積Sの最大値 =', max(answer))