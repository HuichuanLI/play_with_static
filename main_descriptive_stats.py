from collections import Counter

from playStats.descriptive_stats import frequency, mode

from playStats.descriptive_stats import median

from playStats.descriptive_stats import average

from playStats.descriptive_stats import rng

from playStats.descriptive_stats import quartile

from playStats.descriptive_stats import variance, std, covariance, cor

if __name__ == "__main__":
    data = [2, 1, 3]
    counter = Counter(data)
    print(counter.most_common())

    fre = frequency(data)
    print(fre)

    mode_elements, mode_count = mode(data)
    print(mode_count)

    if mode_elements:
        print(mode_elements)
        print(mode_count)
    else:
        print("Mode doesn't not exists.")

    data = [1, 4, 2, 3]
    print(median(data))

    data = [1, 4, 2, 3, 5, 6]
    print(median(data))

    print(average(data))

    # 测试极差
    data = [1, 4, 2, 3, 5]
    print(rng(data))

    print(quartile(data))

    data = [1, 4, 2, 3, 5, 8]
    print(variance(data))

    print(std(data))

    score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    happy = [1, 3, 2, 6, 4, 5, 8, 10, 9, 7]
    print(covariance(happy, score))
    print(cor(happy, score))
