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

def find_peak_2d(ary, r, start_col, col):
    mid = (col + start_col) // 2
    max_num, max_idx = 0, 0
    for i in range(r):
        if max_num < ary[i][mid]:
            max_num = ary[i][mid]
            max_idx = i
    if mid != 0 and ary[max_idx][mid] < ary[max_idx][mid - 1] :
        return find_peak_2d(ary, r, start_col, mid - 1)
    elif mid != col and ary[max_idx][mid] < ary[max_idx][mid + 1]:
        return find_peak_2d(ary, r, mid + 1, col)
    else:
        return mid, max_idx

test_ary = [[10, 8, 10, 10],
            [14, 13, 12, 11],
            [15, 9, 11, 21],
            [16, 17, 19, 20]]

print(find_peak_2d(test_ary, len(test_ary), 0, len(test_ary[0]) - 1))