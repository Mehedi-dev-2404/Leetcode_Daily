def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)

    return [sorted_items[i][0] for i in range(k)]
# Time complexity: O(n log n) due to sorting the count dictionary.
# Space complexity: O(n) for storing the count of each unique number in the dictionary.