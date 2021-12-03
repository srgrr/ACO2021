import sys

ones, nums = {}, []

for t, line in enumerate(sys.stdin):
  nums.append(''.join(x for x in reversed(line.strip())))
  for i, v in enumerate(nums[-1]):
    ones[i] = ones.get(i, 0) + int(v)

# part 1
max_len = max(ones.keys())

epsilon = sum((ones[b] > (t + 1 - ones[b])) * (2 ** b) for b in range(max_len + 1))
gamma = ~(epsilon) & (2 ** (max_len + 1) - 1)

print(epsilon * gamma)

# part 2

def filter_list(l, p, return_largest):
  if len(l) > 1:
    ones = [x for x in l if x & (2 ** p)]
    zeros = [x for x in l if not x & (2 ** p)]

    if return_largest:
      return ones if len(ones) >= len(zeros) else zeros
    return ones if len(ones) < len(zeros) else zeros
  return l


oxygen, co2 = [[int(''.join(reversed(num)), 2) for num in nums]] * 2

for b in range(max_len, -1, -1):
  oxygen, co2 = [filter_list(l, b, v) for (l, v) in [(oxygen, True), (co2, False)]]

print(oxygen[0] * co2[0])
