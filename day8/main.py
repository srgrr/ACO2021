import sys
from itertools import permutations
from collections import Counter

canon = [
  'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
  'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
]
pos2canon = {i: k for (i, k) in enumerate(canon)}
canon2pos = {k: i for (i, k) in enumerate(canon)}
alphabet = 'abcdefg'

# parts 1 and 2
total_1, total_2 = 0, 0
for line in sys.stdin:
  patterns, digits = [x.split() for x in line.split(' | ')]

  def map_num(num, mapper):
    return ''.join(x for x in sorted(mapper[y] for y in num))

  for mapping in permutations(alphabet):
    mapper = {k: v for k, v in zip(alphabet, mapping)}
    translated_patterns = [map_num(x, mapper) for x in patterns]
    if all(x in canon for x in translated_patterns):
      mapped_digits = [map_num(digit, mapper) for digit in digits]
      cnt = Counter(mapped_digits)
      total_1 += sum(cnt[pos2canon[i]] for i in [1, 4, 7, 8])
      total_2 += sum(10 ** (4 - i - 1) * canon2pos[mapped_digits[i]] for i in range(4))

print(total_1)
print(total_2)
