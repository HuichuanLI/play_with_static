# -*- coding:utf-8 -*-
# @Time : 2021/12/26 12:10 上午
# @Author : huichuan LI
# @File : markov_process.py
# @Software: PyCharm
import numpy as np

A = np.array([[0.7, 0.2, 0.1],
              [0.3, 0.5, 0.2],
              [0.2, 0.4, 0.4]])


def get_matrix_pow(matrix, n):
    ret = matrix
    for i in range(n):
        ret = np.dot(ret, A)
    print(ret)


get_matrix_pow(A, 3)
get_matrix_pow(A, 5)
get_matrix_pow(A, 10)
get_matrix_pow(A, 20)
get_matrix_pow(A, 100)

