# 1: Brute Force
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1+i, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return []
# Time complexity: O(n^2)
# Space complexity: O(1)
