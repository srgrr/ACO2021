import sys
from collections import Counter

part_num, num_days = map(int, sys.argv[1:])
fishes =  Counter([x for x in map(int, sys.stdin.readline().split(','))])

for _ in range(num_days):
  new_fishes = Counter()
  new_fishes[8] = fishes[0]
  for i in range(1, 9):
    new_fishes[i - 1] = fishes[i]
  new_fishes[6] += fishes[0]
  fishes = new_fishes

print(sum(fishes.values()))
