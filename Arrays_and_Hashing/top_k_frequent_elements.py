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

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
# Time complexity: O(n) for counting the frequency and O(n) for iterating through the frequency list, resulting in O(n) overall.
# Space complexity: O(n) for the count dictionary and O(n) for the frequency list