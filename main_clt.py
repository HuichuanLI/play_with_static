import random
import matplotlib.pyplot as plt

from playStats.descriptive_stats import average


def sample(num_of_sample, sample_sz):
    data = []
    for _ in range(num_of_sample):
        data.append(average([random.uniform(0.0, 1.0) for _ in range(sample_sz)]))
    return data


if __name__ == "__main__":
    data = sample(10000, 40)
    plt.hist(data, bins="auto", rwidth=0.8)
    plt.axvline(x=average(data), c='r')
    plt.show()
