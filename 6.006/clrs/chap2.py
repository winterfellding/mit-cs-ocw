def insert_sort(ary):
    for i in range(1, len(ary)):
        key = ary[i]
        j = i - 1
        while j >= 0 and ary[j] > key:
            ary[j + 1] = ary[j]
            j -= 1
        ary[j + 1] = key            
          
ary = [5, 2, 4, 6, 1, 3]
print(ary)
insert_sort(ary)
print(ary)

"""
ex2.1-1
[31, 41, 59, 26, 41, 58]
[31, 41, 59, 26, 41, 58]
[31, 41, 59, 26, 41, 58]
[26, 31, 41, 59, 41, 58]
[26, 31, 41, 41, 59, 58]
[26, 31, 41, 41, 58, 59]
"""

"""
ex2.1-2
"""
def decrease_insert_sort(ary):
    for i in range(1, len(ary)):
        key = ary[i]
        j = i - 1
        while j >= 0 and ary[j] < key:
            ary[j + 1] = ary[j]
            j -= 1
        ary[j + 1] = key

ary = [31, 41, 59, 26, 41, 58]
print(ary)
decrease_insert_sort(ary)
print(ary)

"""
ex2.1-3
idx = 0
for idx in range(ary.length)
    if ary[idx] == v:
        return idx
return nil
"""

"""
ex2.1-4
"""
def add_two_bi_bit_arry(ary, ary2):
    carry = 0
    result = [None] * (len(ary) + 1)
    print(result)
    for i in range(len(ary) - 1, -1, -1):
        result[i + 1] = (carry + ary[i] + ary2[i]) % 2
        carry = (carry + ary[i] + ary2[i]) // 2
    result[0] = carry
    return result

ary = [1, 0, 1, 0]
ary2 = [0, 1, 0, 1]
print(add_two_bi_bit_arry(ary, ary2))
ary = [1, 1, 1, 1]
ary2 = [0, 0, 0, 1]
print(add_two_bi_bit_arry(ary, ary2))

