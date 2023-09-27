#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys


def print_stats(file_size, stats):
    """prints the stats"""
    print("File size: {}".format(file_size))
    for k, v in sorted(stats.items()):
        if v > 0:
            print("{}: {}".format(k, v))


total_size = 0
count = 0
stats = {"200": 0, "301": 0, "400": 0, "401": 0,
         "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        line = line.split()
        if len(line) != 9:
            continue
        code = line[-2]
        if code in stats.keys():
            stats[code] += 1
        total_size += int(line[-1])
        count += 1
        if count == 10:
            count = 0
            print_stats(total_size, stats)
except KeyboardInterrupt as e:
    pass
finally:
    print_stats(total_size, stats)
