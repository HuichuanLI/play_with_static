# -*- coding:utf-8 -*-
# @Time : 2022/1/2 7:02 下午
# @Author : huichuan LI
# @File : bin_norm.py
# @Software: PyCharm
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
import seaborn

seaborn.set()

n = 10
p_params = [0.35, 0.5, 0.8]
x = np.arange(0, n + 1)
f, ax = plt.subplots(len(p_params), 1)

for i in range(len(p_params)):
    p = p_params[i]
    y = binom(n=n, p=p).pmf(x)

    ax[i].vlines(x, 0, y, colors='red', lw=10)
    ax[i].set_ylim(0, 0.5)
    ax[i].plot(0, 0, label='n={}\n`$\\theta$`={}'.format(n, p), alpha=0)
    ax[i].legend()
    ax[i].set_xlabel('y')
    ax[i].set_xticks(x)

ax[1].set_ylabel('`$p(y|\\theta)$`')
plt.show()
