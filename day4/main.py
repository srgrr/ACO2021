import numpy as np
import sys

marked_sequence = map(int, sys.stdin.readline().split(','))
cartoncikos = []

for line in sys.stdin:
  cartoncillo = np.zeros((5, 5), dtype=np.uint32)
  for i in range(5):
    cartoncillo[i, :] = \
      list(map(int, sys.stdin.readline().strip().split()))
  cartoncikos.append(cartoncillo)

# Part 1
already_marked = set()

for cur in marked_sequence:
  already_marked.add(cur)
  winner_cartoncetes = [
    (i, x) for i, x in enumerate(cartoncikos) if
    any(
      all(x[i, j] in already_marked for j in range(5)) or
      all(x[j, i] in already_marked for j in range(5))
      for i in range(5)
    )
  ]
  if winner_cartoncetes:
    cartonbanks = winner_cartoncetes[0][1]
    print(sum(x for x in cartonbanks.flatten() if x not in already_marked) * cur)
  winner_indices = set([x[0] for x in winner_cartoncetes])
  cartoncikos = [cartoncikos[i] for i in range(len(cartoncikos)) if i not in winner_indices]
