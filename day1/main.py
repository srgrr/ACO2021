nums = [int(x.strip()) for x in open('input.txt', 'r').readlines()]
print(sum(nums[i - 1] < nums[i ] for i in range(1, len(nums))))
nums3 = [nums[i - 2] + nums[i - 1] + nums[i] for i in range(2, len(nums))]
print(sum(nums3[i - 1] < nums3[i] for i in range(1, len(nums3))))
