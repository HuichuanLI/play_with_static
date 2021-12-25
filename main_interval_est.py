from playStats.interval_est import main_ci_est, var_ci_est, mean_diff_ci_t_est, mean_diff_ci_z_test,var_ratio_ci_test

from playStats.descriptive_stats import average, variance, std

if __name__ == "__main__":
    salary_18 = [1484, 785, 1598, 1366, 1716, 1020, 1716, 785, 3113, 1601]
    salary_35 = [902, 4508, 3809, 3923, 4276, 2065, 1601, 553, 3345, 2182]

    # print(average(salary_18), main_ci_est(salary_18, 0.05))
    # print(average(salary_35), main_ci_est(salary_35, 0.05))
    #
    # print(std(salary_18), variance(salary_18), var_ci_est(salary_18, 0.05))
    # print(std(salary_35), variance(salary_35), var_ci_est(salary_35, 0.05))

    # 两个方差已知，且相等
    # print(mean_diff_ci_t_est(salary_18, salary_35, 0.05, True))
    # 两个方差未知，且不想等
    # print(mean_diff_ci_t_est(salary_18, salary_35, 0.05, False))

    # 两个方差已知的情况
    print(mean_diff_ci_z_test(salary_18, salary_35, 0.05, 1035, 1240))

    # 两个均值未知，方差比
    print(var_ratio_ci_test(salary_18, salary_35, 0.05))
