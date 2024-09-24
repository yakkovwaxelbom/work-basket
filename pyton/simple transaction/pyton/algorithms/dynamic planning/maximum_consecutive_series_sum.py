from typing import List


def maximum_consecutive_series_sum(series: List[int]) -> list[int]:
    if not series:
        return []

    opt = [0] * len(series)
    opt[0] = series[0]

    for i in range(1, len(series)):
        opt[i] = max(series[i], opt[i - 1] + series[i])

    sum_sub_series = max(opt)
    end = opt.index(sum_sub_series)

    begin = 0
    for i in range(end - 1, -1, -1):
        if opt[i] <= 0:
            begin = i + 1
            break

    return series[begin:end + 1]


a = [1, 2, -1, 2, -3, 2, 1, -5, 4]

print(maximum_consecutive_series_sum(a))
