from playStats.descriptive_stats import average
from playStats.descriptive_stats import variance
import random
import matplotlib.pyplot as plt


def sample(num_of_sample, sample_sz, var):
    data = []
    for _ in range(num_of_sample):
        data.append(var([random.uniform(0.0, 1.0) for _ in range(sample_sz)]))
    return data


def variance_bias(data):
    """方差"""
    n = len(data)
    if n <= 1:
        return None
    mean_value = average(data)
    return sum((e - mean_value) ** 2 for e in data) / (n)


if __name__ == "__main__":
    data1 = sample(1000, 40, variance_bias)
    plt.hist(data1, bins="auto", rwidth=0.8)
    plt.axvline(x=average(data1), c="black")
    plt.axvline(x=1 / 12, c="red")
    print("bias:", average(data1), 1 / 12)
    plt.show()

    data2 = sample(1000, 40, variance)
    plt.hist(data2, bins="auto", rwidth=0.8)
    plt.axvline(x=average(data2), c="black")
    plt.axvline(x=1 / 12, c="red")
    print("bias:", average(data2), 1 / 12)
    plt.show()
