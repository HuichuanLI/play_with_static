# -*- coding:utf-8 -*-
# @Time : 2021/12/25 11:15 下午
# @Author : huichuan LI
# @File : random_process.py
# @Software: PyCharm

import scipy
import matplotlib.pyplot as plt
import seaborn
from math import sqrt

seaborn.set()

s0 = 10.0
T = 1.0
n = 244 * T
mu = 0.15
sigma = 0.2
n_simulation = 10000

dt = T / n
s_array = []

for i in range(n_simulation):
    s = s0
    for j in range(int(n)):
        e = scipy.random.normal()
        s = s + mu * s * dt + sigma * s * e * sqrt(dt)
    s_array.append(s)

plt.hist(s_array, bins=30, normed=True, edgecolor='k')
plt.show()
