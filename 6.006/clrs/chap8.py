def count_sort(array, count_array):
    for i in array:
        count_array[i] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i-1]
    result = [0] * len(array)
    for i in range(len(array)-1, -1, -1):
        print(count_array)
        print(i)
        result[count_array[array[i]]-1] = array[i]
        count_array[array[i]] = count_array[array[i]] - 1 
    return result

print(count_sort([6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2], [0]*7))