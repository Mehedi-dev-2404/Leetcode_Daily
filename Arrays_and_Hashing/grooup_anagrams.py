
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = []

    for s in strs:
        found = False

        for group in groups:
            if sorted(s) == sorted(group[0]):
                group.append(s)
                found = True
                break
        if not found:
            groups.append([s])
        
    return groups
# Time complexity: O(n * m log m) where n is the number of strings and m is the average length of the strings (due to sorting each string).
# Space complexity: O(n * m) for storing the groups of anagrams.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_map = {}

    for s in strs:
        key = "".join(sorted(s))

        if key in anagram_map:
            anagram_map[key].append(s)
        else:
            anagram_map[key] = [s]
    
    return list(anagram_map.values())

# Time complexity: O(n * m log m) where n is the number of strings and m is the average length of the strings (due to sorting each string).
# Space complexity: O(n * m) for storing the groups of anagrams in the hash map.
