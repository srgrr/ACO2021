import sys

nums = list(sorted(map(int, sys.stdin.readline().split(','))))

print(sum(abs(x - nums[len(nums) // 2]) for x in nums))

def pyramid(x):
  return x * (x + 1) // 2

pdiffs = [
  sum(pyramid(abs(x - y)) for x in nums)
  for y in range(min(nums), max(nums) + 1)
]

print(min(pdiffs))
