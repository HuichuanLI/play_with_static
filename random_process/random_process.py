# -*- coding:utf-8 -*-
# @Time : 2021/12/25 11:15 下午
# @Author : huichuan LI
# @File : random_process.py
# @Software: PyCharm

import pandas as pd
import random

sample_list = []
person_num = 100000
round_num = 10000
for person in range(1, person_num + 1):
    money = 10
    for round in range(1, round_num + 1):
        result = random.randint(0, 1)
        if result == 1:
            money = money + 1
        elif result == 0:
            money = money - 1
        if money == 0:
            break
    sample_list.append([person, round, money])
sample_df = pd.DataFrame(sample_list, columns=['person', 'round', 'money'])
sample_df.set_index('person', inplace=True)

print("总轮数:{},总人数:{}".format(round_num, person_num))
print("输光赌本提前出局的人数:{}".format(person_num - len(sample_df[sample_df['round'] == round_num])))
print("赌满全场且盈利的人数:{}".format(len(sample_df[sample_df['money'] > 10])))
print("赌满全场且亏损的人数:{}".format(len(sample_df[sample_df['money'] <= 10][sample_df['money'] > 0])))

