def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
nums = [5, 6, -3, 8, 1, 9, 2]
print("\n")
print(three_sum(nums))