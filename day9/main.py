import sys
from itertools import product
from functools import reduce

m = [[int(x) for x in line.strip()] for line in sys.stdin]
N, M = len(m), len(m[0])


def get_adj(i, j):
  return \
    [
      (ii, jj) for (ii, jj) in
      product(
        range(max(0, i - 1), min(N, i + 2)),
        range(max(0, j - 1), min(M, j + 2))
      )
      if (ii != i) ^ (jj != j)
    ]


low_points = [
  (i, j) for (i, j) in product(range(N), range(M))
  if m[i][j] < min(m[ii][jj] for (ii, jj) in get_adj(i ,j))
]

print(sum(m[i][j] + 1 for (i, j) in low_points))


# part 2
def add_next(i, j, vis):
  if (i, j) not in vis:
    vis.add((i, j))
    for (ii, jj) in get_adj(i, j):
      if m[ii][jj] > m[i][j] and m[ii][jj] < 9:
        add_next(ii, jj, vis)
  return vis

basins = list(sorted([add_next(i, j, set()) for (i, j) in low_points], key=lambda x: -len(x)))

print(reduce(int.__mul__, [len(x) for x in basins[:3]]))
