#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Sort and count the number of inversions in an array.

def sort_count(array):
    # Return the inversion count and the sorted subarray.
    n = len(array)
    if n <= 1:
        return array, 0
    else:
        mid = n / 2
        l_array, left = sort_count(array[:mid])
        r_array, right = sort_count(array[mid:])
        merged_array, split = merge_count_split_inv(l_array, r_array)
    return merged_array, left + right + split

def merge_count_split_inv(l_array, r_array):
    # Return the merged array and count the split inversions.
    merged_array = []
    inv_count = 0
    while l_array or r_array:
        if not l_array:
            merged_array.append(r_array.pop(0))
        elif not r_array:
            merged_array.append(l_array.pop(0))
        elif l_array[0] <= r_array[0]:
            merged_array.append(l_array.pop(0))
        else:
            merged_array.append(r_array.pop(0))
            inv_count += len(l_array)
    return merged_array, inv_count

if __name__ == '__main__':
    array = []
    with open('IntegerArray.txt') as fin:
        for num in fin:
            array.append(int(num))
    print sort_count(array)[1]
