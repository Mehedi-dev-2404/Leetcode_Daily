class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
# Time complexity: O(n)
# Space complexity: O(n) in the worst case when all elements are unique