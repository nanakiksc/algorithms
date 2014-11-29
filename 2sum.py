#!/usr/bin/env python
#-*- coding:utf-8 -*-

numbers = []
with open('data/2sum.txt') as fin:
    for line in fin:
        numbers.append(int(line))
numbers.sort()

LOW, HIGH = -10000, 10000
left, right = 0, len(numbers) - 1
last_right = right
sums = set()

while left < right:
    pair_sum = sum((numbers[left], numbers[right]))
    while pair_sum > HIGH and left < right:
        right -= 1
        pair_sum = sum((numbers[left], numbers[right]))
        last_right = right

    while pair_sum >= LOW and left < right:
        sums.add(pair_sum)
        right -= 1
        pair_sum = sum((numbers[left], numbers[right]))
    
    right = last_right
    left += 1

print len(sums)
