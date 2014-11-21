#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Sort and count the number of comparisons done.
# This is a side-effect function: the array is sorted in place.

def quick_sort(array, start, end):
    comparisons = end - start - 1
    # Pivot variable is the *index* of the pivoting element.
    pivot = start # Choose different pivots...
    #pivot = end - 1 # Choose different pivots...
    #length = end - start
    #if length % 2 == 0:
    #    middle = length / 2
    #else:
    #    middle = length / 2 + 1
    #first = array[start]
    #mid = array[start + middle - 1]
    #last = array[end-1]
    #median = sorted([first, mid, last])[1]
    #pivot = array.index(median) # Choose different pivots...

    array[start], array[pivot] = array[pivot], array[start]
    pivot = start

    i = start + 1
    for j in xrange(start + 1, end):
        if array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[pivot], array[i - 1] = array[i - 1], array[pivot]
    pivot = i - 1
    if pivot - start > 1:
        comparisons += quick_sort(array, start, pivot)
    if end - pivot > 1:
        comparisons += quick_sort(array, pivot + 1, end)

    return comparisons


if __name__ == '__main__':
    array = []
    with open('QuickSort.txt') as fin:
        for num in fin:
            array.append(int(num))
    print quick_sort(array, 0, len(array)), array[:10]
