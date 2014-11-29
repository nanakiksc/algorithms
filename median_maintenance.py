#!/usr/bin/env python
#-*- coding:utf-8 -*-

from heapq import *

medians = [0]
length_medians = 0
low = []
length_low = 0
heapify(low)
high = []
heapify(high)
length_high = 0

with open('data/Median.txt') as fin:
    for line in fin:
        num = int(line)

        # Push where appropriate.
        if num > medians[-1]:
            heappush(high, num)
            length_high += 1
        else:
            heappush(low, num)
            length_low += 1

        # Rebalance if needed.
        if length_low - length_high > 1:
            heappush(high, low.pop(low.index(nlargest(1, low)[0])))
            length_high += 1
            length_low -= 1
        elif length_high - length_low > 1:
            heappush(low, heappop(high))
            length_low += 1
            length_high -= 1

        # Retrieve the current median.
        length_medians += 1
        if length_medians % 2:
            # If length_medians is odd...
            if length_high > length_low:
                # ...and high is bigger than low,
                # median is high's min.
                medians.append(nsmallest(1, high)[0])
                continue

        # If length_medians is even,
        # or length_medians is odd and low is bigger than high,
        # median is low's max.
        medians.append(nlargest(1, low)[0])

print sum(medians) % 10000
