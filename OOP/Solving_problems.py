x=5
nums = [int(x) for x in input().strip().split(' ')]
print(sum(nums) - max(nums), sum(nums) - min(nums))