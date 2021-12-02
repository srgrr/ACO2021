import numpy as np
import sys

vec_functions = {
  'forward': lambda v, k: np.array([0, 1, 0]) * k + np.array([0, 0, 1]) * v[0] * k,
  'down': lambda v, k: np.array([1, 0, 0]) * k,
  'up': lambda v, k: np.array([-1, 0, 0]) * k,
}

# aim, horizontal, depth
v = np.zeros(3, dtype=np.int64)

for line in sys.stdin:
  vec_name, k = line.split()
  v += vec_functions[vec_name](v,  int(k))

print(v[1] * v[2])
