import re
import sys
from collections import Counter

is_part_1 = int(sys.argv[1])

point_re = re.compile(r'(\d+),(\d+) \-> (\d+),(\d+)')

point_count = Counter()

for line in sys.stdin:
  x1, y1, x2, y2 = map(int, re.match(point_re, line).groups())
  if not is_part_1 or (x1 != x2) ^ (y1 != y2):
    point_count[(x1, y1)] += 1
    while (x1 != x2) or (y1 != y2):
      x1 += 1 if x2 > x1 else -1 if x2 < x1 else 0
      y1 += 1 if y2 > y1 else -1 if y2 < y1 else 0
      point_count[(x1, y1)] += 1

print(sum((val > 1) for val in point_count.values()))
