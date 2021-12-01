nums = [int(x.strip()) for x in open('input.txt', 'r').readlines()]

print(sum(nums[i] > nums[i - 1] for i in range(len(nums))))

