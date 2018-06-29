def counting_sort(ary):
    max_num = max(ary)
    nums = [0] * (max_num + 1)
    for i in ary:
        nums[i] += 1
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            for j in range(nums[i]):
                result.append(i)
    return result


# print(counting_sort([3, 4, 1, 1, 2, 3, 4, 5]))
   