# -*- coding:utf-8 -*-
# @Time : 2021/12/26 12:03 上午
# @Author : huichuan LI
# @File : random_process3.py
# @Software: PyCharm
import numpy as np
from hmmlearn import hmm

# 隐状态集合 Q
states = ['box1', 'box2', 'box3']
# 观测集合 V
observations = ['black', 'white']
# 初始概率 pi
start_probability = np.array([0.3, 0.5, 0.2])
# 状态转移矩阵 A
transition_probability = np.array([
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.2, 0.6, 0.2]
])

# 观测概率矩阵 B
emission_probability = np.array([
    [0.2, 0.8],
    [0.6, 0.4],
    [0.4, 0.6]
])

# 选用 MultinomialHMM 对离散观测状态建模
model = hmm.MultinomialHMM(n_components=len(states))
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

# 观测序列
obervation_list = np.array([0, 1, 0])
# 计算观测序列的概率，计算出来的是概率值的自然对数值
print(model.score(obervation_list.reshape(-1, 1)))
