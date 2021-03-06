from playStats.hypothesis_testing import z_test, t_test, t_test_paired, chi2_test, F_test, cor_test, simple_linear_reg

from playStats.interval_est import main_ci_est, mean_diff_ci_z_test

if __name__ == "__main__":
    data1 = [41, 36, 12, 18, 23, 19, 8, 16, 11, 14, 18, 14, 34, 6, 30, 11, 1, 11, 4, 32]
    data2 = [23, 45, 115, 37, 29, 71, 39, 23, 21, 37, 20, 12, 13, 135, 49, 32, 64, 40, 77, 97]

    # print(z_test(data1, tail="both", mu=35, sigma1=5))
    # print(main_ci_est(data1, 0.05, 5))

    # print(z_test(data1, data2, tail="both", mu=0, sigma1=5, sigma2=15))
    # print(mean_diff_ci_z_test(data1, data2, 0.05, sigma1=5, sigma2=15))

    # one-sample t-test
    print(t_test(data1, tail="both", mu=35))
    # two-sample t-test
    print(t_test(data1, data2, tail="both", mu=0, equal=False))
    # paired t-test
    print(t_test_paired(data1, data2, tail="both", mu=0))

    print(chi2_test(data1, tail="both", sigma2=5))

    print(F_test(data1, data2, tail="both", ratio=1))

    score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    happy = [1, 3, 2, 6, 4, 5, 8, 10, 9, 7]
    print(cor_test(score, happy))
    print(simple_linear_reg(happy, score))
