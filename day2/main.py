import numpy as np
import sys

dirvecs = {
  'forward': np.array([0, 1]),
  'down': np.array([1, 0]),
  'up': np.array([-1, 0])
}

v = np.zeros(2, dtype=np.int64)

for line in sys.stdin:
  vec_name, k = line.split()
  v += dirvecs[vec_name] * int(k)

print(v[0] * v[1])
