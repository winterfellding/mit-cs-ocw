def find_peak_1d(ary, lo, hi):
    mid = (hi - lo) // 2
    if ary[mid] < ary[mid - 1]:
        return find_peak_1d(ary, lo, mid - 1)
    elif ary[mid] < ary[mid + 1]:
        return find_peak_1d(ary, mid + 1, hi)
    else:
        return mid

test_ary = [3, 4, 1, 3, 5, 7, 9, 3, 13, 14]
print(find_peak_1d(test_ary, 0, len(test_ary) - 1))

