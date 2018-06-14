"""
insertion sort
"""
def insertion_sort(ary):
    if len(ary) <= 1:
        return ary
    for i in range(1, len(ary)):
        j = i - 1
        key = ary[i]
        while ary[j] > key and j >= 0:
            ary[j+1] = ary[j]
            j -= 1
        ary[j+1] = key

arry = [2, 1, 3, 4, 0]
print(arry)
insertion_sort(arry)
print(arry)


"""
merge sort
"""
def merge_sort(ary, start, end):
    mid = (end + start) // 2
    L = merge_sort(ary[start:mid], start, mid)
    R = merge_sort(ary[mid:end], mid, end)
    i, j, r = 0, 0, 0
    while i < len(L) and j < len(R):
        if ary[i] < ary[j]:
            ary[start+r] = L[i]
            i += 1
            r += 1
        else:
            ary[start+r] = R[j]
            j += 1
            r += 1
    
    for idx in range(i, len(L)):
        ary[start+r] = L[idx]
        r += 1
    
    for idx in range(j, len(R)):
        ary[start + r] = R[idx]
        r += 1

ary = [3, 2, 5, 32, 5, 7, 5, 3, 5, 7]
print(ary)
merge_sort(ary, 0, len(ary))
print(ary)